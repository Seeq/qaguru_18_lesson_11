from selene import browser, have, be
import allure

def test_simple(setup_browser):
    browser.open('https://google.com')
    pass

@allure.tag("allure test 1")
@allure.label("owner", "Sergey")
@allure.feature('Регистрация пользователя')
@allure.story('Регистрация пользователя с заполнением всех полей')
@allure.link("https://github.com", name='Testing')
def test_complete_form(setup_browser, file_path):
    browser.open('/automation-practice-form')
    browser.element('#fixedban').should(be.visible)
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")
    browser.driver.execute_script("$('header').remove()")
    browser.element('#app').should(be.visible)
    browser.element('#app').should(have.text('Practice Form'))
    browser.element('#firstName').type(text="Sergey")
    browser.element('#lastName').type(text="Labov")
    browser.element('#userEmail').type(text="qaguru@nosuchdomain.net")
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type(text="9111002030")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('select').element('option[value="7"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1989"]').click()
    browser.element('.react-datepicker__day--017').click()
    browser.element('#subjectsInput').type(text="English").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('input[type="file"]').set_value(file_path)
    browser.element('#currentAddress').type(text='First street, Second house, Third app.')
    browser.element('#state').click()
    browser.element('#react-select-3-option-3').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').click()
    browser.element('.table').all('td:nth-child(2)').should(have.exact_texts(
        "Sergey Labov",
        "qaguru@nosuchdomain.net",
        "Male",
        "9111002030",
        "17 August,1989",
        "English",
        "Sports, Reading, Music",
        "meme.png",
        "First street, Second house, Third app.",
        "Rajasthan Jaiselmer"))
