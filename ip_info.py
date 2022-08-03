from requests import get
import requests
import test_art
import socket
from socket import gethostname

def get_public_ip():
    try:
        ip = get('https://api.ipify.org').content.decode('utf8')
        return ip
    except requests.exceptions.ConnectionError:
        return "[-] Please, check your Internet connection."

def get_local_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

def get_info_by_ip(ip = get_public_ip()):
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        return response

def is_ip(ip):
   try:
       parts = ip.split('.')
       return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
   except ValueError:
       return False # one of the 'parts' not convertible to integer
   except (AttributeError, TypeError):
       return False # `ip` isn't even a string


def return_info(public_ip = get_public_ip()):
            country = get_info_by_ip(ip = public_ip)['country']
            region = get_info_by_ip(ip = public_ip)['regionName']
            city = get_info_by_ip(ip = public_ip)['city']
            isp = get_info_by_ip(ip = public_ip)['isp']
            print("\n" + f"Your IP-address: {public_ip}")
            print(f"Your country: {country}")
            print(f"Your region: {region}")
            print(f"Your city: {city}")
            print(f"Your ISP: {isp}", "\n")

def main():
    test_art.arted()
    print("\n", "\n")
    var = True
    while var:
        request = input("ip_info > ")
        if request == "public_ip":
            print(f"Your public IP-address is {get_public_ip()}", "\n")         #get public my ip
            continue
        if request == "local_ip":
            print(f"Your local IP-address is {get_local_ip()}", "\n")           #get local my ip
            continue
        if request == "get_info":
            try:
                IP = input("Please, enter IP-address to get information or press Enter: ")
                if IP == "":
                    return_info()
                    continue
                if is_ip(IP):
                    return_info(IP)
                    continue
                else:
                    print("[!] Not valid IP-address")
                    continue
            except requests.exceptions.ConnectionError:
                print("[!] Please check your connection!")
                continue
        if request == "exit":
            print(f"Bye, {socket.gethostname()}")
            var = False

        else:
            print("""
            NAME
            
                ip_info - IP exploration tool
                
            COMMANDS
            
                public_ip - return your public IP
                local_ip - return your local IP 
                get_info - return info about entered IP (by default your public IP)
             """)
            continue

if __name__ == '__main__':
    main()
