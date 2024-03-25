import rpa as r

def submit_contact_form():
    r.init()

    r.url('http://3.139.109.244/')

    r.wait(10)

    r.type('name', 'Emmanuel')
    r.type('email', 'emmanuelchivunira@gmail.com')
    r.type('phoneNumber', '745370117')
    r.type('country', 'Kenya')
    r.type('message', 'RPA automation test')

    r.click('//*[@id="contact"]/form/button')

    r.wait(10)

    r.snap('page', 'success_message.png')

