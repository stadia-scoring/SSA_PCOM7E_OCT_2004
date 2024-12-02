import socket
from cryptography.fernet import Fernet
import json
import os

# Generate or load the shared key
def get_or_create_key():
    key_file = "key.key"
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
        print(f"Key generated and saved to {key_file}")
    else:
        with open(key_file, "rb") as f:
            key = f.read()
        print(f"Key loaded from {key_file}")
    return key

key = get_or_create_key()
cipher = Fernet(key)

# Decrypt the message based on its structure
def decrypt_message(data, cipher):
    try:
        # Attempt to parse the data as JSON
        msg = json.loads(data.decode())

        # If the message has an "encrypted" field, it's selectively encrypted
        if "encrypted" in msg:
            encrypted_data = msg["encrypted"]
            decrypted_sensitive = json.loads(cipher.decrypt(encrypted_data.encode()))
            msg.update(decrypted_sensitive)  # Merge decrypted sensitive fields back into the message
            del msg["encrypted"]
        else:
            # If no "encrypted" field, assume fully encrypted payload
            msg = json.loads(cipher.decrypt(data).decode())
        
        return msg
    except Exception as e:
        print(f"Error during decryption: {e}")
        return None

# Main server function
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("127.0.0.1", 65432))
        server_socket.listen()
        print("Server listening on 127.0.0.1:65432...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connection from {addr}")
                data = conn.recv(1024)
                if not data:
                    print("No data received.")
                    continue

                # Debug: Print raw data received
                print(f"Raw data received: {data}")

                # Decrypt the message
                decrypted_message = decrypt_message(data, cipher)
                if decrypted_message:
                    print("Decrypted Message:", decrypted_message)
                    conn.sendall(b"Message received")
                else:
                    conn.sendall(b"Decryption error")

if __name__ == "__main__":
    start_server()
