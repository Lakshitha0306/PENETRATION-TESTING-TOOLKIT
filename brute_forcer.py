def brute_force_login(username, password_list, actual_password):
    print(f"[*] Starting brute-force on user: {username}")
    for pwd in password_list:
        print(f"Trying password: {pwd}")
        if pwd == actual_password:
            print(f"[+] Success! Password found: {pwd}")
            return pwd
    print("[-] Failed to find the password.")
    return None