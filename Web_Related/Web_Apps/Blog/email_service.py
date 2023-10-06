import smtplib

EMAIL = 'Your email here'
PASSWORD = 'Your app generated password here'


def send_email(form_data):
    print(f"Name: {form_data['name']}\n"
          f"Email: {form_data['email']}\n"
          f"Phone: {form_data['phone']}\n"
          f"Message: {form_data['message']}"
          )

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs='Destination email here',
            msg=f"Subject:Blog reader message!\n\n"
                f"Hey there,\n"
                f"Name: {form_data['name']}\n"
                f"Email: {form_data['email']}\n"
                f"Phone: {form_data['phone']}\n"
                f"Message: {form_data['message']}"
        )
