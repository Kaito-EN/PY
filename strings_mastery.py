message = "hello world"
message = message.replace("world","RASIMAAAA")
words = message.split()
print(len(words))
print (len(message))
print(message[0:8])
print(message[9])
print(message.upper())
print(message.count("hello"))
print(message.find("RASIMAAAA"))
reverse_message = message[::-1]
print(reverse_message)