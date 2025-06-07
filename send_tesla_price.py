# send_tesla_price.py
import yfinance as yf
from datetime import datetime
from twilio.rest import Client
import os

# Fetch Tesla stock price
ticker = yf.Ticker("TSLA")
price = ticker.history(period="1d")['Close'].iloc[-1]

# Format message
today = datetime.now().strftime('%Y-%m-%d')
message_body = f"📈 Tesla (TSLA) closing price on {today}: ${price:.2f}"

# Read credentials from environment variables
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_whatsapp = 'whatsapp:+14155238886'  # Twilio sandbox
to_whatsapp = os.getenv('MY_WHATSAPP')   # Your verified number

# Send message via Twilio
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=message_body,
    from_=from_whatsapp,
    to=to_whatsapp
)

print("Message sent:", message.sid)