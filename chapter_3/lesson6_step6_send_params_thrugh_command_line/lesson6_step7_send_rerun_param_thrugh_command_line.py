link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")

"""
pytest -v --tb=line --reruns 1 --browser_name=chrome chapter_3/lesson6_step6_send_params_thrugh_command_line/lesson6_step7_send_rerun_param_thrugh_command_line.py 

"""