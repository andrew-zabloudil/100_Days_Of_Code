# Motivational Quote Project
""" import smtplib
import datetime as dt
import random

my_gmail = os.getenv("my_gmail")
gmail_password = os.getenv("gmail_password")
my_yahoo = os.getenv("my_yahoo")
yahoo_app_password = os.getenv("yahoo_app_password")

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    with open("./Day 32 Birthday Wisher/quotes.txt", "r") as quotes:
        motivational_quotes = quotes.readlines()
        today_quote = random.choice(motivational_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=gmail_password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="birthdaywishertester@yahoo.com",
            msg=f"Subject:Weekly Motivation\n\n{today_quote}"
        ) """

# Birthday Wisher Project

import smtplib
import datetime as dt
import random
import csv
from dotenv import load_dotenv
import os

load_dotenv()

my_gmail = os.getenv("my_gmail")
gmail_password = os.getenv("gmail_password")
my_yahoo = os.getenv("my_yahoo")
yahoo_app_password = os.getenv("yahoo_app_password")

now = dt.datetime.now()
month = now.month
day = now.day

with open("./Day 32 Birthday Wisher/birthdays.csv", newline='') as birthday_list:
    birthdays = csv.reader(birthday_list, delimiter=",")
    for row in birthdays:
        if row[3] == str(month) and row[4] == str(day):
            name = row[0]
            email = row[1]
            letter_choice = random.randint(1, 3)
            with open(f"./Day 32 Birthday Wisher/letter_templates/letter_{letter_choice}.txt", 'r') as letter:
                message_body = letter.read().replace("[NAME]", name)

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_gmail, password=gmail_password)
                connection.sendmail(
                    from_addr=my_gmail,
                    to_addrs=email,
                    msg=f"Subject:Happy Birthday!\n\n{message_body}"
                )
