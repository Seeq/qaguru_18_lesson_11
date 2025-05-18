from selene import browser
import allure
from qaguru_18_lesson_11.pages.registration_page import RegistrationPage


@allure.tag("allure test 1")
@allure.label("owner", "Sergey")
@allure.feature('Регистрация пользователя')
@allure.story('Регистрация пользователя с заполнением всех полей')
@allure.link("https://demoqa.com", name='test')

def test_complete_form(setup_browser):
    RegistrationPage()\
        .open_url()\
        .preconditions_met()\
        .fill_first_name("Sergey")\
        .fill_last_name("Labov")\
        .fill_email("qaguru@nosuchdomain.net")\
        .select_gender()\
        .fill_user_phone("9111002030")\
        .fill_date_of_birth('1989', '7', '017')\
        .fill_subjects("English")\
        .fill_hobbies()\
        .upload_img()\
        .fill_address("First street, Second house, Third app.")\
        .select_state()\
        .select_city()\
        .click_submit_button()\
        .should_registered_user_with(
            "Sergey Labov",
            "qaguru@nosuchdomain.net",
            "Male",
            "9111002030",
            "17 August,1989",
            "English",
            "Sports, Reading, Music",
            "meme.png",
            "First street, Second house, Third app.",
            "Rajasthan Jaiselmer")

