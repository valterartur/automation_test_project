def test_guest_can_go_to_login_page(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()