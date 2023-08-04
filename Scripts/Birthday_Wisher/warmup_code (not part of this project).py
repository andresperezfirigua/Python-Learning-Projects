# import smtplib
# source_email = 'your email address here'
# password = 'your generated app password here'
#
# with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#     connection.starttls()
#     connection.login(user=source_email, password=password)
#     connection.sendmail(
#     from_addr=source_email,
#     to_addrs='destination email here',
#     msg='Subject:Test mail\n\nHey,this is my second test email.'
#     )


# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
# year = now.year
# print(year)
# month = now.month
# print(month)
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1990, month=9, day=30)
# print(date_of_birth)


# Challenge #1

# import smtplib
# import datetime as dt
# import random
#
# source_email = 'your email address here'
# password = 'your generated app password here'
# quotes = []
# expected_day = 4
# now = dt.datetime.now()
# day_of_week = now.weekday()
#
# if expected_day == day_of_week:
#     with open('quotes.txt') as file:
#         for quote in file:
#             quotes.append(quote.strip())
#
#     selected_quote = random.choice(quotes)
#
#     with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#         connection.starttls()
#         connection.login(user=source_email, password=password)
#         connection.sendmail(
#             from_addr=source_email,
#             to_addrs=source_email,
#             msg=f"Subject:Monday's motivational quote\n\n{selected_quote}"
#         )
# else:
#     print("It's not a quote day")
