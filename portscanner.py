import socket
from datetime import datetime

# Create a socket obj
def obj_socket(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            return True
        else:
            return False
    except socket.error:
        return False

    finally:
        s.close()

def port_scanner(target, start_port, end_port):
    print(f"\nStarting scan on targer: {target}")
    print(f"Scanning port from:{start_port} to {end_port}...\n")

    start_time = datetime.now()

    ports_opening= []
    for port in range(start_port, end_port+1):
        if obj_socket(target, port):
            print(f"\nPort {port} is opening")
            ports_opening.append(port)
        else: 
            print(f"\nPort {port} is closing")

    end_time = datetime.now()
    print(f"\nScan completed in:{end_time - start_time}")

    return ports_opening

#Usage 
if __name__ == "__main__":
    target = input("Enter the host or IP")
    start_port = int(input("Enter the starting port"))
    end_port = int(input("Enter the ending port"))

    ports_opening = port_scanner(target, start_port, end_port)
    print(f"\nOpen ports: {ports_opening}")


