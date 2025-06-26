import socket

def scan_ports(target_ip, ports=[21, 22, 23, 25, 53, 80, 110, 443, 8080]):
    open_ports = []
    print(f"[*] Scanning {target_ip}...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.5)  # Wait a bit longer for each port
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN ✅")
                open_ports.append(port)
            else:
                print(f"[-] Port {port} is CLOSED ❌")
            sock.close()
        except Exception as e:
            print(f"[!] Error on port {port}: {e}")
    return open_ports