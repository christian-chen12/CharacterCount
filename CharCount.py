import pprint


print("Please type a message")
message = input()
count = {}

for char in message.upper():
    count.setdefault(char, 0)
    count[char] = count[char] + 1


text = pprint.pformat(count)
print(text)
