#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2017/8/17 9:16
# Author : lixingyun
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sys

sys.path.append('../')
from lib2 import hash_table

# 初始化数据库连接:
# 用法：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名' ！！！
engine = create_engine("mysql://root:123456@db.huomaotv.com.cn/lucky", encoding='utf-8', echo=False)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
# 创建对象的基类:
Base = declarative_base()


# 定义User对象: //与原数据表要对应！！！！！！
class User(Base):
    # 表的名字:
    __tablename__ = 'auth_user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    username = Column(String(20))




# 以上代码完成SQLAlchemy的初始化和具体每个表的定义。如果有其他表则继续定义其他class

# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：！！！！！

# 创建新User对象:！！！！！！！！！！！
new_user = User(id='22', username='12')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()

# users = session.query(User).one()
# for user in users:
#     print(user.id)

# 关闭session:
session.close()
