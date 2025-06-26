import socket
import modules.port_scanner as port_scanner
import modules.brute_forcer as brute_forcer

def menu():
    while True:
        print("\n=== Penetration Testing Toolkit ===")
        print("1. Port Scanner")
        print("2. Brute Forcer (Demo)")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            ip = input("Enter target IP address: ").strip()
            try:
                socket.gethostbyname(ip)  # Check if IP/hostname is valid
                port_scanner.scan_ports(ip)
            except socket.gaierror:
                print("❌ Invalid IP address or hostname. Please try again.")

        elif choice == '2':
            username = input("Enter username to brute-force: ").strip()
            actual_password = input("Set the correct password (for demo): ").strip()
            password_list = ["admin", "1234", "password", "root", "admin123", "letmein"]
            brute_forcer.brute_force_login(username, password_list, actual_password)

        elif choice == '3':
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()