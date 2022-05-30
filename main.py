from browse import driver, dl_register, parser, attendance_link, attendance_check
from checkers import check_reg, check_refs
from configurations import read, write, register


def main() -> None:
    data = read()
    if not check_reg(data):
        register()
        main()

    browser = driver()
    dl_register(browser, data)

    if not check_refs(data):
        write(parser(browser))
        browser.close()
        main()

    while True:
        for i in data['refs']:
            attendance_check(browser,
                            attendance_link(browser, i))


if __name__ == '__main__':
    main()
