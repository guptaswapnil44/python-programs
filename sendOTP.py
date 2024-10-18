# send 4 digits OTP to an email address
import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""

""" 
- random.random() generates a random floating-point number between 0 and 1. e.g. 0.6770382022214881
- random.random() * 10 scales this random number up to a value between 0 and 10.
- math.floor() rounds this scaled number down to the nearest integer (from 0 to 9).
- digits is a string containing the characters "0123456789", representing the possible digits (0-9) for the OTP.
- digits[math.floor(random.random() * 10)] selects a digit from the digits string, using the calculated random index (an integer between 0 and 9). """

# Generating the OTP
for i in range(4):
    OTP +=  digits[math.floor(random.random() * 10)]

# Prepare the email message
msg =  "Your OTP is" + str(OTP) 

# Setting up the email server (Gmail in this case)
s = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS (Transport Layer Security) encryption
s.starttls()

# Sender and receiver email details
recv_emailid = "abc@gmail.com"
sender_emailid = "xyz@gmail.com"

# Login to the sender's Gmail account using app password (needs 2f auth enabled)
s.login(sender_emailid, "app_password")

# Sending the email
s.sendmail(sender_emailid, recv_emailid, msg)

# Asking the user to input the OTP
user_otp = input("Enter the OTP: ")

# Verifying if the entered OTP matches the sent OTP
if user_otp == OTP:
    print("Verified")
else:
    print("Incorrect OTP")

# Closing the connection to the email server
s.quit()
