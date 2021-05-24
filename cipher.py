import string
def encoding(message,key1):
    alphabet=" "+string.ascii_lowercase
    positions=dict()
    for i in range(27):
        positions[alphabet[i]]=i
    encoded_message=""
    key=list(positions.keys())
    values=list(positions.values())
    index=0
    for i in message:
        index=positions[i]+key1
        if index>26:
            index=index-26-1
        encoded_message=encoded_message+key[index]
    return encoded_message
    
message = "hi this is my mini project"
key=3
print(encoding(message,key))