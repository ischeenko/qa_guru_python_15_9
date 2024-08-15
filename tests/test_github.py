import allure
from allure_commons.types import Severity
from allure_commons.types import AttachmentType
from selene import browser, by, be


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'ischenkoalex')
@allure.feature('Задачи в репозитории')
@allure.story('Пример теста без шагов и декоратора')
@allure.link('https://github.com', name='Testing')
def test_github_without_decorator():
    browser.open(browser.config.base_url)
    browser.element('.search-input-container').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example')
    browser.element('#query-builder-test').submit()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element("#issues-tab").click()
    browser.element(by.partial_text("#76")).should(be.visible)


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'ischenkoalex')
@allure.feature('Задачи в репозитории')
@allure.story('Пример теста c шагами')
@allure.link('https://github.com', name='Testing')
def test_with_allure_steps():
    with allure.step('Открываем главную страницу'):
        browser.open(browser.config.base_url)
    with allure.step('Нажимаем поиск и вводим текст'):
        browser.element('.search-input-container').click()
        browser.element('#query-builder-test').type('eroshenkoam/allure-example')
        browser.element('#query-builder-test').submit()
    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step('Нажимаем issues'):
        browser.element("#issues-tab").click()
    with allure.step('Проверяем наличие Issue c #76'):
        browser.element(by.partial_text("#76")).should(be.visible)
    with allure.step('Делаем финальный скриншот'):
        allure.attach(browser.driver.get_screenshot_as_png(), name="Test", attachment_type=AttachmentType.PNG)


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'ischenkoalex')
@allure.feature('Задачи в репозитории')
@allure.story('Пример теста c с декоратором')
@allure.link('https://github.com', name='Testing')
def test_with_allure_decorator():
    open_browser_with_github()
    search_repository('eroshenkoam/allure-example')
    click_repository('eroshenkoam/allure-example')
    open_issues()
    search_issue_with_number('#76')


@allure.step('Открываем браузер и гитхаб')
def open_browser_with_github():
    browser.open(browser.config.base_url)


@allure.step('Ищем репозиторий {repo}')
def search_repository(repo):
    browser.element('.search-input-container').click()
    browser.element('#query-builder-test').type(repo)
    browser.element('#query-builder-test').submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def click_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issues():
    browser.element("#issues-tab").click()


@allure.step('Проверяем наличие Issue c номером {number}')
def search_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)
