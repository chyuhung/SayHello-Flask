# -*- coding: utf-8 -*-

from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy

app=Flask("mesayhello")
app.config.from_pyfile=('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db=SQLAlchemy(app)
