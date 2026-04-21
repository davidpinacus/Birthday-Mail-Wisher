# 🎉 Birthday Email Automation (Python - SMTP + Pandas)

An automated Python script that sends personalized birthday emails using CSV data and email templates.
Never forget to wish someone again!

---

## 💡 What Makes This Unique?

* 📅 Automatically checks today's date
* 📂 Reads structured data from CSV
* ✉️ Sends **personalized emails**
* ⚡ Can run **automatically every day (cloud/server)**

---

## 📁 Project Structure

```id="q8k2xs"
.
├── main.py
├── birthdays.csv
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   ├── letter_3.txt
```

---

## 📊 How It Works

* Reads `birthdays.csv` using Pandas
* Checks today's date
* Finds matching birthdays
* Replaces `[NAME]` in template
* Sends email via SMTP

📄 Core logic: 

---

## 🔐 Gmail Setup

1. Enable **2-Step Verification**
2. Generate **App Password**
3. Use that password in the script

---

## ☁️ Run Automatically (PythonAnywhere)

You can run this script daily without keeping your PC ON.

### Steps:

1. Create account → https://www.pythonanywhere.com
2. Upload your project files
3. Open **Tasks → Scheduled Tasks**
4. Add a new scheduled task:

```
python3 /home/yourusername/birthday-email-automation/main.py
```

5. Set time (once per day)

✅ Now your script runs automatically every day!



