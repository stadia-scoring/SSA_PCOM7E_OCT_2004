## Activity: Socket Programming

### Step 1: Create the Echo Server

1. **Copy the following code into a file named `echo-server.py`:**

    ```python
    #!/usr/bin/env python3
    import socket

    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
    ```

### Step 2: Create the Echo Client

2. **Copy the following code into a file named `echo-client.py`:**

    ```python
    #!/usr/bin/env python3
    import socket

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))
    ```

### Step 3: Start the Server

3. **Open a terminal and start the server by running the following command:**

    ```bash
    python3 echo-server.py
    ```

### Step 4: Start the Client

4. **Open a second terminal and start the client by running the following command:**

    ```bash
    python3 echo-client.py
    ```

### Step 5: Interaction

The client and server will now communicate with one another.

<img width="904" alt="port used by the server" src="https://github.com/user-attachments/assets/36b10e10-9120-421d-bbe7-6eec1a31f594">
---

### Question 1

**In relation to `echo-server.py`, what is achieved using the command:**

```python
s.bind((HOST, PORT))
```

**Answer:**

The command `s.bind((HOST, PORT))` is used to associate the socket `s` with a specific network interface and port number. In this case, it binds the socket to the loopback address (127.0.0.1), allowing the server to accept connections from clients on the same machine. The `PORT` variable (65432) specifies the port number on which the server will listen for incoming connections. This is a necessary step before calling `s.listen()` to enable the server to accept client connections.

---

### Question 2

**In relation to `echo-client.py`, what is achieved using the command:**

```python
s.connect((HOST, PORT))
```

**Answer:**

The command `s.connect((HOST, PORT))` is used to establish a connection from the client socket `s` to the server socket that is listening on the specified `HOST` (loopback address 127.0.0.1) and `PORT` (65432). By executing this command, the client attempts to connect to the server, enabling two-way communication between the client and server once the connection is successfully established. If the server is running and listening on the specified port, the client will be able to send data to the server and receive responses.
