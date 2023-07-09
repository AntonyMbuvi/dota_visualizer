from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, SubmitField, widgets, SelectField


class MultipleCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

# Usage in the form
class MyForm(FlaskForm):
    options = MultipleCheckboxField('Options', choices=[
        ('Primary_Attribute', 'Primary Attribute'),
        ('Attack_Type', 'Attack Type'),
        ('Attack_Range', 'Attack Range'),
        ('Niche_Hero', 'Niche Hero'),
        ('Total_Pro_wins', 'Total Pro wins'),
        ('Times_Picked', 'Times Picked'),
        ('Times_Banned', 'Times Banned'),
        ('Win_Rate', 'Win Rate')
    ])
    submit = SubmitField('Submit')


class CheckGraphs(FlaskForm):
    options = SelectField('Do you want to see the graphs', choices=[('yes', 'Yes'), ('no', 'No')])
    submit = SubmitField('Submit')