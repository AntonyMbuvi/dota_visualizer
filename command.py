import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


connection = mysql.connector.connect(
    host='localhost',
    user='Antony',
    password='--',
    database='trial_database'
)

cursor = connection.cursor()
"""
    CREATE TABLE heroes (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255),
        Primary_Attribute VARCHAR(255),
        Attack_Type VARCHAR(255),
        Attack_Range VARCHAR(255),
        Roles VARCHAR(255),
        Total_Pro_wins INT,
        Times_Picked INT,
        Times_Banned INT,
        Win_Rate DECIMAL(5, 2),
        Niche_Hero BOOLEAN
    )
"""
cat_cols = ['Primary_Attribute', 'Attack_Type', 'Niche_Hero']
int_cols = ['Attack_Range', 'Total_Pro_wins', 'Times_Picked', 'Times_Banned', 'Win_Rate']
selected_columns = input("Enter column names (comma-separated): ").split(",")

# Trim whitespace from column names
selected_columns = [column.strip() for column in selected_columns]

cursor.execute("""SELECT {} 
                FROM HEROES
                """. format(", ".join(selected_columns)))

rows = cursor.fetchall()

# Get the column names from the cursor description
column_names = [desc[0] for desc in cursor.description]

# Create a Pandas DataFrame from the rows and column names
df = pd.DataFrame(rows, columns=column_names)

#Univariant plots
for col_name in selected_columns:
    if col_name in int_cols:
        print(col_name)
        df[col_name].plot.hist(bins=5)
        plt.xlabel(col_name)
        plt.ylabel('Frequency')
        plt.title('{} Distribution'.format(col_name))
        plt.tight_layout()
        plt.savefig('dota_app/static/images/histogram{}.png'.format(col_name))
        plt.clf()

    if col_name in cat_cols:
        print(col_name)
        df[col_name].value_counts().plot(kind='bar')
        plt.xlabel(col_name)
        plt.ylabel('Count')
        plt.title('{} Distribution'.format(col_name))
        plt.tight_layout()
        plt.savefig('dota_app/static/images/bar{}.png'.format(col_name))
        plt.clf()

# Bivariant plots
the_len = len(selected_columns)
if the_len > 1:
    for x in range(the_len-1):
        for i in range(x+1, the_len):
            if selected_columns[x] in int_cols and selected_columns[i] in int_cols:
                df.plot.scatter(x=selected_columns[x], y=selected_columns[i])
                plt.title('{},{} Scatter'.format(selected_columns[x], selected_columns[i]))
                plt.savefig('dota_app/static/images/scatter{}{}.png'.format(x, i))
                plt.clf()
            
            if selected_columns[x] in cat_cols and selected_columns[i] in cat_cols:
                sb.countplot(data=df, x=selected_columns[x], hue=selected_columns[i])
                plt.title('{},{} Countplot'.format(selected_columns[x], selected_columns[i]))
                plt.savefig('dota_app/static/images/Countplot{}{}.png'.format(x, i))
                plt.clf()
            
            if (selected_columns[x] in cat_cols and selected_columns[i] in int_cols) or (selected_columns[i] in cat_cols and selected_columns[x] in int_cols):
                print('catplot')
                if selected_columns[x] in cat_cols:
                    sb.catplot(data=df, x=selected_columns[x], y=selected_columns[i])
                else:
                    sb.catplot(data=df, x=selected_columns[i], y=selected_columns[x])

                plt.title('{},{} Catplot'.format(selected_columns[x], selected_columns[i]))
                plt.savefig('dota_app/static/images/Catplot{}{}.png'.format(x, i))
                plt.clf()




# Commit the changes and close the connection
#connection.commit()
cursor.close()
connection.close()

print('was successful')

