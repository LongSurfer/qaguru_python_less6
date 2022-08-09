from selene import command
from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser

from demoqa_tests.Controls import datepicker, tags_input, dropdown
from demoqa_tests.utils import resource


def test_register_student():
    # Act
    browser.open('automation-practice-form')
    # input student data
    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Evans')
    browser.element('#userEmail').type('my@mail.net')

    gender = browser.all('.custom-radio').element_by(have.exact_text('Male'))
    gender.click()

    phone_number = browser.element('#userNumber').type('0001230067')
    phone_number.click()

    birthday = datepicker.DatePicker(browser.element('#dateOfBirthInput'))
    birthday.set_by_enter('01', 'Jan', '2000')
    """
    # Alternative method:
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element(f'[value="{2000}"]').click()
    browser.element('.react-datepicker__month-select').element(f'[value="{0}"]').click()
    browser.element('.react-datepicker__day--001').click()
    
    OR
    
    browser.element('#dateOfBirthInput').perform(command.js.set_value('01 January 2000'))
    """

    subject = tags_input.TagsInput(browser.element('#subjectsInput'))
    subject.set_by_enter(from_='Eng')

    hobby_checkbox = browser.element(by.text('Sports'))
    hobby_checkbox.perform(command.js.scroll_into_view).click()
    '''
    # OR
    browser.element('#subjectsInput').type('Computer').press_enter()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Music')).click()
    '''

    upload_file = browser.element('#uploadPicture')
    upload_file.send_keys(resource('dev_godzillas.png'))
    '''
    browser.element('#uploadPicture').send_keys(resource('dev_godzillas.png'))
    '''

    browser.element('#currentAddress').type('Indonesia, Bali, Kuta')

    state = dropdown.Dropdown(browser.element('#state'))
    state.set_by_click('#react-select-3-option-0')

    city = dropdown.Dropdown(browser.element('#city'))
    city.set_by_click('#react-select-4-option-0')
    '''
    browser.element('#state').element('input').type('NCR').press_tab()
    browser.element('#city').element('input').type('Delhi').press_tab()
    '''

    browser.element('#submit').perform(command.js.click)

    # Assert
    def table_rows(index):
        return browser.element('.modal-dialog').all("table tr").all('td')[index]

    table_rows(1).should(have.exact_text("Alex Evans"))
    table_rows(3).should(have.exact_text("my@mail.net"))
    table_rows(5).should(have.exact_text("Male"))
    table_rows(7).should(have.exact_text("0001230067"))
    table_rows(9).should(have.exact_text("01 January,2000"))
    table_rows(11).should(have.exact_text("English"))
    table_rows(13).should(have.exact_text("Sports"))
    table_rows(15).should(have.exact_text("dev_godzillas.png"))
    table_rows(17).should(have.exact_text("Indonesia, Bali, Kuta"))
    table_rows(19).should(have.exact_text("NCR Delhi"))