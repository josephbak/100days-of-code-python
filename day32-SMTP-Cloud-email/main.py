import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

load_dotenv("../.env")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")

#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user= my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="programming.31415@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
#
# date_of_birth = dt.datetime(year= 2001, month= 1, day=1, hour= 1)
# print(date_of_birth)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2: # 0 is Monday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Monday Motivation\n\n{quote}"
                            )
