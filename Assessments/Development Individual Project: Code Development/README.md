
# Encryption Performance Analysis and RTT Discrepancy Investigation

This project evaluates the performance of Selective Encryption and Full Encryption schemes by measuring their encryption times, payload sizes, and Round-Trip Times (RTTs) over various iteration counts. It highlights the impact of encryption methods and test configurations on RTT discrepancies, offering insights into their performance and security implications (ScienceDirect, 2018).

For further context on the system modeled in this project, refer to the original design document: [Development Team Project: Design Document](https://gist.github.com/stadia-scoring/35a7b5ed853ce4ca49db343518a46ac4). This document provides a comprehensive overview of the smart home network system, its functionalities, and the potential security vulnerabilities it addresses.


 A [Video Walkthrough](https://risjo-my.sharepoint.com/:v:/p/mauricio/EURmNn01uE1GvUN5l4a977EBdxTTaGwtU4IgqyRiE1AHvQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=WdXYaE) of the model is availble to view online.

This project is availabe as a Gist: [https://gist.github.com/stadia-scoring/1972642d75f72395381a7737e6f1dbc6](https://gist.github.com/stadia-scoring/1972642d75f72395381a7737e6f1dbc6)

## Table of Contents

- [Introduction](#introduction)
- [Hypothesis](#hypothesis)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [Output Example](#output-example)
- [Testing and Analysis](#testing-and-analysis)
- [Conclusion](#conclusion)
- [References](#references)

---

## Introduction

Encryption performance is a critical consideration in smart home communication systems, where security, efficiency, and system responsiveness must balance against constrained computational resources (Cisco Press, 2021). Variations in encryption methods, payload sizes, and system/network constraints significantly influence performance metrics such as encryption time and RTT.

This project examines the relative performance of Selective Encryption and Full Encryption under varying iteration counts. By analyzing encryption times, payload sizes, and RTTs, we aim to evaluate the practical trade-offs of each method in securing smart home systems while maintaining operational efficiency.

This comparative analysis reveals the performance-to-security trade-offs of each approach and their suitability for different use cases, such as residential versus industrial applications (MDPI, 2018).

---

## Hypothesis

The hypothesis driving this investigation is as follows:

> **“Selective encryption of sensitive voice command data in a smart home communication system improves performance without compromising the confidentiality of critical information.”**

This hypothesis assumes that encrypting only sensitive fields can achieve a better balance between performance (e.g., faster encryption times, reduced payload sizes) and security compared to encrypting the entire payload. We examine how these trade-offs impact critical performance metrics like RTT and encryption time (IEEE Xplore, 2018).

### ABCDE Characteristics Addressed

- **A: Availability** — RTT directly impacts system availability, determining how quickly messages are transmitted and responses are received.
- **B: Behavior** — The chosen encryption method influences system behavior, with Selective Encryption likely enabling faster responses due to smaller encrypted payloads.
- **C: Confidentiality** — Both methods aim to secure sensitive data while differing in their approach to protecting metadata.
- **D: Dependability** — Encryption and transmission times affect the reliability of real-time or high-throughput environments.
- **E: Efficiency** — Metrics such as encryption time, payload size, and RTT provide insight into the system’s efficiency in handling encrypted data.

---

## Model

### System Overview

The modeled system is a smart home communication network designed to transmit voice commands securely between client devices (e.g., voice assistants) and a central server. The system emphasizes security and efficiency, addressing potential vulnerabilities in sensitive data transmission through encryption.

### Encryption Schemes

The system implements two encryption schemes for securing transmitted data:

- **Selective Encryption**: Encrypts only critical fields (e.g., `device_id` and `command`) in the message payload while leaving non-sensitive metadata accessible.
- **Full Encryption**: Encrypts the entire message payload, ensuring comprehensive data protection.


### Message Structure

The input data for both encryption schemes is a JSON message with the following structure:

- **Device ID**: Identifies the source device.
- **Command**: Represents the action to be performed.
- **Metadata**: Provides additional information, such as a timestamp.

In Selective Encryption, only `device_id` and `command` are encrypted, while `metadata` remains accessible. In Full Encryption, the entire message is encrypted.

### Key Management

The encryption and decryption processes rely on a shared symmetric key generated by the server. The key is stored locally in the file system (`key.key`) and loaded at runtime. For testing purposes, the server automatically generates the key when started.

### Data Flow

The system follows this workflow for encryption and transmission:

1. **Encryption**:
   - The client encrypts messages using either selective or full encryption.
   - Encrypted messages are transmitted to the server.
2. **Decryption**:
   - The server decrypts received messages based on their format (selective or full).
   - If selective encryption is used, the server decrypts only the sensitive fields and merges them with the unencrypted metadata.
3. **Performance Measurement**:
   - The client measures encryption time, payload size, and RTT for each encryption scheme.

## Installation and Usage

#### **Prerequisites**
Ensure that Python 3.8 or higher is installed on your system. If not, follow these steps:

For macOS:
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Install Python using Homebrew
brew install python
```
For Windows:
```bash
# Check for Python installation
python --version
# If not installed, download from the official Python website
# https://www.python.org/downloads/
```
---

#### **Set Up a Virtual Environment**
Using a virtual environment ensures that project dependencies do not interfere with your system's global Python environment.

Activate the virtual environment:
```bash
# macOS/Linux:
source SSA_PCOM7E_OCT_2004/bin/activate
# Windows:
SSA_PCOM7E_OCT_2004\Scripts\activate
```
---

#### **Install Project Dependencies**

```bash
# Install the required dependencies
pip install cryptography
```
---

### **Usage**

#### **Run the Server**
The server (`server.py`) initializes the encryption key and handles decryption of messages from the client. Always start the server before running the client.

```bash
python server.py  
```
The server will start listening on `127.0.0.1:65432`.

---

#### **Run the Client**
The client (`client.py`) encrypts messages using both selective and full encryption schemes, sends them to the server, and measures performance metrics.

```bash
python client.py  
```
**Client Prompts**:  
1. **Enter the number of iterations for testing**: Specify the number of iterations to test encryption performance. For example, `100`, `5000`, or `10000`.  
2. **Do you want verbose output? (yes/no)**:  
   - Enter `yes` to see detailed encryption and server response information.  
   - Enter `no` to see only summarized results.
---

#### **Deactivate the Virtual Environment**
After completing your tests, deactivate the virtual environment to return to your system's global Python environment.
```bash
deactivate
```
## Output Example

Below is an examples of the program's output for different iteration counts, demonstrating the performance of Selective Encryption and Full Encryption. 

---

### **Non-Verbose Output Example (10 Iterations)**

```plaintext
Enter the number of iterations for testing: 10
Do you want verbose output? (yes/no): no

=== Results ===
Average Selective RTT: 0.000774 seconds
Average Full RTT: 0.000350 seconds

Encryption Time (seconds):
Selective: ################################################## 0.000620 s
Full     : ####### 0.000089 s

Payload Size (bytes):
Selective: ################################################## 284.000000 bytes
Full     : ######################################## 228.000000 bytes

Round-Trip Time (seconds):
Selective: ################################################## 0.000774 s
Full     : ####################### 0.000350 s
```

### **Testing and Analysis**

#### **Overview**
This section analyzes the performance of Selective Encryption and Full Encryption schemes using metrics such as encryption time, payload size, and Round-Trip Time (RTT). Tests were conducted under varying iteration counts (1, 5, 10, 1000, 5000, 10000, and 50000) to simulate different smart home communication scenarios MDPI (2018).

---

#### **1. Encryption Time Analysis**
- **Selective Encryption**: Encrypts only sensitive fields, adding fixed overhead due to partial encryption processing.
- **Full Encryption**: Encrypts the entire payload, achieving faster performance due to simplicity.

##### **Key Observations**
| Iteration Count | Selective Encryption Time (s) | Full Encryption Time (s) | Performance Gap (Times Slower) |
|------------------|-------------------------------|---------------------------|--------------------------------|
| 1                | 0.006685                      | 0.000559                  | ~12x                           |
| 5                | 0.001568                      | 0.000072                  | ~22x                           |
| 10               | 0.000620                      | 0.000089                  | ~7x                            |
| 1000             | 0.000029                      | 0.000022                  | ~1.3x                          |
| 5000             | 0.000015                      | 0.000012                  | ~1.25x                         |
| 10000            | 0.000013                      | 0.000011                  | ~1.18x                         |
| 50000            | 0.000011                      | 0.000010                  | ~1.10x                         |

**Implications**:
- At lower iteration counts (e.g., 1, 5, 10), Selective Encryption is significantly slower due to fixed processing overhead.
- As the iteration count increases, the performance gap narrows, with both schemes showing comparable times for high iteration counts (e.g., 50000).

---

#### **2. Payload Size Comparison**
The payload size directly affects the amount of data transmitted over the network (Cisco Press, 2021). Selective Encryption increases payload size due to added metadata, while Full Encryption minimizes size by avoiding extra metadata fields (IBM Developer, 2020).

| Encryption Scheme   | Payload Size (bytes) |
|----------------------|----------------------|
| Selective Encryption | 284                  |
| Full Encryption      | 228                  |

**Implications**:
- Selective Encryption incurs a larger payload size due to the added metadata for partial encryption, increasing transmission costs.
- This fixed difference has a proportionally larger impact at lower iteration counts.

---

#### **3. Round-Trip Time (RTT) Analysis**
RTT measures the total time taken to send a message to the server and receive a response (ScienceDirect, 2018). Factors such as payload size, network variability, and encryption method significantly influence RTT performance (MDPI, 2018).

##### **Key Observations**
| Iteration Count | Selective RTT (s) | Full RTT (s) | Performance Gap (Times Slower) |
|------------------|-------------------|--------------|--------------------------------|
| 1                | 0.000842          | 0.000861     | N/A (network variability)      |
| 5                | 0.000980          | 0.000533     | ~1.8x                          |
| 10               | 0.000774          | 0.000350     | ~2.2x                          |
| 1000             | 0.000076          | 0.000063     | ~1.2x                          |
| 5000             | 0.000066          | 0.000064     | ~1.03x                         |
| 10000            | 0.001171          | 0.002029     | ~0.58x (Selective faster)      |
| 50000            | 0.002173          | 0.002175     | ~1x                            |

**Implications**:
- At lower iteration counts (e.g., 1, 5, 10), Full Encryption consistently outperforms Selective Encryption due to its smaller payload size and lower processing overhead.
- At higher iteration counts, network variability and the diminishing relative impact of payload size and encryption time narrow the performance gap.
- Interestingly, at 10000 iterations, Selective Encryption achieves faster RTT due to reduced processing variance in metadata handling.

---

#### **5. Deployment Recommendations**
- **Residential Use**: Full Encryption is recommended for smart homes due to its simplicity, faster performance at low iteration counts, and negligible RTT.
- **Industrial Use**: Selective Encryption may be more suitable in industrial scenarios requiring metadata accessibility or granular control over sensitive data, despite its higher processing overhead at low iteration counts.

---

### **Conclusion**

This project evaluated the performance of Selective and Full Encryption schemes within a smart home communication system. Key findings include:

1. **Performance Trade-offs**: Full Encryption consistently outperforms Selective Encryption at low iteration counts. However, Selective Encryption becomes competitive at high iteration counts where fixed processing overhead diminishes.
2. **Payload Size Impact**: Selective Encryption's larger payload size incurs higher transmission costs, particularly impactful at lower iteration counts.
3. **Operational Context**: Full Encryption is optimal for typical smart home scenarios with low concurrency, whereas Selective Encryption is better suited for high-throughput or metadata-sensitive environments like industrial applications.

## References

1. Cisco Press (2021) *Communication Protocols for IoT*. Available at: [https://www.ciscopress.com/articles/article.asp?p=2923211&seqNum=6](https://www.ciscopress.com/articles/article.asp?p=2923211&seqNum=6) (Accessed: 29 November 2024).

2. Schneier, B. (1999) *Attack Trees*. Available at: [https://www.schneier.com/academic/archives/1999/12/attack_trees.html](https://www.schneier.com/academic/archives/1999/12/attack_trees.html) (Accessed: 27 November 2024).

3. IBM Developer (2020) *Top 10 IoT Security Challenges*. Available at: [https://developer.ibm.com/articles/iot-lp101-connectivity-network-protocols/](https://developer.ibm.com/articles/iot-lp101-connectivity-network-protocols/) (Accessed: 30 November 2024).

4. Docker Inc. (2021) *Containerized Python Development – Part 1*. Available at: [https://www.docker.com/blog/containerized-python-development-part-1/](https://www.docker.com/blog/containerized-python-development-part-1/) (Accessed: 28 November 2024).

5. MDPI (2018) *Security of IoT Application Layer Protocols: Challenges and Findings*. *Future Internet*, 12(3), p.55. Available at: [https://www.mdpi.com/2411-9660/3/3/32](https://www.mdpi.com/2411-9660/3/3/32) (Accessed: 26 November 2024).

6. IEEE Xplore (2018) *IoT Based Smart Security and Home Automation System*. Available at: [https://ieeexplore.ieee.org/document/7813916](https://ieeexplore.ieee.org/document/7813916) (Accessed: 28 November 2024).

7. IEEE Xplore (2017) *Smart Vehicles with Everything*. Available at: [https://ieeexplore.ieee.org/document/7917997](https://ieeexplore.ieee.org/document/7917997) (Accessed: 27 November 2024).

8. ScienceDirect (2018) *A Review of Smart Cities Based on the Internet of Things Concept*. *Journal of Cleaner Production*. Available at: [https://www-sciencedirect-com.uniessexlib.idm.oclc.org/science/article/pii/S0959652618339775?via%3Dihub](https://www-sciencedirect-com.uniessexlib.idm.oclc.org/science/article/pii/S0959652618339775?via%3Dihub) (Accessed: 29 November 2024).
