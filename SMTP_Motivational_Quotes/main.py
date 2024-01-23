import smtplib
import datetime as dt
import random

my_email = "cephiustechnologies@gmail.com"
password = "pass_here" # get from https://myaccount.google.com/apppasswords
to_email = "email_here"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:

    with open("quotes.txt", encoding='utf-8') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="rahi.coder@gmail.com", msg=f"Subject: Motiovation Quote\n\n{quote}")