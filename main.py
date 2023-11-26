from reply_message import ReplyMessage

user_input = input("Enter some text: ")
reply = ReplyMessage().generate_response(user_input)
print("Coda:", reply)
