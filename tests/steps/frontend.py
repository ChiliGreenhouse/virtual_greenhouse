from behave import given, when, then

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

@given("that I am on the homepage")
def ensure_on_homepage(context):
    context.driver.get(context.frontend_url)

@given("that devices exist")
def ensure_devices_exist(context):
    devices = list(context.api_client.get_devices())

    context.devices = devices

    assert len(devices) > 0

@when("I navigate to the {page} page")
def navigate_to_page(context, page: str):
    context.driver.get(f"{context.frontend_url}/{page}")

    if page == "data":
        wait = WebDriverWait(context.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "data-regulation")))

@when("I press the {site} navbar button")
def press_navbar_button(context, site: str):
    nav = context.driver.find_element(By.LINK_TEXT, site)

    nav.click()

@then("all devices should be listed")
def ensure_all_devices_listed(context):
    html = context.driver.page_source

    soup = BeautifulSoup(html)

    devices = [tag.text for tag in soup.find_all("div", class_="item")]

    assert all([device.name in devices for device in context.devices])

@then("I should be on the {site} site")
def ensure_on_site(context, site: str):
    if site == "home":
        site = ""

    path = context.driver.current_url.split("/")[-1]

    assert path == site