import socket
from colorama import Fore

red = Fore.RED
green = Fore.GREEN
blue = Fore.LIGHTBLUE_EX
yellow = Fore.YELLOW
white = Fore.WHITE
reset = Fore.RED

def portscanner(target, startport, endport, whitelist=[]):
    print(f'Starting port scan on target {target}')

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting.")
        return

    try:
        for port in range(startport, endport + 1):
            if port not in whitelist:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    print(f"Port {port}: Open")
                sock.close()
    except KeyboardInterrupt:
        print("Keyboard Interrupt detected. Exiting.")
        return
    except socket.error:
        print("Socket error occurred. Exiting.")
        return

def scan_ip_range(start_ip, end_ip, start_port, end_port, whitelist=[]):
    start_ip_parts = start_ip.split('.')
    end_ip_parts = end_ip.split('.')

    for a in range(int(start_ip_parts[0]), int(end_ip_parts[0]) + 1):
        for b in range(int(start_ip_parts[1]), int(end_ip_parts[1]) + 1):
            for c in range(int(start_ip_parts[2]), int(end_ip_parts[2]) + 1):
                for d in range(int(start_ip_parts[3]), int(end_ip_parts[3]) + 1):
                    ip = f"{a}.{b}.{c}.{d}"
                    portscanner(ip, start_port, end_port, whitelist)

def main():
    print(f'''{red}
          
██████╗ ██╗     ██╗███╗   ██╗██████╗ ███████╗██╗   ██╗███████╗
██╔══██╗██║     ██║████╗  ██║██╔══██╗██╔════╝╚██╗ ██╔╝██╔════╝
██████╔╝██║     ██║██╔██╗ ██║██║  ██║█████╗   ╚████╔╝ █████╗  
██╔══██╗██║     ██║██║╚██╗██║██║  ██║██╔══╝    ╚██╔╝  ██╔══╝  
██████╔╝███████╗██║██║ ╚████║██████╔╝███████╗   ██║   ███████╗
╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝   ╚═╝   ╚══════╝                
                                              {yellow}GitHub: @hoaxter
                                              MadeBy: Nitin Sikarwar''')
    target_type = input(f"\n{reset}{green}Enter '1' for single IP or '2' for IP range: ")

    if target_type == '1':
        target = input("Enter the target host/IP address: ")
    elif target_type == '2':
        start_ip = input("Enter the starting IP address: ")
        end_ip = input("Enter the ending IP address: ")
    else:
        print("Invalid choice.")
        return

    startport = int(input("Enter the start port: "))
    endport = int(input("Enter the end port: "))

    whitelist = input("Enter ports to whitelist (comma-separated, if any): ")
    whitelist = [int(port.strip()) for port in whitelist.split(',') if port.strip().isdigit()]

    if target_type == '1':
        portscanner(target.strip(), startport, endport, whitelist)
    elif target_type == '2':
        scan_ip_range(start_ip.strip(), end_ip.strip(), startport, endport, whitelist)

main()
