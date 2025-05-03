import os, yagmail, time
from datetime import datetime as dt
my_email=os.getenv('email')
my_pass=os.getenv('password')
# print(my_email)
receiver='work.rohitkhatri@gmail.com'
subject= 'automating emails using python'
content="""
Nothing but I am just trying to automate Emails using Python.
Sorry to Disturb you.
Yours faithful, Rohit
"""
# yurg tiiq xlhh iwzc
while True:
    now = dt.now()
    if now.hour==12 and now.minute==50 :
        yag=yagmail.SMTP(user=my_email, password=my_pass)
        yag.send(to=receiver,subject=subject,contents=content)
        print('Email Sent')
        time.sleep(60)

