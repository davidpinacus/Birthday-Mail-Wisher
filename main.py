
import smtplib
import datetime as dt
import pandas 

your_mail="Your Email"
your_password="Your Password" # go to https://myaccount.google.com/ and search:-  App passwords, Give an App name eg-" Birthday Mail wisher" and it will give a password 

now = dt.datetime.now()
day = now.day
month = now.month
data = pandas.read_csv("birthdays.csv")
birth_day = data[(data["month"] == month) & (data["day"] == day)]

if not birth_day.empty:
    name = birth_day.iloc[0]["name"]
    email = birth_day.iloc[0]["email"]
    
    with open("letter_templates/letter_3.txt") as file:
        letter=file.read()
        update_name=letter.replace("[NAME]", name)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=your_mail, password=your_password)
        connection.sendmail(
            from_addr=your_mail,
            to_addrs=email,
            msg=f"Subject:Hello \n\n {update_name}"
        )

