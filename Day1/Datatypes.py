# Strings (str)  Used for paths, messages and to config names.abs

server_name = "prod-server-01"
print(server_name)


# Interger(int)  Used for port numbers, count instances and thresholds etc
 
port = 9000
max_retries =5
print(port*max_retries)

# Float Used for CPU, Memory, Response time 

cpu_usage=72.45
memory_gb =3.8
print(f"cpu uage:{cpu_usage}%")

# Booleans Used for toogling features and checking service states

service_running = True
if service_running:
    print("service is UP!!")

# Lists Ordered, Mutable collection  batch of IP'S, commands & filenames 

ip_list = ["192.178.1.9", "192.174.2.23", "192.123.4.35"]
commands = ["ls", "pwd", "df -h", "uptime"]
print(commands[3])

# Tuple Ordered, Immutable collection Used for Fixed credentials

credentials = ("admin", "pass123")
print(credentials[1])


# SET (unordered,unique elements) removes dupicate hosts or tasks 
unique_ids = set(["10.0.0.1", "10.2.0.0", "10.0.0.1"])
print(unique_ids)