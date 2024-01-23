

FROM_EMAIL = "enter_email_from"
TO_EMAIL = "enter_email_to"
PASSWORD = "enter_pass"

import smtplib
import datetime as dt
import random
import pandas


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row['month'], row['day']): row for _, row in data.iterrows()}



today = dt.datetime.now()
if (today.month, today.day) in birthdays_dict:
    print("I found a perfect match")
    dict = birthdays_dict[(today.month, today.day)]
    print(f"name: {dict["name"]} | email: {dict.email}")

    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        content = letter.read()
        new_content = content.replace("[NAME]", dict["name"])
        print(new_content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL, to_addrs=dict["email"], msg=f"Subject: Happy Birthday\n\n{new_content}")


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



