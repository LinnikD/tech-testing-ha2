# coding=utf-8
import os


class UserData(object):
    USERNAME = 'tech-testing-ha2-18@bk.ru'
    PASSWORD = os.environ['TTHA2PASSWORD']
    DOMAIN = '@bk.ru'


class BannerData(object):
    NAME = 'MEGA CAMPAIGN'
    HEADER = 'HEADER'
    TEXT = 'TEXT TEXT TEXT TEXT TEXT'
    URL = 'www.superurl.com'
    PICTURE = os.getcwd() + '/tests/res/kotik.jpg'
    AGE = {'offset': 50, 'value': u'18 лет и старше'}
    RESTRICT = '12+'