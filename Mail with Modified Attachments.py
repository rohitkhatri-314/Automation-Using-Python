import os,yagmail,pandas

email=os.getenv('email')
password=os.getenv('password')

yag=yagmail.SMTP(user=email, password=password)

def createFile(filename, content):
    with open(filename,'w') as file:
        file.write(content)
        
df=pandas.read_csv('Contacts Pay.csv')

for index,rows in df.iterrows():
    name=rows['name']
    email_address=rows['email']
    amount=rows['amount']
    
    createFile(name +'.txt', str(amount))
    
    subject="Your bill is due"
    
    content=[f"""Hey {name},
    Your bill is due with the amount {amount}
    Please Pay it ASAP.
    """, f'{name}.txt']
    
    yag.send(to=email_address,subject=subject,contents=content)
    print(f'Email sent to {name}')