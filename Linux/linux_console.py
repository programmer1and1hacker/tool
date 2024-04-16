import Modules.module_for_base_tool as module_for_base_tool, Modules.module_for_linux_tool as module_for_linux_tool
from subprocess import run, DEVNULL
from tabulate import tabulate
from os.path import exists
from re import search
from os import system
def start_console_linux(): 
    while True:
        try: command_user, linux_commands = input('>>> ').strip(), ['help', 'clear', 'system', 'wifi', 'search wifi', 'hack wifi', 'dos wifi', 'beacon wifi', 'fuzzer wifi', 'tor', 'tor -e', 'tor -d', 'mac', 'search ip', 'scan', 'screenshot', 'sms bomber', 'ddos', 'website', 'set website', 'check website', 'socials', 'file', 'shutdown', 'exit']
        except KeyboardInterrupt: exit()
        if 'help' == command_user: print('help - Output about all commands information\nclear - Clear output\nsystem - Search all information about your computer\nwifi - Work with wifi\ntor - Anonymous network the tor\nmac - Change mac-address\nsearch ip - Search all ip-addresses connected your network\nscan - Ip-address or website scan OS and ports\nscreenshot file name - Make screenshot\nsms bomber - It is number phone sms bomber only Ukraine number phone example +380500334635\nddos - Distributed denial of service attack on ip-address\nwebsite - Download website or check all web directories of this website\nsocials - Search profile socials network of nickname\nfile - Encode file or decode file\nshutdown - Shutdown your computer\nexit - Exit in the program')
        if 'clear' == command_user: system('clear')
        if 'system' == command_user: 
            computer, interfaces = module_for_linux_tool.system_info(), []
            for interface in range(1, 6):
                try: interfaces.append(f'Interface: {computer[interface]["interface"]} Mac-address: {computer[interface]["mac_address"]}')
                except IndexError: break
            print(f'Architecture: {computer[0]["architecture"]}\nOS: {computer[0]["os"]}\nOperation memory: {computer[0]["operation_memory"]}\nProcessor: {computer[0]["processor"]}\nVideo controller: {computer[0]["video_controller"]}\nIp-address route: {computer[0]["ip_address_route"]}\nIp-address computer: {computer[0]["ip_address_computer"]}\nIpv6-address computer: {computer[0]["ipv6_address_computer"]}\n{interfaces}')
        if 'wifi' in command_user:
            if 'search wifi' == command_user: 
                try: print(tabulate(module_for_linux_tool.search_wifi(), headers = [('FREQUENCY'), ('SSID'), ('MAC-ADDRESS'), ('CHANNEL'), ('MODE'), ('ENCRYPTION-ENABLED'), ('ENCRYPTION'), ('CIPHER'), ('AUTHENTICATION'), ('IEEE'), ('SIGNAL')], tablefmt = 'pipe'))
                except SystemError: print("You haven't interface with monitor mode")
                continue
            try:
                if 'hack wifi -s ' + search(r'hack wifi -s (\S+.+)', command_user).group(1) == command_user: 
                    try: wifi = module_for_linux_tool.hack_wifi(wifi_name = search(r'hack wifi -s (\S+.+)', command_user).group(1))
                    except ValueError: system('clear'), print('Not found wifi for hack wifi')
                    except SystemError: system('clear'), print("You haven't interface with monitor mode")
                    except TimeoutError: system('clear'), print("Can't be continued attack happened a error")
                    except SystemExit: system('clear'), print("Didn't work hack wifi")
                    else:
                        try: system('clear'), print(tabulate([(wifi['type_hacked_wifi'], wifi['ssid'], wifi['bssid'], wifi['channel'], wifi['wps_pin'], wifi['password'])], [('TYPE-HACKED-WIFI'), ('SSID'), ('BSSID'), ('CHANNEL'), ('WPS-PIN'), ('PASSWORD')], tablefmt = 'pipe'))
                        except KeyError: system('clear'), print(tabulate([(wifi['type_hacked_wifi'], wifi['ssid'], wifi['bssid'], wifi['password'])], [('TYPE-HACKED-WIFI'), ('SSID'), ('BSSID'), ('PASSWORD')], tablefmt = 'pipe'))
                    continue
            except AttributeError: pass
            try:
                if 'hack wifi -s ' + search(r'hack wifi -s (\S+.+) -d', command_user).group(1) + ' -d ' + search(r'hack wifi -s \S+.+ -d (\S+)', command_user).group(1) == command_user: 
                    try: wifi = module_for_linux_tool.hack_wifi(wifi_name = search(r'hack wifi -s (\S+.+) -d', command_user).group(1), file_dictionary_passwords = search(r'hack wifi -s \S+.+ -d (\S+)', command_user).group(1))
                    except ValueError: system('clear'), print('Not found wifi for hack wifi')
                    except SystemError: system('clear'), print("You haven't interface with monitor mode")
                    except TimeoutError: system('clear'), print("Can't be continued attack happened a error")
                    except FileNotFoundError: system('clear'), print('This file not found or this file not is txt')
                    except SystemExit: system('clear'), print("Didn't work hack wifi")
                    else:
                        try: system('clear'), print(tabulate([(wifi['type_hacked_wifi'], wifi['ssid'], wifi['bssid'], wifi['channel'], wifi['wps_pin'], wifi['password'])], [('TYPE-HACKED-WIFI'), ('SSID'), ('BSSID'), ('CHANNEL'), ('WPS-PIN'), ('PASSWORD')], tablefmt = 'pipe'))
                        except KeyError: system('clear'), print(tabulate([(wifi['type_hacked_wifi'], wifi['ssid'], wifi['bssid'], wifi['password'])], [('TYPE-HACKED-WIFI'), ('SSID'), ('BSSID'), ('PASSWORD')], tablefmt = 'pipe'))
                    continue
            except AttributeError: pass
            try:
                if 'dos wifi -s ' + search(r'dos wifi -s (\S+.+) -t', command_user).group(1) + ' -t ' +  search(r'dos wifi -s \S+.+ -t (\d+)', command_user).group(1) == command_user: 
                    try: module_for_linux_tool.dos_attack_wifi(wifi_name = search(r'dos wifi -s (\S+.+) -t', command_user).group(1), how_much_time_long_attack = int(search(r'dos wifi -s \S+.+ -t (\d+)', command_user).group(1)))
                    except ZeroDivisionError: print('Not must be dos wifi -s wifi name -t 0')
                    except ValueError: system('clear'), print('Not found wifi for dos-attack wifi')
                    except SystemError: system('clear'), print("You haven't interface with monitor mode")
                    except TimeoutError: system('clear'), print("Didn't work dos-attack wifi")
                    continue
            except AttributeError: pass
            try:
                if 'beacon wifi -t ' + search(r'beacon wifi -t (\d+)', command_user).group(1) == command_user: 
                    try: module_for_linux_tool.beacon_flood_attack_wifi(how_much_time_long_attack = int(search(r'beacon wifi -t (\d+)', command_user).group(1)))
                    except ZeroDivisionError: print('Not must be beacon wifi -t 0')
                    except SystemError: system('clear'), print("You haven't interface with monitor mode")
                    continue
            except AttributeError: pass
            try:
                if 'fuzzer wifi -t ' + search(r'fuzzer wifi -t (\d+)', command_user).group(1) == command_user: 
                    try: module_for_linux_tool.fuzzer_attack_wifi(how_much_time_long_attack = int(search(r'fuzzer wifi -t (\d+)', command_user).group(1)))
                    except ValueError: system('clear'), print("Can't be digit zero in how_much_time_long_attack")
                    except SystemError: system('clear'), print("You haven't interface with monitor mode")
                    continue
            except AttributeError: print('search wifi - Search wifi around you\nhack wifi -s name wifi - or - hack wifi -s name wifi -d path to file password format only txt - Hack wifi and get password or wps pin of wifi\ndos wifi -s name wifi -t how much time long attack - Distributed denial of wifi attack\nbeacon wifi -t how much time long attack - Beacon flood attack wifi this can sometimes crash network scanners and even drivers\nfuzzer wifi -t how much time long attack - Fuzzer attack on wifi a simple packet fuzzer with multiple packet sources and a nice set of modifiers')
        if 'tor' in command_user:
            if 'tor -e' == command_user: 
                try:
                    ip_address = module_for_linux_tool.change_ip_address()
                    print(tabulate([(ip_address['current_ip_address'], ip_address['new_ip_address'])], headers = [('CURRENT-IP-ADDRESS'), ('NEW-IP-ADDRESS')], tablefmt = 'grid'))
                except ConnectionError: print('No internet connection')
                except SystemError: print('Install error in the tool toriptables2')
            elif 'tor -d' == command_user:
                if exists('/usr/local/bin/toriptables2.py'): run('sudo toriptables2.py -f'.split(), stdout = DEVNULL, stderr = DEVNULL), print('Disabled network the tor')
                else: print("You haven't the tor")
            else: print('tor -e - Enable anonymous network the tor\ntor -d - Disable network the tor')
        if 'mac' == command_user: 
            try: 
                mac_address = module_for_linux_tool.change_mac_address()
                print(tabulate([(mac_address['current_mac_address'], mac_address['new_mac_address'])], headers = [('CURRENT-MAC-ADDRESS'), ('NEW-MAC-ADDRESS')], tablefmt = 'grid'))
            except ConnectionError: print('No internet connection')
        if 'search ip' == command_user: 
            try: find_all_ip_addresses, how_much_device = module_for_linux_tool.search_all_ip_addresses_connected_with_network(), 0
            except SystemError: print('Install error in the tool toriptables2')
            except ConnectionError: print('No internet connection')
            else:
                for device in find_all_ip_addresses: 
                    how_much_device += 1
                    if how_much_device == 1: print('-' * len(f'Device route: {device[0]["device_route"]}') + f'\nIp-address route: {device[0]["ip_address_route"]}\nMac-address route: {device[0]["mac_address_route"]}\nDevice route: {device[0]["device_route"]}\n' + '-' * len(f'Device route: {device[0]["device_route"]}')), print(f'Ip-address your computer: {device[0]["ip_address_computer"]}\nMac-address your computer: {device[0]["mac_address_computer"]}\n' + '-' * len(f'Mac-address your computer: {device[0]["mac_address_computer"]}'))
                    try: print(f'Found the ip-address: {device["ip_address"]}\nFound the mac-address: {device["mac_address"]}\nFound the device: {device["device"]}\n' + '-' * len(f'Found the device: {device["device"]}'))
                    except TypeError: pass
        if 'scan' in command_user: 
            try:
                if 'scan ' + search(r'scan (\S+)', command_user).group(1) == command_user: 
                    try: 
                        linux_commands.append('scan ' + search(r'scan (\S+)', command_user).group(1))
                        information_about_target = module_for_linux_tool.scanner(target_ip_address_or_url_website = 'scan ' + search(r'scan (\S+)', command_user).group(1))
                    except ConnectionError: print('No internet connection')
                    except SystemError: print('Install error in the tool toriptables2')
                    else:
                        for target in information_about_target: 
                            try: 
                                if len(target['port']) == 2:
                                    if len(target['service']) == 3: print('-' * 17 + f'\nPORT|SERVICE|TYPE\n {target["port"]}    {target["service"]}   {target["status_port"]}\n' + '-' * 17)
                                    elif len(target['service']) == 4: print('-' * 17 + f'\nPORT|SERVICE|TYPE\n {target["port"]}    {target["service"]}  {target["status_port"]}\n' + '-' * 17)
                                    elif len(target['service']) == 5: print('-' * 17 + f'\nPORT|SERVICE|TYPE\n {target["port"]}   {target["service"]}  {target["status_port"]}\n' + '-' * 17)
                                    elif len(target['service']) == 6: print('-' * 17 + f'\nPORT|SERVICE|TYPE\n {target["port"]}   {target["service"]} {target["status_port"]}\n' + '-' * 17)
                                    else: print('-' * 19 + f'\nPORT |SERVICE| TYPE\n {target["port"]} {target["service"]} {target["status_port"]}\n' + '-' * 19)
                                elif len(target['port']) == 4: 
                                    if len(target['service']) == 3: print('-' * 17 + f'\nPORT|SERVICE|TYPE\n{target["port"]}   {target["service"]}   {target["status_port"]}\n' + '-' * 17)
                                    elif len(target['service']) == 4: print('-' * 17 + f'\nPORT|SERVICE|TYPE\n{target["port"]}   {target["service"]}  {target["status_port"]}\n' + '-' * 17)
                                    elif len(target['service']) == 5: print('-' * 17 + f'\nPORT|SERVICE|TYPE\n{target["port"]}  {target["service"]}  {target["status_port"]}\n' + '-' * 17)
                                    elif len(target['service']) == 6: print('-' * 17 + f'\nPORT|SERVICE|TYPE\n{target["port"]}  {target["service"]} {target["status_port"]}\n' + '-' * 17)
                                    else: print('-' * 17 + f'\nPORT|SERVICE|TYPE\n{target["port"]} {target["service"]} {target["status_port"]}\n' + '-' * 17)
                                else: print('-' * 19 + f'\nPORT |SERVICE| TYPE\n{target["port"]} {target["service"]}  {target["status_port"]}\n' + '-' * 19)
                            except TypeError: print(f'\nHost: {target[0]["ip_address"]}\nOS: {target[0]["os"]}\nClosed ports: ' + search(r'(\d+)', target[0]["closed_ports"]).group(1))
            except AttributeError: print('scan ip-address or website')
        if 'screenshot' in command_user: 
            try:
                if 'screenshot ' + search(r'screenshot (\w+)', command_user).group(1) == command_user: linux_commands.append('screenshot ' + search(r'screenshot (\w+)', command_user).group(1)), module_for_base_tool.make_screenshot(file_name = search(r'screenshot (\w+)', command_user).group(1) + '.png')
            except AttributeError: print('screenshot file name')
        if 'sms bomber' in command_user:
            try:
                if 'sms bomber -n ' + search(r'([+]380\d{9})', command_user).group(1) + ' -b ' + search(r'[+]380\d{9} -b (\d+)', command_user).group(1) + ' -m ' + search(r'[+]380\d{9} -b \d+ -m (fast|medium|normal)', command_user).group(1) == command_user: 
                    try: linux_commands.append('sms bomber -n ' + search(r'([+]380\d{9})', command_user).group(1) + ' -b ' + search(r'[+]380\d{9} -b (\d+)', command_user).group(1) + ' -m ' + search(r'[+]380\d{9} -b \d+ -m (fast|medium|normal)', command_user).group(1)), module_for_base_tool.phone_sms_bomber(target_number_phone = search(r'([+]380\d{9})', command_user).group(1), how_much_sms_bomber_attacks = int(search(r'[+]380\d{9} -b (\d+)', command_user).group(1)), mode = search(r'[+]380\d{9} -b \d+ -m (fast|medium|normal)', command_user).group(1))
                    except ConnectionError: print('No internet connection')
            except AttributeError: print('sms bomber -n number phone -b how much number phone sms bomber attacks -m mode number phone sms bomber have only modes (fast, medium, normal)')
        if 'ddos' in command_user: 
            try: 
                if 'ddos -i ' + search(r'ddos -i (\d+[.]\d+[.]\d+[.]\d+)', command_user).group(1) + ' -m ' + search(r'ddos -i \d+[.]\d+[.]\d+[.]\d+ -m (\d+)', command_user).group(1) == command_user: linux_commands.append('ddos -i ' + search(r'ddos -i (\d+[.]\d+[.]\d+[.]\d+)', command_user).group(1) + ' -m ' + search(r'ddos -i \d+[.]\d+[.]\d+[.]\d+ -m (\d+)', command_user).group(1)), module_for_base_tool.ddos_attack(target_ip_address = search(r'ddos -i (\d+[.]\d+[.]\d+[.]\d+)', command_user).group(1), how_much_attacks = int(search(r'ddos -i \d+[.]\d+[.]\d+[.]\d+ -m (\d+)', command_user).group(1)))
            except AttributeError: print('ddos -i ip-address -m how much attacks') 
        if 'website' in command_user: 
            try: 
                if 'set website -u ' + search(r'set website -u (\S+)', command_user).group(1) + ' -n ' + search(r'set website -u \S+ -n (\w+)', command_user).group(1) == command_user: 
                    try:linux_commands.append('set website -u ' + search(r'set website -u (\S+)', command_user).group(1) + ' -n' + search(r'set website -u \S+ -n (\w+)', command_user).group(1)), module_for_base_tool.download_website(url_website = search(r'set website -u (\S+)', command_user).group(1), file_name = search(r'set website -u \S+ -n (\w+)', command_user).group(1))
                    except ConnectionError: print('No internet connection')
                    continue
            except AttributeError: pass
            try: 
                if 'check website -u ' + search(r'check website -u (\S+)', command_user).group(1) == command_user: 
                    try: 
                        linux_commands.append('check website -u ' + search(r'check website -u (\S+)', command_user).group(1))
                        try: name_website = search(r'\S+[:]//(\S+)*', command_user).group(1)
                        except AttributeError: name_website = search(r'check website -u (\S+)', command_user).group(1)
                        else:
                            if '/' in name_website[-1:]: name_website = name_website[:name_website.index('/')]
                        print(f'Searching web directories of this website: {name_website}\n' + '-' * len(f'Searching web directories of this website: {name_website}'))
                        found_all_website_directories = module_for_linux_tool.search_web_directories_of_this_website(url_website = search(r'check website -u (\S+)', command_user).group(1))
                    except ConnectionError: print('No internet connection')
                    else: 
                        if 'NOT FOUND INFORMATION' in found_all_website_directories: print('Not found web directories of this website')
                        else:
                            for url in found_all_website_directories: print(f'Url: {url}')
                    continue
            except AttributeError: print('set website -u url -n file name\ncheck website -u url - search all web directories of this website')
        if 'socials' in command_user:
            try:
                if 'socials ' + search(r'socials (\S+.+)', command_user).group(1): 
                    try: linux_commands.append('socials ' + search(r'socials (\S+.+)', command_user).group(1)), module_for_base_tool.search_socials_network_profile(nickname = search(r'socials (\S+.+)', command_user).group(1))
                    except SystemError: print("Didn't work to search profile socials network of nickname")
            except AttributeError: print('socials nickname - search profile socials network of nickname') 
        if 'file' in command_user: 
            try: 
                if 'file -e' in command_user:
                    if 'file -e ' + search(r'file -e (\S+)', command_user).group(1) == command_user: linux_commands.append('file -e ' + search(r'file -e (\S+)', command_user).group(1)), module_for_base_tool.encode_file(file_path = search(r'file -e (\S+)', command_user).group(1))
            except AttributeError: print('file -e file path')
            try: 
                if 'file -d' in command_user:
                    if 'file -d ' + search(r'file -d (\S+)', command_user).group(1) == command_user: linux_commands.append(f'file -d ' + search(r'file -d (\S+)', command_user).group(1)), module_for_base_tool.decode_file(file_path = search(r'file -d (\S+)', command_user).group(1))
            except AttributeError: print('file -d file path for encode')
            try:
                if f'file{command_user[4]}': pass
                else: print('file -e file path - this for encode file\nfile -d file encoded path - this for decode file') 
            except IndexError: print('file -e file path - this for encode file\nfile -d file encoded path - this for decode file') 
        if 'shutdown' == command_user: run('shutdown', stdout = DEVNULL, stderr = DEVNULL)
        if 'exit' == command_user: exit() 
        if not command_user in linux_commands: print(f'Not found command {command_user}')
