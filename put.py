import requests
import os
import signal
from colorama import Fore, Style, init

init(autoreset=True)

def signal_handler(sig, frame):
    print(Fore.YELLOW + "\n[!] Scan interrupted. Exiting...")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

open("results.txt", "w").close()
open("failed.txt", "w").close()

def check_http_put(target_url, test_filename="poc.txt", test_content="Bang Heker Hadir"):
    test_url = f"{target_url.rstrip('/')}/{test_filename}"

    try:
        response = requests.put(test_url, data=test_content, headers={"Content-Type": "text/plain"}, timeout=10)

        if response.status_code in [200, 201, 204]:
            print(Fore.GREEN + f"[+] PUT upload successful: {test_url}")

            verify_response = requests.get(test_url, timeout=10)
            if verify_response.status_code == 200 and test_content in verify_response.text:
                print(Fore.GREEN + f"[+] File successfully uploaded and accessible: {test_url}")

                with open("results.txt", "a") as result_file:
                    result_file.write(f"VULN: {test_url}\n")

                delete_response = requests.request("DELETE", test_url, timeout=10)
                if delete_response.status_code in [200, 204]:
                    print(Fore.CYAN + f"[+] Cleanup successful: {test_url} deleted.")
                else:
                    print(Fore.RED + f"[-] Failed to delete test file: {test_url}")

                return True
            else:
                print(Fore.YELLOW + f"[-] File upload succeeded, but not accessible: {test_url}")
        else:
            print(Fore.RED + "[-] PUT method seems disabled or restricted.")
            with open("failed.txt", "a") as failed_file:
                failed_file.write(f"FAILED: {target_url}\n")

    except requests.exceptions.ConnectTimeout:
        print(Fore.MAGENTA + f"[!] Connection timeout for {target_url}, skipping...")
        with open("failed.txt", "a") as failed_file:
            failed_file.write(f"ERROR: {target_url} - TIMEOUT\n")
    except requests.RequestException:
        print(Fore.RED + f"[!] Error for {target_url}, logging error...")
        with open("failed.txt", "a") as failed_file:
            failed_file.write(f"ERROR: {target_url}\n")

    return False

def scan_targets(file_path="list.txt"):
    with open(file_path, "r") as f:
        targets = [line.strip() for line in f.readlines() if line.strip()]

    for target in targets:
        if not target.startswith("http://") and not target.startswith("https://"):
            target = "https://" + target
        print(Fore.BLUE + f"[*] Scanning {target}")
        check_http_put(target)

# Run the scan
scan_targets()
