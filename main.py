import amazon_automation
import amazon_login
import time
import leja_automation


def main():
    amazon_login.amazon_login()
    time.sleep(5)
    amazon_automation.amazon_searchItem()

    # leja_automation.submit_contact_form()


if __name__ == "__main__":
    main()
