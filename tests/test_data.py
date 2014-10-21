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
    AGE_LEFT = {'offset': 50, 'value': u'18 лет и старше'}
    AGE_RIGHT = {'offset': 100, 'value': u'до 62 лет'}
    AGE_LEFT_AND_RIGHT = {'l_offset': 100, 'r_offset': 200, 'value': u'от 25 до 50 лет'}
    RESTRICT = '12+'