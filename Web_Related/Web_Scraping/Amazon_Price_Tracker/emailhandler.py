import smtplib

EMAIL = ''
PASSWORD = ''


class EmailHandler:
    def __init__(self, url, product, price):
        self.url = url
        self.product = product
        self.price = price

    def send_price_alert(self):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs='Destination email here',
                msg=f'Subject:Amazon Low Price Alert\n\nHey there,\nThe price for the following item has gone down:\n'
                    f'Product: {self.product}\nPrice: {self.price}\nProduct URL: {self.url}\n\nBuy now!'
            )

