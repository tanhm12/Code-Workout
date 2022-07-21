import csv, smtplib, ssl

message = """Subject: Your grade

Hi this is aimebot"""
from_address = "no-reply@aimesoft.com"
password = "mCy6tV4k2z5R"

context = ssl.create_default_context()
with smtplib.SMTP("211.125.90.230", 25) as server:
    server.login(from_address, password)
    
    server.sendmail(
        from_address,
        "tanhm.aime@gmail.com",
        message,
    )