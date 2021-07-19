# -*- coding: utf-8 -*-

import os
from mysayhello import app

SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'data.db'))