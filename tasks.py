import os
import requests
from dotenv import load_dotenv

load_dotenv()
domain = os.getenv("MAILGUN_DOMAIN")

def send_simple_message(to, subject, body):
    return requests.post(
		f"https://api.mailgun.net/v3/{domain}/messages",
		auth=("api", os.getenv("MAILGUN_API_KEY")),
		data={f"from": "Herik <mailgun@{domain}>",
			"to": [to],
			"subject": subject,
			"text": body})

def send_user_registration_email(email):
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {email} You have successfully signed up to the Stores REST API",
    )
