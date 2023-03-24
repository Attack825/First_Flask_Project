# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

app = Flask('tf_idf')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True)

from tf_idf import views
