import Modules.module_for_base_tool as module_for_base_tool, Modules.module_for_windows_tool as module_for_windows_tool
from subprocess import run, DEVNULL
from re import search
from os import system
def start_console_windows():
    while True:
        try: 
            try: command_user, windows_commands = input('>>> ').strip(), ['help', 'clear', 'system', 'search wifi', 'network', 'network -c', 'network -d', 'search ip', 'scan', 'get wifi password', 'screenshot', 'sms bomber', 'ddos', 'website', 'socials', 'file', 'shutdown', 'exit']
            except KeyboardInterrupt: exit()
            if 'help' == command_user: print('help - Output about all commands information\nclear - Clear output\nsystem - Search all information about your computer\nsearch wifi - Search wifi around you\nnetwork - This work to network\nsearch ip - Search all ip-addresses connected your network\nscan ip-address - Scan ports of ip-address\nget wifi password - Get all passwords wifi save your computer\nscreenshot file name - Make screenshot\nsms bomber - It is number phone sms bomber only Ukraine number phone example +380500334635\nddos - Distributed denial of service attack on ip-address\nget wifi password - Get all passwords wifi save your computer\nwebsite - Download website\nsocials - Search profile socials network of nickname\nfile - Encode file or decode file\nshutdown - Shutdown your computer\nexit - Exit in the program')
            if 'clear' == command_user: system('cls')
            if 'system' == command_user: 
                computer = module_for_windows_tool.system_info()
                print(f'computer name: {computer["name"]}\narchitecture: {computer["architecture"]}\nos: {computer["os"]} {computer["release"]} {computer["type_os"]}\nversion os: {computer["version"]}\nlanguage os: {computer["languaga"]}\nDate created os: {computer["date_create_os"]}\nBIOS name: {computer["bios"]["name"]} date: {computer["bios"]["date"]}\nprocessor: {computer["processor"]}\nvideo controller: {computer["video_controller"]}\nmemory: {computer["memory"]}\nC: {computer["size_disk_C"]} D: {computer["size_disk_D"]} E: {computer["size_disk_E"]}\nnetwork adapters: {[network_adapter["name"] for network_adapter in computer["network_adapters"]]}\nip-address route: {computer["ip_address_route"]}\nip-address os: {computer["ip_address"]}\nmac-address os: {computer["mac_address"]}\nipv6-address os: {computer["ipv6_address"]}')
            if 'search wifi' == command_user: 
                for wifi in module_for_windows_tool.search_wifi(): print('-' * len(f'mac-address: {wifi["mac_address"]}') + f'\nname: {wifi["ssid"]}\nmac-address: {wifi["mac_address"]}\nsignal: {wifi["signal"]}\n' + '-' * len(f'mac-address: {wifi["mac_address"]}'))
            if 'search ip' == command_user:
                all_ip_addresses_connected_to_network = []
                for ip_addresses in module_for_windows_tool.search_all_ip_addresses_connected_to_network():
                    try: 
                        try: search(r'(2[1-9]{2}[.]\d+[.]\d+[.]\d+)|(\d+[.]\d+[.]\d+[.]2[50-55])', ip_addresses[0]['ip_address']).group(1)
                        except AttributeError: all_ip_addresses_connected_to_network.append(ip_addresses[0]['ip_address'])
                    except KeyError: all_ip_addresses_connected_to_network.append(ip_addresses[0]['ip_address_route']), all_ip_addresses_connected_to_network.append(ip_addresses[0]['ip_address_computer'])
                for ip in all_ip_addresses_connected_to_network: print(f'This ip-address connected your network: {ip}')    
            if 'scan' in command_user: 
                try:
                    if f'scan {search(r"(\d+[.]\d+[.]\d+[.]\d+)", command_user).group(1)}' == command_user: windows_commands.append(f'scan {search(r"(\d+[.]\d+[.]\d+[.]\d+)", command_user).group(1)}'), module_for_windows_tool.scanner(target_ip_address = search(r'(\d+[.]\d+[.]\d+[.]\d+)', command_user).group(1))
                except AttributeError: print('scan ip-address')
            if 'network' in command_user:
                if 'network -c' == command_user: print(module_for_windows_tool.connecting_network())
                elif 'network -d' == command_user: module_for_windows_tool.disconnecting_network()
                else: print('network -c - connecting to network\nnetwork -d - disconnecting to network')
            if 'get wifi password' == command_user:
                for information_about_wifi in module_for_windows_tool.get_network_password(): 
                    try: print('-' * len(f'password: {information_about_wifi["password"]}') + f'\nname: {information_about_wifi["ssid"]}\npassword: {information_about_wifi["password"]}\n' + '-' * len(f'password: {information_about_wifi["password"]}'))
                    except TypeError: 
                        print('NOT FOUND INFORMATION')
                        break
            if 'screenshot' in command_user: 
                try:
                    if f'screenshot {search(r"screenshot (\w+)", command_user).group(1)}' == command_user: 
                        try: windows_commands.append(f'screenshot {search(r"screenshot (\w+)", command_user).group(1)}'), module_for_base_tool.make_screenshot(file_name = search(r'screenshot (\w+)', command_user).group(1) + '.png')
                        except SystemError: print("Didn't make screenshot")
                except AttributeError: print('screenshot file name')
            if 'sms bomber' in command_user:
                try:
                    if f'sms bomber -n {search(r"([+]380\d{9})", command_user).group(1)} -b {search(r"[+]380\d{9} -b (\d+)", command_user).group(1)} -m {search(r"[+]380\d{9} -b \d+ -m (fast|medium|normal)", command_user).group(1)}' == command_user: 
                        try: windows_commands.append(f'sms bomber -n {search(r"([+]380\d{9})", command_user).group(1)} -b {search(r"[+]380\d{9} -b (\d+)", command_user).group(1)} -m {search(r"[+]380\d{9} -b \d+ -m (fast|medium|normal)", command_user).group(1)}'), module_for_base_tool.phone_sms_bomber(target_number_phone = search(r'([+]380\d{9})', command_user).group(1), how_much_sms_bomber_attacks = int(search(r'[+]380\d{9} -b (\d+)', command_user).group(1)), mode = search(r'[+]380\d{9} -b \d+ -m (fast|medium|normal)', command_user).group(1))
                        except ConnectionError: print('No internet connection')
                except AttributeError: print('sms bomber -n number phone -b how much number phone sms bomber attacks -m mode number phone sms bomber have only modes (fast, medium, normal)')
            if 'ddos' in command_user: 
                try: 
                    if f'ddos -i {search(r"ddos -i (\d+[.]\d+[.]\d+[.]\d+)", command_user).group(1)} -m {search(r"ddos -i \d+[.]\d+[.]\d+[.]\d+ -m (\d+)", command_user).group(1)}' == command_user: windows_commands.append(f'ddos -i {search(r"ddos -i (\d+[.]\d+[.]\d+[.]\d+)", command_user).group(1)} -m {search(r"ddos -i \d+[.]\d+[.]\d+[.]\d+ -m (\d+)", command_user).group(1)}'), module_for_base_tool.ddos_attack(target_ip_address = search(r'ddos -i (\d+[.]\d+[.]\d+[.]\d+)', command_user).group(1), how_much_attacks = int(search(r'ddos -i \d+[.]\d+[.]\d+[.]\d+ -m (\d+)', command_user).group(1)))
                except AttributeError: print('ddos -i ip-address -m how much attacks') 
            if 'website' in command_user: 
                try: 
                    if f'website -u {search(r"website -u (\S+)", command_user).group(1)} -n {search(r"website -u \S+ -n (\w+)", command_user).group(1)}' == command_user: windows_commands.append(f'website -u {search(r"website -u (\S+)", command_user).group(1)} -n {search(r"website -u \S+ -n (\w+)", command_user).group(1)}'), module_for_base_tool.download_website(url_website = search(r'website -u (\S+)', command_user).group(1), file_name = search(r'website -u \S+ -n (\w+)', command_user).group(1))
                except AttributeError: print('website -u url -n file name')
                except ConnectionError: print('No internet connection')
            if 'socials' in command_user:
                try:
                    if f'socials {search(r"socials (\S+.+)", command_user).group(1)}': 
                        try: windows_commands.append(f'socials {search(r"socials (\S+.+)", command_user).group(1)}'), module_for_base_tool.search_socials_network_profile(nickname = search(r'socials (\S+.+)', command_user).group(1))
                        except SystemError: print("Didn't work to search profile socials network of nickname")
                except AttributeError: print('socials nickname - search profile socials network of nickname') 
            if 'file' in command_user: 
                try: 
                    if 'file -e' in command_user:
                        if f'file -e {search(r"file -e (\S+)", command_user).group(1)}' == command_user: windows_commands.append(f'file -e {search(r"file -e (\S+)", command_user).group(1)}'), module_for_base_tool.encode_file(file_path = search(r'file -e (\S+)', command_user).group(1))
                except AttributeError: print('file -e file path')
                try: 
                    if 'file -d' in command_user:
                        if f'file -d {search(r"file -d (\S+)", command_user).group(1)}' == command_user: windows_commands.append(f'file -d {search(r"file -d (\S+)", command_user).group(1)}'), module_for_base_tool.decode_file(file_path = search(r'file -d (\S+)', command_user).group(1))
                except AttributeError: print('file -d file path for encode')
                try:
                    if f'file{command_user[4]}': pass
                    else: print('file -e file path - this for encode file\nfile -d file encoded path - this for decode file') 
                except IndexError: print('file -e file path - this for encode file\nfile -d file encoded path - this for decode file') 
            if 'shutdown' == command_user: run('shutdown /f /t 0 /s'.split(), stdout = DEVNULL, stderr = DEVNULL)
            if 'exit' == command_user: exit()
            if not command_user in windows_commands: print(f'Not found command {command_user}')
        except FileNotFoundError: print("Didn't work this tool")
