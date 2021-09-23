#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/3/22 15:30 
# @Author : dxc
# @File : celery_config.py
# -*- coding: utf-8 -*-
"""
celery的配置文件
"""
from datetime import timedelta

# import djcelery
import os
import django
from celery.schedules import crontab
from celery import platforms

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoMatSlave.settings")
django.setup()
# djcelery.setup_loader()

platforms.C_FORCE_ROOT = True

# celery执行任务的队列
CELERY_QUEUES = {
    # 定时任务队列
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    # 其他队列
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_type': 'direct',
        'binding_key': 'work_queue'
    }
}

# celery默认配置队列
CELERY_DEFAULT_QUEUE = 'work_queue'

# celery任务模块
CELERY_IMPORTS = (
    'user.tasks',
)

# 有些情况可以防止死锁
CELERYD_FORCE_EXECV = True

# 设置并发的worker数量
CELERYD_CONCURRENCY = 2

# 允许重试
CELERY_ACKS_LATE = True

# 每个worker最多执行100个任务被销毁，可以防止内存泄露
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务的最大运行时间 软处理 不报异常
CELERYD_TASK_SOFT_TIME_LIMIT = 12 * 30

# 定时任务
CELERYBEAT_SCHEDULE = {
    # 编写定时任务模块
    # 'blank_openid-task': {
    #     'task': 'get_user_openid-task',  # 任务名字自己命名
    #     'schedule': crontab(hour=20, minute=30),  # 执行时间
    #     'options': {
    #         'queue': 'beat_tasks'  # 指定队列
    #     }
    # },
    # 'top_device': {
    #     'task': 'user.tasks.change_top_device',
    #     'schedule': crontab(hour=7, minute=30),  # 执行时间
    #     'options': {
    #         'queue': 'beat_tasks'  # 指定队列
    #     }
    # },

}
