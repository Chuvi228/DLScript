from selenium import webdriver

PATTERN_COURSE = "https://dl.nure.ua/course/view.php?id="
PATTERN_ATTENDANCE = "https://dl.nure.ua/mod/attendance/view.php?id="
PATTERN_ATTENDANCE_CHECK = "https://dl.nure.ua/mod/attendance/attendance.php"


def view_option() -> webdriver.ChromeOptions():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return options


def hide_option() -> webdriver.ChromeOptions():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--enable-javascript')
    options.add_argument(
        "--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/72.0'")
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')
    return options
