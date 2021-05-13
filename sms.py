from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6388d57ea82b680a311b744f2d934c7e"
# Your Auth Token from twilio.com/console
auth_token  = "8054dafda873294c9283487240ca8886"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="your mobile number", 
    from_="+18504276101",
    body="Hello from Python!")

print(message.sid)
