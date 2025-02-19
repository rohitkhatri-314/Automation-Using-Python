import os, yagmail, pandas
my_email=os.getenv('email')
my_pass=os.getenv('password')
# print(my_email)

subject= 'automating emails using python'

# yurg tiiq xlhh iwzc

df=pandas.read_csv('Contacts.csv')

for index,rows in df.iterrows():
    
    content=f"""
Nothing but I am just trying to automate Emails using Python.
Sorry to Disturb you {rows['name']}.
Yours faithful, Rohit
"""
    yag=yagmail.SMTP(user=my_email, password=my_pass)
    yag.send(to=rows['email'],subject=subject,contents=content)
    print(f"Email Sent to {rows['name']}")

