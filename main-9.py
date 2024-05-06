import base64

def encode_message(message):

    encoded_message = base64.b64encode(message.encode()).decode()
    return encoded_message

def decode_message(encoded_message):

    decoded_message = base64.b64decode(encoded_message.encode()).decode()
    return decoded_message

# Example usage

original_message = "Hello, World!"
encoded = encode_message(original_message)
decoded = decode_message(encoded)

print(f"Original Message: {original_message}")
print(f"Encoded Message: {encoded}")
print(f"Decoded Message: {decoded}")
