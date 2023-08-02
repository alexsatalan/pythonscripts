from twilio.rest import Client

account_sid = 'ACcb6f055137cfb3370bad4a347932f9e5'
auth_token = '28ef06ac19e8f585e4edb58f1a84e470'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12545894787',
    body='barosaneeeee',
    to='+40762657641'
)

print(message.sid)
