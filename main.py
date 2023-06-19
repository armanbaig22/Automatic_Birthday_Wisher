import smtplib
import datetime as dt
import random
import pandas as pd
import os

my_email = "your-email"
# This is an app password generated from gmail account settings
# Using normal password may not work
password = "your-password"

# get current month and day
now = dt.datetime.now()
month = now.month
day = now.day

# get data from csv file
data_frame = pd.read_csv("birthdays.csv")

for i in range(len(data_frame)):
    # get the row
    row = data_frame.iloc[i]
    # check if the month and day matches
    if row["month"] == month and row["day"] == day:
        name = row["name"]
        email = row["email"]

        # Get all the .txt files from the Letters folder
        txt_files = [file for file in os.listdir('./Letters') if file.endswith('.txt')]
        # Select a random .txt file name from the list
        random_file = random.choice(txt_files)
        # Get the full path of the file
        selected_file = os.path.join('./Letters', random_file)
        # Open the file and read the content
        with open(selected_file, 'r') as file:
            letter = file.read()
        # Replace the [NAME] placeholder with the actual name
        letter = letter.replace("[name]", name)
        # Using smtplib to send the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg="Subject:Happy BirthDay\n\n{}".format(letter)
            )





