

import os
from utils.functions import get_db_uri

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 页面模版
template_dir = os.path.join(BASE_DIR, 'templates')
# 静态模版
static_dir = os.path.join(BASE_DIR, 'static')

DATABASE = {
    # 用户
    'USER': 'root',
    # 密码
    'PASSWORD': 'jy2190883',
    # 地址
    'HOST': '47.106.144.34',
    # 端口
    'PORT': '3306',
    # 数据库
    'DB': 'mysql',
    # 驱动
    'DRIVER': 'pymysql',
    # 数据库名称
    'NAME': 'flask3'
}
# 连接数据库
SQLACHEMY_DATABASE_URI = get_db_uri(DATABASE)
