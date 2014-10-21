# coding=utf-8
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select, WebDriverWait
from html_elements import CreateEl, AuthEl, CampaignEl, EditEl


#Base Object
class Component(object):
    def __init__(self, driver):
        self.driver = driver


#AuthPage
class AuthForm(Component):
    def set_login(self, login):
        self.driver.find_element_by_css_selector(AuthEl.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_css_selector(AuthEl.PASSWORD).send_keys(pwd)

    def set_domain(self, domain):
        select = self.driver.find_element_by_css_selector(AuthEl.DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(AuthEl.SUBMIT).click()


#CreatePage
class TopMenu(Component):
    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(CreateEl.U_EMAIL).text
        )


class CampaignName(Component):
    def set_name(self, name):
        el = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(CreateEl.CAMPAIGN)
        )
        el.clear()
        el.send_keys(name)


class MainForm(Component):
    def set_header(self, header):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(CreateEl.HEADER)
        )
        element.send_keys(header)

    def set_text(self, text):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(CreateEl.TEXT)
        )
        element.send_keys(text)

    def set_url(self, url):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(CreateEl.URL)
        )
        element.send_keys(url)

    def set_picture(self, pic):
        element = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(CreateEl.PICTURE)
        )
        element.send_keys(pic)


class Age(Component):
    def choose_age(self, offset):
        el = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(CreateEl.AGE_GROUP)
        )
        age_el = WebDriverWait(el, 30, 0.5).until(
            lambda e: e.find_element_by_css_selector(CreateEl.AGE)
        )
        age_el.click()
        left = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(CreateEl.LEFT_SLIDER)
        )
        ac = ActionChains(self.driver)
        ac.click_and_hold(left).move_by_offset(offset, 0).release().perform()

    def get_age(self):
        el = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(CreateEl.AGE_GROUP)
        )
        age_el = WebDriverWait(el, 30, 0.5).until(
            lambda e: e.find_element_by_css_selector(CreateEl.AGE)
        )
        return age_el.text


class AgeRestrictions(Component):
    def choose_restriction(self, age_val):
        block = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(CreateEl.RESTRICTION)
        )
        block.click()

        el = WebDriverWait(self.driver, 30, 0.5).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, CreateEl.RESTRICTION_VAL % age_val))
        )
        el.click()

    def get_restrictions(self):
        el = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(CreateEl.RESTRICTION))
        return el.text


class SubmitButton(Component):
    def press(self):
        el = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(CreateEl.MAIN_BUTTON))
        el.click()


#CampaignPage
class Name(Component):
    def get_name(self):
        el = WebDriverWait(self.driver, 7, 0.1).until(
            lambda d: d.find_element_by_css_selector(CampaignEl.NAME)
        )
        return el.text


class ActionBar(Component):
    def edit(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(CampaignEl.EDIT)
        ).click()

    def delete(self):
        block = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(CampaignEl.DELETE_BLOCK)
        )
        el = WebDriverWait(block, 30, 0.1).until(
            lambda b: b.find_element_by_css_selector(CampaignEl.DELETE)
        )
        el.click()


#EditPage
class Banner(Component):
    def get_banner_header(self):
        block = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(EditEl.BANNER_BLOCK)
        )
        el = WebDriverWait(block, 30, 0.1).until(
            lambda b: b.find_element_by_css_selector(EditEl.HEADER)
        )
        return el.text

    def get_banner_text(self):
        block = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(EditEl.BANNER_BLOCK)
        )
        el = WebDriverWait(block, 30, 0.1).until(
            lambda b: b.find_element_by_css_selector(EditEl.TEXT)
        )
        return el.text
