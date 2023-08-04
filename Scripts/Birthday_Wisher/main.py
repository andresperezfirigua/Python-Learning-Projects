import pandas
import smtplib
import random
import datetime as dt

now = dt.datetime.now()
content = ''

data = pandas.read_csv('birthdays.csv')
birthdays = data.to_dict(orient='records')

source_email = 'your email address here'
password = 'your generated app password here'

for item in birthdays:
    if item['month'] == now.month and item['day'] == now.day:
        template_letter = f'letter_templates/letter_{random.randint(1, 3)}.txt'
        with open(template_letter) as file:
            content = file.read()

        content = content.replace('[NAME]', item['name'])

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=source_email, password=password)
            connection.sendmail(
                from_addr=source_email,
                to_addrs=item['email'],
                msg=f'Subject:Happy birthday\n\n{content}'
            )
