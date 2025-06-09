# send_tesla_price.py
import yfinance as yf
from datetime import datetime
from twilio.rest import Client
import os

# Fetch Tesla current stock price
ticker = yf.Ticker("TSLA")
price = ticker.fast_info['last_price']  # Current real-time price (if available)

# Format message
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
message_body = f"🚀 Tesla (TSLA) current price as of {now}: ${price:.2f}"

# Read credentials from environment variables
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_whatsapp = 'whatsapp:+14155238886'  # Twilio sandbox
to_whatsapp = os.getenv('MY_WHATSAPP')   # Your verified number

# Debug info
print("TWILIO_SID:", account_sid[:6])  # Should print "ACxxxx"
print("AUTH TOKEN set:", auth_token is not None)
print("TO WHATSAPP:", to_whatsapp[:6])

# Send message via Twilio
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=message_body,
    from_=from_whatsapp,
    to=to_whatsapp
)

print("Message sent:", message.sid)