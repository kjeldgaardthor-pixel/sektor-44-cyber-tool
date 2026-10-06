import os
import time
import hashlib
import sys

def show_banner():
    print("=" * 65)
    print("  S E K T O R  4 4  -  C Y B E R  S E C U R I T Y  T O O L  v 1 . 0")
    print("  Made by Sektor 44")
    print("=" * 65)

def calculate_file_hash():
    print("\n[ * ] File Integrity & Hash Scanner")
    file_path = input("Enter the full path of the file to scan: ").strip()
    
    # Fjerner eventuelle anføringstegn, hvis brugeren har træk-og-sluppet filen
    file_path = file_path.strip('"').strip("'")
    
    if not os.path.exists(file_path):
        print(f"[ ! ] Error: File not found at '{file_path}'\n")
        input("Press Enter to return to the main menu...")
        return

    print("[*] Calculating SHA-256 cryptographic hash...")
    time.sleep(1)
    
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        file_hash = sha256_hash.hexdigest()
        print(f"\n[ + ] Target File: {os.path.basename(file_path)}")
        print(f"[ + ] SHA-256 Hash: {file_hash}")
        print("[ + ] Status: Integrity verified. Ready for GitHub deployment.\n")
        
    except Exception as e:
        print(f"[ ! ] An error occurred while reading the file: {e}\n")
        
    input("Press Enter to return to the main menu...")

def main():
    while True:
        show_banner()
        print("\n[ MAIN MENU - SEKTOR 44 ]")
        print("  [1] Calculate File SHA-256 Hash (Real Integrity Check)")
        print("  [2] View System Logs & Status")
        print("  [3] Encrypt File (Locked - Coming in v2.0)")
        print("  [4] Decrypt File (Locked - Coming in v2.0)")
        print("  [5] Exit Program")
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == '1':
            calculate_file_hash()
            
        elif choice == '2':
            print("\n--- Sektor 44 System Log ---")
            print(f"Tool Name: Sektor 44 Cyber Tool")
            print(f"Version: 1.0")
            print(f"Developer: Sektor 44")
            print(f"Core Status: Operational\n")
            input("Press Enter to return to the main menu...")
            
        elif choice == '3':
            print("\n[ ! ] NOTICE: File encryption is locked to Version 2.0.")
            print("[ ! ] Scheduled for future releases (Coming Soon).\n")
            time.sleep(1.5)
            
        elif choice == '4':
            print("\n[ ! ] NOTICE: File decryption is locked to Version 2.0.")
            print("[ ! ] Scheduled for future releases (Coming Soon).\n")
            time.sleep(1.5)
            
        elif choice == '5':
            print("\nShutting down Sektor 44 Tool... Goodbye!")
            time.sleep(1)
            sys.exit()
        else:
            print("\n[ ! ] Invalid choice! Please select a number between 1 and 5.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()