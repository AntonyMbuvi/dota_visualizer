from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_password'

from dota_app import routes