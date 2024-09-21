#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coded by      @charliecpln
# Discord:      @charliecpln
# Telegram:     @charliecpln
# Github:       @charliecpln

import os
import time
from sys import exit
import socket
from datetime import datetime

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
                   [github.com/charliecpln]            @charliecpln👻
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
            "'><img src=x onerror=alert(1)>"
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
                response = requests.get(f"{targeturl}?input={payload}")
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
    
    def porttarayici():
        print(banner)
        openports = []
        ipadres = input(Fore.LIGHTCYAN_EX + Style.DIM + "[*] Target IP address: ")
        baslangicport = int(input(Fore.LIGHTCYAN_EX + Style.DIM + "[?] Start port no: "))
        bitisport = int(input(Fore.LIGHTCYAN_EX + Style.DIM + "[?] End port no: "))
        sil()
        print(banner)

        print(Fore.LIGHTYELLOW_EX + f"\n\nTarget IP: {ipadres}\nPort: {baslangicport} - {bitisport}\n\n")

        baslangiczamani = datetime.now()

        for port in range(baslangicport, bitisport + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ipadres, port))

            if result == 0:
                print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"[+] Open port: {port}")
                openports.append(port)
            else:
                print(Style.DIM + Fore.LIGHTRED_EX + f"[-] Closed port: {port}")
            sock.close()

        bitiszamani = datetime.now()
        kalanzaman = bitiszamani - baslangiczamani

        #ÖZET
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f"\n\nTarget IP: {ipadres}\nPort: {baslangicport} - {bitisport}")

        if not openports:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + f"Open ports: No open ports")
        else:
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"Open ports: {openports}")

        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"Scanned in {kalanzaman.seconds // 60} minutes {kalanzaman.seconds % 60} seconds\n")

        time.sleep(1)
        input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to continue...\n")
        main()

    def dizintarama():  # directory scanner
        print(banner)
        directorys = []
        targeturl = input(Fore.LIGHTCYAN_EX + Style.DIM + "[*] Target URL: ")
        wordlist_file = input(Fore.LIGHTCYAN_EX + Style.DIM + "[?] Path of wordlist: ")

        if not targeturl.startswith("http"):
            if targeturl.startswith("www."):
                targeturl = "https://" + targeturl
            else:
                targeturl = "https://www." + targeturl

        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f"\n[?] Trying connecting to {targeturl}")
        
        try:
            requests.get(targeturl)
            print(Style.BRIGHT + Fore.GREEN + "[+] Connection successful")
        except Exception as e:
            print(Style.BRIGHT + Fore.LIGHTRED_EX + f"Connection error!\n")
            input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to continue...\n")
            main()

        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + f"\n[?] Editing {wordlist_file}")

        try:
            with open(wordlist_file, "r+") as f:
                word = f.readlines()
                f.seek(0)
                f.truncate()

                for w in word:
                    w = w.strip()
                    if not w.startswith("/"):
                        f.write("/" + w + "\n")
                    else:
                        f.write(w + "\n")
            print(Style.BRIGHT + Fore.GREEN + "[+] Editing successful")

        except FileNotFoundError:
            print(Fore.LIGHTRED_EX + Style.BRIGHT + "\n[!] File not found!")
            input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to continue...\n")
            main()
        
        with open(wordlist_file, "r") as f:
            wordlist = f.readlines()

        baslangiczamani = datetime.now()

        print(Style.BRIGHT + Fore.LIGHTBLUE_EX + f"[*] Starting scan...\n")

        foundeddirectory = 0
        notfoundeddirectory = 0
        totaldirectory = 0

        for w in wordlist:
            w = w.strip()
            fullurl = f"{targeturl}{w}"
            response = requests.get(fullurl)
            if response.status_code == 200:
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"[+] Directory found: {fullurl}")
                directorys.append(fullurl)
                foundeddirectory += 1
                totaldirectory += 1
                with open("directorys.txt", "a", encoding="utf-8") as dosya:
                    dosya.write(f"{fullurl}\n")
            else:
                print(Fore.LIGHTRED_EX + Style.BRIGHT + f"[-] Directory not found: {fullurl}")
                notfoundeddirectory += 1
                totaldirectory += 1

        bitiszamani = datetime.now()
        kalanzaman = bitiszamani - baslangiczamani

        # ÖZET
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX  + f"\n            [RESULTS]           ")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + f"\nTarget url: {targeturl}\nWordlist: {wordlist_file}")
        if not directorys:
            print(Style.DIM + Fore.LIGHTRED_EX + f"Directorys: Can't found any directorys")
        else:
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + f"Founded: {foundeddirectory}\nNot founded: {notfoundeddirectory}\nTotal: {totaldirectory}")
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f"Scanned in {kalanzaman.seconds // 60} minutes {kalanzaman.seconds % 60} seconds\n")
        
        input(Fore.LIGHTMAGENTA_EX + "Press 'enter' to continue...\n")
        main()

    def adminpanelfinder():
        print(banner)
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "[!] WARNING\nIf you want use Admin Panel Finder you must download it on github!")
        time.sleep(1)
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
    [3] - Port Scanner
    [4] - Directory Scanner
    [5] - Admin Panel Finder
    
    [6] - Contact
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
            porttarayici()

        elif sec == "4":
            sil()
            dizintarama()

        elif sec == "5":
            sil()
            adminpanelfinder()

        elif sec == "6" or sec.lower() == "c":
            sil()
            contact()

        elif sec.lower() == "q" or sec == "7" or sec == "0" or sec == "10":
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
