import urlparse
from components import \
    AuthForm, \
    TopMenu, CampaignName,  AgeRestrictions, MainForm, Age, SubmitButton, \
    Name, ActionBar, \
    Banner


class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)


class CreatePage(Page):
    PATH = '/ads/create'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def campaign_name(self):
        return CampaignName(self.driver)

    @property
    def restrictions(self):
        return AgeRestrictions(self.driver)

    @property
    def age(self):
        return Age(self.driver)

    @property
    def main_form(self):
        return MainForm(self.driver)

    @property
    def submit_button(self):
        return SubmitButton(self.driver)


class CampaignPage(Page):
    PATH = '/ads/campaigns'

    @property
    def name(self):
        return Name(self.driver)

    @property
    def action_bar(self):
        return ActionBar(self.driver)


class EditPage(Page):
    @property
    def banner(self):
        return Banner(self.driver)

    @property
    def restrictions(self):
        return AgeRestrictions(self.driver)

    @property
    def age(self):
        return Age(self.driver)