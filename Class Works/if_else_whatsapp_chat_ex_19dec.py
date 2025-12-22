chatStatus = int(input("Enter the chat status: "))
if chatStatus == 0:
    print("Sent, display single tick")
elif chatStatus == 1:
    print("Delivered, display double tick")
elif chatStatus == 2:
    print("Seen, display blue tick")
else:
    print("Unable to sent message, try again!!")
