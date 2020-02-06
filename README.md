# Impulse BETA!
> Simple Denial-of-service ToolKit


<p align="center">
  <img src="https://i.ibb.co/rFct6QX/LOGO.png">
</p>


* Links:
  * [All methods](#methods)
  * [Installation](#installation)
  * [Example (SMS Flood)](#example-sms--call-flood)

# Main window
![MAIN-WINDOW](https://i.ibb.co/JK50vDR/MAIN.png)

# Methods:
| Method               |   Target   | Description |
| ---------------------| -----------|-------------|
| SMS                  | +PHONE     | SMS & CALL FLOOD|
| NTP                  | IP:PORT    | NTP amplification is a type of Distributed Denial of Service (DDoS) attack in which the attacker exploits publically-accessible Network Time Protocol (NTP) servers to overwhelm the targeted with User Datagram Protocol (UDP) traffic. |
| SYN                  | IP:PORT    | A SYN flood (half-open attack) is a type of denial-of-service (DDoS) attack which aims to make a server unavailable to legitimate traffic by consuming all available server resources. |
| TCP                  | IP:PORT    | What is a SYN flood attack. TCP SYN flood (a.k.a. SYN flood) is a type of Distributed Denial of Service (DDoS) attack that exploits part of the normal TCP three-way handshake to consume resources on the targeted server and render it unresponsive. |
| UDP                  | IP:PORT    | A UDP flood is a type of denial-of-service attack in which a large number of User Datagram Protocol (UDP) packets are sent to a targeted server with the aim of overwhelming that device’s ability to process and respond. The firewall protecting the targeted server can also become exhausted as a result of UDP flooding, resulting in a denial-of-service to legitimate traffic. |
| POD (Ping of Death)  | IP         | Ping of Death (a.k.a. PoD) is a type of Denial of Service (DoS) attack in which an attacker attempts to crash, destabilize, or freeze the targeted computer or service by sending malformed or oversized packets using a simple ping command. |
| HTTP                 | URL        | HTTP Flood is a type of Distributed Denial of Service (DDoS) attack in which the attacker manipulates HTTP and POST unwanted requests in order to attack a web server or application. These attacks often use interconnected computers that have been taken over with the aid of malware such as Trojan Horses. |
| Slowloris            | IP:PORT    | Slowloris is a denial-of-service attack program which allows an attacker to overwhelm a targeted server by opening and maintaining many simultaneous HTTP connections between the attacker and the target. |
| Memcached            | IP:PORT    | A memcached distributed denial-of-service (DDoS) attack is a type of cyber attack in which an attacker attempts to overload a targeted victim with internet traffic. The attacker spoofs requests to a vulnerable UDP memcached* server, which then floods a targeted victim with internet traffic, potentially overwhelming the victim’s resources. While the target’s internet infrastructure is overloaded, new requests cannot be processed and regular traffic is unable to access the internet resource, resulting in denial-of-service. |

# Installation:
* Windows:
  * Download Python 3.6 from [here](https://www.python.org/downloads/release/python-360/)
  * Launch installer, click `add python to PATH`
  * Download Impulse
  * Open cmd or powershell in Impulse directory
  * Run this command: `pip install -r requirements.txt`
  * And this: `python impulse.py --help`

* Linux/Termux:
  * `sudo apt update`
  * `sudo apt install python python-pip git -y`
  * `git clone https://github.com/LimerBoy/Impulse`
  * `cd Impulse/`
  * `pip install -r requirements.txt`
  * `python impulse.py --help`

# Example SMS & Call flood:
```python impulse.py --method SMS --target +XXXXXXXXXXXX --time 20 --threads 2```

![SMS-DDOS](https://i.ibb.co/yXSSF7R/SMS.png)
