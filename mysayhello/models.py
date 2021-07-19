# -*- coding: utf-8 -*-

from mysayhello import db
from datetime import datetime

#定义message模型
class Message(db.Model):
    id=db.Colume(db.Interger,primary_key=True)
    body=db.Colume(db.String(200))
    name=db.Colume(db.String(20))
    timestamp=db.Colume(db.Datetime,default=datetime.now,index=True)