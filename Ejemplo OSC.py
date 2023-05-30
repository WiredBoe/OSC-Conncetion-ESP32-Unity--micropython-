from uosc.client import Bundle, Client, create_message

# Set the IP address and port of the OSC server (the device receiving the messages)
ip = "192.168.60.95"
port = 8001

# Create an OSC client
osc = Client(ip, port)

# Create an OSC message with an address and some values
msg = create_message("/address/value1", 1, 2.0, "three")

# Send the message
osc.send(msg)
print("Message sent:", msg)

# You can also send multiple messages in a bundle
bundle = Bundle(
    create_message("/tounity", 1),
    create_message("/tounity/slider1", 70),
    create_message("/address3", "three")
)
osc.send(bundle)
print("Bundle sent:", bundle)