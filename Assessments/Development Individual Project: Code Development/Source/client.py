import socket
import time
import json
from cryptography.fernet import Fernet

# Load the shared key
def load_key():
    key_file = "key.key"
    try:
        with open(key_file, "rb") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {key_file} not found. Ensure the server has generated the key.")
        exit(1)

key = load_key()
cipher = Fernet(key)

# Test message
message = {
    "device_id": "Device_001",
    "command": "Turn on lights",
    "metadata": {"timestamp": "2024-12-01T12:00:00Z"}
}

# Selective encryption
def selective_encrypt(msg, cipher):
    sensitive = {"device_id": msg["device_id"], "command": msg["command"]}
    encrypted = cipher.encrypt(json.dumps(sensitive).encode())
    msg["encrypted"] = encrypted.decode()
    msg["device_id"], msg["command"] = None, None
    return json.dumps(msg)

# Full encryption
def full_encrypt(msg, cipher):
    return cipher.encrypt(json.dumps(msg).encode()).decode()

# Test encryption and round-trip time
def test_client(iterations=1, verbose=True):
    selective_rtt = []
    full_rtt = []

    print("Measuring Selective Encryption...")
    for i in range(iterations):
        selective_message = selective_encrypt(message.copy(), cipher)
        if verbose:
            print(f"Selective Encrypted Message: {selective_message}")
        selective_rtt.append(send_message_to_server(selective_message, mode="Selective", verbose=verbose))

    print("Measuring Full Encryption...")
    for i in range(iterations):
        full_message = full_encrypt(message.copy(), cipher)
        if verbose:
            print(f"Full Encrypted Message: {full_message}")
        full_rtt.append(send_message_to_server(full_message, mode="Full", verbose=verbose))

    avg_selective_rtt = sum(selective_rtt) / iterations
    avg_full_rtt = sum(full_rtt) / iterations

    print("\n=== Results ===")
    print(f"Average Selective RTT: {avg_selective_rtt:.6f} seconds")
    print(f"Average Full RTT: {avg_full_rtt:.6f} seconds")
    return avg_selective_rtt, avg_full_rtt

# Send message to server and measure round-trip time
def send_message_to_server(encrypted_message, mode, verbose):
    start_time = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("127.0.0.1", 65432))
        client_socket.sendall(encrypted_message.encode())
        response = client_socket.recv(1024)  # Wait for server response
    end_time = time.time()
    if verbose:
        print(f"Server Response ({mode}): {response.decode()}")
    return end_time - start_time

# Measure encryption performance
def measure_encryption_performance(iterations=10):
    print(f"\nMeasuring Encryption Performance over {iterations} iterations...")
    selective_times = []
    full_times = []

    for _ in range(iterations):
        # Measure selective encryption time
        start = time.time()
        selective_encrypt(message.copy(), cipher)
        selective_times.append(time.time() - start)

        # Measure full encryption time
        start = time.time()
        full_encrypt(message.copy(), cipher)
        full_times.append(time.time() - start)

    avg_selective_time = sum(selective_times) / iterations
    avg_full_time = sum(full_times) / iterations

    selective_size = len(json.dumps(selective_encrypt(message.copy(), cipher)).encode())
    full_size = len(full_encrypt(message.copy(), cipher).encode())

    print(f"Average Selective Encryption Time: {avg_selective_time:.6f} seconds")
    print(f"Average Full Encryption Time: {avg_full_time:.6f} seconds")
    print(f"Selective Encryption Payload Size: {selective_size} bytes")
    print(f"Full Encryption Payload Size: {full_size} bytes")

    return avg_selective_time, avg_full_time, selective_size, full_size

# ASCII bar chart
def print_text_bar_chart(metric_name, selective_value, full_value, unit=""):
    max_bar_length = 50
    if abs(selective_value - full_value) < 1e-9:
        selective_bar = full_bar = max_bar_length
    else:
        selective_bar = round((selective_value / max(selective_value, full_value)) * max_bar_length)
        full_bar = round((full_value / max(selective_value, full_value)) * max_bar_length)

    print(f"\n{metric_name}:")
    print(f"Selective: {'#' * selective_bar} {selective_value:.6f}{unit}")
    print(f"Full     : {'#' * full_bar} {full_value:.6f}{unit}")

if __name__ == "__main__":
    # Prompt user for number of iterations and verbosity
    iterations = int(input("Enter the number of iterations for testing: "))
    verbose = input("Do you want verbose output? (yes/no): ").strip().lower() == "yes"

    # Run encryption performance tests
    encryption_metrics = measure_encryption_performance(iterations=iterations)

    # Test round-trip time
    rtt_metrics = test_client(iterations=iterations, verbose=verbose)

    # Display results in bar charts
    print_text_bar_chart("Encryption Time (seconds)", encryption_metrics[0], encryption_metrics[1], " s")
    print_text_bar_chart("Payload Size (bytes)", encryption_metrics[2], encryption_metrics[3], " bytes")
    print_text_bar_chart("Round-Trip Time (seconds)", rtt_metrics[0], rtt_metrics[1], " s")
