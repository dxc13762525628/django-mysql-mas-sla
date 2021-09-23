# 项目说明

## 概述

```python
"""
项目继承django+mysql(主从复制)+redis+celery的一个小demo
"""
```

## MYSQL数据库主从复制

```python
第一步：配置主机的配置文件
# 两台数据库 一台在116从数据库 一台117主数据库 docker启动的服务(不用docker启动也行) 关于主数据谁主都行 两台数据库的版本尽量一致
# 1. 先找到主数据库(117)的配置文件my.cnf 我的是在docker 里面的/etc/mysql/my.cnf
vim my.cnf
# mysql版本一致
[mysqld]
# 主服务器唯一id
server-id=1
# 启用二进制文件
log-bin=路径/mysqlbin
# 启动错误日志(可选项) 
log-err = 自己本地路径/mysqlerr
# 根目录(可选性)
basedir=安装路径
# 临时目录(可选性)
tmpdir=安装路径
# 数据目录（可选择）
datadir=安装路径/Data/
# 设置读写权限
read-only=0
# 设置不用复制的数据库(可选)
binlog-ignore-db=mysql
# 设置需要复制的数据库(可选)
binlog-do-db=数据库名字
# 重启mysql服务
service mysql start

第二步配置 从机的配置文件
# 主机配置好就配置从机配置文件 同样还是在/etc/mysql/my.cnf里面
# my.cnf
[mysqld]
# 主服务器唯一id
server-id=2
# 启用二进制文件(可选)
log-bin=路径/mysqlbin
# 重启mysql服务
service mysql start
# 关闭两台服务器的防火墙
service iptables stop

第三步配置 主机配置授权账号
# 进入主机mysql
# 创建用户 这个名字和密码是从机授权的使用使用的
CREATE USER '名字'@'从机ip' IDENTIFIED BY '密码';
GRANT REPLICATION SLAVE ON *.* TO '名字'@'从机ip';
FLUSH PRIVILEGES;
# 刷新 情况是否授权
flush privileges
# 查询master的状态 并记录 File 和Position
show master status

第四部配置 从机的授权账号
change master to master_host='主机ip', 
master_user='名字(主机上面创建的用户名字)', 
master_password='密码(主机上面创建的用户密码)', 
master_log_file='mysql-bin.000001', # show master status 主机输入这个找到的对呀文件号
master_log_pos=894; # show master status 主机输入这个找到的对呀文件位置
# 启动从服务器复制功能
start slave;
# 查询从机状态 两个参数都是yes就是成功
show slave status\G
#Slave_IO_Running:Yes
#Slave_SQL_Running:Yes
```

### 关于mysql8.0加密问题

```python
# 修改主机授权的用户名密码
# mysql8.0的密码加密问题
# 修改加密方式
ALTER USER '名字'@'从机ip' IDENTIFIED WITH mysql_native_password BY '密码';
```



## Django读写分离配置

#### 第一步

```python

# settings.py文件添加数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb58',
        'HOST': '10.215.0.117',
        'PORT': "3306",
        'USER': "root",
        "PASSWORD": "123456",
    },
    'slave': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb58',
        'HOST': '10.215.0.116',
        'PORT': "3306",
        'USER': "root",
        "PASSWORD": "123456",
    }
}
```

#### 第二步

```python
# 在任意一个app下创建一个文件，创建一个类
# 我的是user下面的router_db下面的Router类
class Router:
    """
    读操作用slave库
    写操作用default
    """

    def db_for_read(self, model, **kwargs):
        """
        user读用主表
        cat读从表
        """
        app = model._meta.app_label
        if app == 'user':
            print("user读数据用主表")
            return 'default'
        print("cat使用从表数据库读数据")
        return 'slave'

    def db_for_write(self, model, **kwargs):
        print("使用主表数据库写数据")
        return 'default'

```

#### 第三步

```python
# settings.py加入配置
'-------------------------------主从数据库配置------------------------------------'
DATABASE_ROUTERS = ['user.router_db.Router',]
```

然后可以了快去试一试吧!!!!!!!