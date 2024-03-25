import rpa as r
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv('email')
password = os.getenv('password')


def amazon_login():
    r.init()

    # enter into the amazon site
    r.url('https://www.amazon.com/')
    r.wait(10)

    # click on sign in button
    r.click('nav-link-accountList')
    r.wait(5)

    # key in email address
    r.type('ap_email', email)
    r.click('continue')
    r.wait(5)

    # key in password
    r.type('ap_password', password)
    r.click('signInSubmit')
    r.wait(5)

    # take a snap of the home page
    r.snap('page', 'home_page.png')
