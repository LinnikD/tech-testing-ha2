# coding=utf-8
import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote
from PageObjects.pages import AuthPage, CreatePage, CampaignPage, EditPage
from test_data import UserData, BannerData


def login(driver):
        auth_page = AuthPage(driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(UserData.DOMAIN)
        auth_form.set_login(UserData.USERNAME)
        auth_form.set_password(UserData.PASSWORD)
        auth_form.submit()


def create_simple_campaign(driver):
        create_page = CreatePage(driver)
        create_page.open()

        create_page.campaign_name.set_name(BannerData.NAME)
        main_from = create_page.main_form
        main_from.set_header(BannerData.HEADER)
        main_from.set_picture(BannerData.PICTURE)
        main_from.set_text(BannerData.TEXT)
        main_from.set_url(BannerData.URL)


def submit(driver):
        create_page = CreatePage(driver)

        create_page.submit_button.press()


def delete_campaign(driver):
        campaign_page = CampaignPage(driver)
        campaign_page.open()
        campaign_page.action_bar.delete()


class Tests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_auth(self):
        login(self.driver)

        create_page = CreatePage(self.driver)
        create_page.open()
        email = create_page.top_menu.get_email()

        self.assertEqual(UserData.USERNAME, email)

    def test_simple_banner(self):
        login(self.driver)

        create_simple_campaign(self.driver)

        #Может потребоваться для FIREFOXа
        #import time
        #time.sleep(2)

        submit(self.driver)

        campaign_page = CampaignPage(self.driver)
        campaign_page.open()
        name = campaign_page.name.get_name()
        self.assertEquals(BannerData.NAME, name)
        campaign_page.action_bar.edit()

        edit_page = EditPage(self.driver)

        header = edit_page.banner.get_banner_header()
        text = edit_page.banner.get_banner_text()
        self.assertEqual(BannerData.HEADER, header)
        self.assertEqual(BannerData.TEXT, text)

        delete_campaign(self.driver)

    def test_age_restrict(self):
        login(self.driver)

        create_simple_campaign(self.driver)
        create_page = CreatePage(self.driver)
        create_page.restrictions.choose_restriction(BannerData.RESTRICT)

        submit(self.driver)

        campaign_page = CampaignPage(self.driver)
        campaign_page.open()
        campaign_page.action_bar.edit()

        edit_page = EditPage(self.driver)
        restrict = edit_page.restrictions.get_restrictions()
        self.assertEquals(BannerData.RESTRICT, restrict)

        delete_campaign(self.driver)

    def test_age(self):
        login(self.driver)

        create_simple_campaign(self.driver)
        create_page = CreatePage(self.driver)
        create_page.age.choose_age(BannerData.AGE['offset'])

        submit(self.driver)

        campaign_page = CampaignPage(self.driver)
        campaign_page.open()
        campaign_page.action_bar.edit()

        edit_page = EditPage(self.driver)
        age = edit_page.age.get_age()
        self.assertEquals(BannerData.AGE['value'], age)

        delete_campaign(self.driver)


