class AuthEl(object):
    LOGIN = "#id_Login"
    PASSWORD = "#id_Password"
    DOMAIN = "#id_Domain"
    SUBMIT = "#gogogo>input"


class CreateEl(object):
    CAMPAIGN = '.base-setting__campaign-name__input'
    U_EMAIL = "#PH_user-email"
    HEADER = ".//input[@data-name='title']"
    TEXT = ".//textarea[@data-name='text']"
    URL = ".//li[@data-top='false']//input[@data-name='url']"
    PICTURE = ".banner-form__img-file"
    RESTRICTION = '[data-node-id="restrict"]'
    RESTRICTION_VAL = '[for="restrict-%s"]'
    MAIN_BUTTON = '.main-button-new'
    AGE_GROUP = '[data-name="age"]'
    AGE = '.campaign-setting__value'
    LEFT_SLIDER = '.range-slider__handle_left'
    RIGHT_SLIDER = '.range-slider__handle_right'


class CampaignEl(object):
    NAME = ".campaign-title__name"
    EDIT = '.control__link_edit'
    DELETE_BLOCK = '.control_campaign'
    DELETE = '.control__preset_delete'


class EditEl(object):
    BANNER_BLOCK = '.added-banner__banners-wrapper'
    HEADER = '.banner-preview__title'
    TEXT = '.banner-preview__text'
