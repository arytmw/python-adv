import time
import requests
import smtplib

url = "https://..." #https://httpbin.org/status/404
email = "email@example.com"
password = "sensitive"

def webmail():
    try:
        result = requests.get(url)
        if result.status_code != 200:
            time.sleep(10)
            result = requests.get(url)
            if result.status_code != 200:
                send = smtplib.SMTP('smtp.gmail.com',587)
                send.starttls()
                send.login(email,password)
                message = "The webpage is not responding. Please troubleshoot."
                send.sendmail(email,email,message)
                send.quit()
        else:
            pass
    except Exception as err:
        print(f"Error: {err}")

webmail()
