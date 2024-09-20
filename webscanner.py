#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coded by      @charliecpln
# Discord:      @charliecpln
# Telegram:     @charliecpln
# Github:       @charliecpln

import os
import time
from sys import exit

try:
    def sil():
        name = os.name
        if name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    sil()

    def installation():
        try:
            print("Libraries checking...")
            from colorama import Fore, Back, Style, init
            import requests
            import webbrowser
            sil()
        
        except ImportError:
            print("Libraries are auto dowloading...")
            os.system("pip install colorama requests webbrowser")
            sil()
    installation()

    from colorama import Fore, Back, Style, init
    import requests
    import webbrowser

    init(autoreset=True)

    banner = Fore.LIGHTRED_EX + Style.BRIGHT + """
 _       ____________     _____ _________    _   ___   ____________ 
| |     / / ____/ __ )   / ___// ____/   |  / | / / | / / ____/ __ \'
| | /| / / __/ / __  |   \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
| |/ |/ / /___/ /_/ /   ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/ 
|__/|__/_____/_____/   /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|  
                   [github.com/charliecpln]             @charliecpln
"""

    def connectiontest():
        #CONNECTION TEST
        print(Fore.LIGHTMAGENTA_EX + "Trying to connection github.com for connection test...")
        response = requests.get("https://www.github.com")
        if response.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "[+] Connection test successful")

        else:
            print(Fore.LIGHTRED_EX + "[-] Connection test not successful!")
            input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to exit...\n")
            exit()

    connectiontest()


    def sqlscanner():
        print(banner)
        payloadlar = ["'", '"', "1 OR 1=1", "' OR '1'='1"]
        print(Back.LIGHTRED_EX + "[!] Leave blank if you don't have any payloads file\n")
        
        payload_dosyasi = input(Fore.LIGHTCYAN_EX + Style.DIM + "[*] Please enter path of payloads: ")
        targeturl = input(Fore.LIGHTCYAN_EX + Style.DIM + "[?] Please enter target url: ")

        if not targeturl.startswith("http"):
            if targeturl.startswith("www."):
                targeturl = "https://" + targeturl
            else:
                targeturl = "https://www." + targeturl

        if payload_dosyasi == "":
            payloadlar = payloadlar
        else:
            try:
                with open(payload_dosyasi, "r") as payload_dosyasi:
                    payloadlar = payload_dosyasi.readlines()
            except FileNotFoundError:
                print(Fore.LIGHTRED_EX + "[!] Payload file not found.")
                input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to exit...\n")
                return
            
        vulnerability_found = False

        for payload in payloadlar:
            payload = payload.strip()
            try:
                response = requests.get(f"{targeturl}{payload}")
            except requests.RequestException as e:
                print(Fore.LIGHTRED_EX + f"[!] Error: {e}")
                input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to exit...\n")
                return

            if "sql" in response.text.lower():
                print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"\n\n[+] SQL Injection vulnerability detected:\nUrl: {targeturl}\nPayload: {payload}\n")
                with open("sqlscanner.txt", "a", encoding="utf-8") as dosya:
                    dosya.write(f"Url: {targeturl}, Payload: {payload}\n")
                webbrowser.open(f"{targeturl}")
                vulnerability_found = True

                input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to continue...\n")
                main()

            if not vulnerability_found:
                print(Style.BRIGHT + Fore.LIGHTRED_EX + "[!] No SQL Injection vulnerabilities found.")
                input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to continue...\n")
                main()

    def xssscanner():
        print(banner)
        default_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg><script>alert('XSS')</script></svg>",
            "<body onload=alert('XSS')>",
            "<iframe src='javascript:alert(\"XSS\")'></iframe>"
        ]
        
        print(Back.LIGHTRED_EX + "[!] Leave blank if you want to use default payloads\n")
        payload_dosyasi = input(Fore.LIGHTCYAN_EX + Style.DIM + "[*] Please enter path of payloads: ")
        
        targeturl = input(Fore.LIGHTCYAN_EX + Style.DIM + "[?] Please enter target url: ")
        
        if not targeturl.startswith("http"):
            if targeturl.startswith("www."):
                targeturl = "https://" + targeturl
            else:
                targeturl = "https://www." + targeturl

        if payload_dosyasi == "":
            payloadlar = default_payloads
        else:
            try:
                with open(payload_dosyasi, "r") as payload_dosyasi:
                    payloadlar = payload_dosyasi.readlines()
                    payloadlar = [payload.strip() for payload in payloadlar]
            except FileNotFoundError:
                print(Fore.LIGHTRED_EX + "[!] Payload file not found.")
                input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to exit...\n")
                return
            
        vulnerability_found = False

        for payload in payloadlar:
            try:
                response = requests.get(f"{targeturl}{payload}")
            except requests.RequestException as e:
                print(Fore.LIGHTRED_EX + f"[!] Error: {e}")
                input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to exit...\n")
                return

            if payload in response.text:
                print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"\n\n[+] XSS vulnerability detected:\nUrl: {targeturl}\nPayload: {payload}\n")
                with open("xssscanner.txt", "a", encoding="utf-8") as dosya:
                    dosya.write(f"Url: {targeturl}, Payload: {payload}\n")
                webbrowser.open(f"{targeturl}")
                vulnerability_found = True

                input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to continue...\n")
                main()

        if not vulnerability_found:
            print(Fore.LIGHTRED_EX + "[!] No XSS vulnerabilities found.")
            input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to continue...\n")
            main()
    
    def adminpanelfinder():
        print(banner)
        time.sleep(1)
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "[!] WARNING\nIf you want use Admin Panel Finder you must download it on github!")
        time.sleep(3.2)
        webbrowser.open("https://github.com/charliecpln/adminpanelfinder")
        input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to continue...\n")
        main()

    def contact():
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + """
This script was writed by @charliecpln👻

    Contact:
          [Discord]  -  @charliecpln
          [Telegram] -  @charliecpln
""")
        time.sleep(2.7)
        input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to continue...\n")
        main()

    def main():
        sil()
        print(banner)

        menu = Style.BRIGHT + Fore.LIGHTCYAN_EX + """
    [1] - Sql Scanner
    [2] - Xss Scanner
    [3] - Admin Panel Finder
    [4] - Contact
    [Q] - Exit
    
    """
        print(menu)
        sec = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Please enter your choice: ")

        if sec == "1":
            sil()
            sqlscanner()

        elif sec == "2":
            sil()
            xssscanner()

        elif sec == "3":
            sil()
            adminpanelfinder()

        elif sec == "4":
            sil()
            contact()

        elif sec.lower() == "q" or sec == "5":
            sil()
            exit()

        else:
            sil()
            main()

    #GET STARTED
    main()

except Exception as error:
    input(f"Error: {error}\nPress 'enter' to exit...\n")
    exit()
