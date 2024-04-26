import re, socket, platform, subprocess
from ipaddress import ip_address
from shutil import disk_usage
from os import cpu_count 
def system_info():
    os_information, all_information_about_os, geting_information_about_videocontroller, searching_mac_address = platform.uname(), subprocess.run('systeminfo', stdout = subprocess.PIPE, stderr = subprocess.DEVNULL), subprocess.run('wmic path win32_VideoController get'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL), subprocess.run('netsh wlan show all'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    information_about_computer, information_about_video_controller, get_mac_address = all_information_about_os.stdout.decode('cp866'), geting_information_about_videocontroller.stdout.decode('cp866'), searching_mac_address.stdout.decode('cp866')
    name_video_controller, language_os, os_memory, key_product_os, date_create_os, bios_computer, all_network_adapters = re.search(r'\s\w+[:]\s\d+\sx\s\d+\sx\s\d+\s+(\S+.+)  +\r|\d+\s(\S+.+)', information_about_video_controller), re.search(r'\s(\w+);', information_about_computer), re.search(r'\s(\d+\s\d+\s\w+)', information_about_computer), re.search(r'([a-z-A-Z-0-9]{5}-[a-z-A-Z-0-9]{5}-[a-z-A-Z-0-9]{5}-[a-z-A-Z-0-9]{5})', information_about_computer),  re.search(r'\s+(?P<date>\d+.\d+.+\d), (?P<time>\d+.\d+.+\d)', information_about_computer), re.search(r'BIOS:\s+(?P<bios_name>\S+.+)?.\s(?P<bios_date>\S+)\r', information_about_computer), []
    if bios_computer: 
        bios_computer.groupdict()
        bios_date_and_time = bios_computer['bios_date']
    else: 
        bios_computer = re.search(r'BIOS Version:\s+(?P<bios_name>\S+.+)?[.]+.+[,]\s+(?P<bios_date>\S+)', information_about_computer)
        if bios_computer: 
            bios_computer = bios_computer.groupdict()
            bios_date_and_time = bios_computer['bios_date'].replace('/', '.')
        else: bios_computer, bios_date_and_time = 'None', 'None'
    names_network_adapter, ip_address_route_and_ip_address, ipv6_address_computer, mac_address = re.findall(r'[0[0-9]][:]\s([A-Z]+.+[a-z]+.+)\r', information_about_computer), re.findall(r'(\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3})', information_about_computer),  re.search(r'(\w+[:][:]\w+[:]\w+[:]\w+[:]\w+)', information_about_computer), re.search(r'\s+.+([a-z-0-9]{2}[:][a-z-0-9]{2}[:][a-z-0-9]{2}[:][a-z-0-9]{2}[:][a-z-0-9]{2})', get_mac_address)
    try: size_disk_C = f'{disk_usage('C:\\').total // 1024 // 1024 // 1024}GB'
    except FileNotFoundError: size_disk_C = "You haven't disk"
    try: size_disk_D = f'{disk_usage('D:\\').total // 1024 // 1024 // 1024}GB'
    except FileNotFoundError: size_disk_D = "You haven't disk"
    try: size_disk_E = f'{disk_usage('E:\\').total // 1024 // 1024 // 1024}GB'
    except FileNotFoundError: size_disk_E = "You haven't disk"
    if name_video_controller: 
        if name_video_controller.group(1) == None:
            name_video_controller = re.search(r'\s+\d+\sx\s\d+\sx\s\d+\w+\s+\w+\s+(\S+.+)\r?', information_about_video_controller)
            if name_video_controller: name_video_controller = name_video_controller.group(1).strip()
            else: name_video_controller = 'None'
        else: name_video_controller = name_video_controller.group(1)
    else: 
        name_video_controller = re.search(r'\s+\d+\sx\s\d+\sx\s\d+\w+\s+\w+\s+(\S+.+)\r?', information_about_video_controller)
        if name_video_controller: name_video_controller = name_video_controller.group(1).strip()
        else: name_video_controller = 'None'
    if language_os: language_os = language_os.group(1)
    else: language_os =  'None'
    if os_memory: os_memory = os_memory.group(1)
    else: 
        os_memory = re.search(r'(\d+[,]\d+ MB)', information_about_computer)
        if os_memory: os_memory = os_memory.group(1).replace(',', ' ')
        else: os_memory = 'None'
    if key_product_os: key_product_os = key_product_os.group(1)
    else: key_product_os = 'None'
    if ipv6_address_computer: ipv6_address_computer = ipv6_address_computer.group(1)
    else: ipv6_address_computer = 'None'
    if mac_address: mac_address = mac_address.group(1)
    else: mac_address = 'None'
    try: names_network_adapter, ip_address_route, ip_address_computer = names_network_adapter[1:], ip_address_route_and_ip_address[0], ip_address_route_and_ip_address[1]
    except IndexError: names_network_adapter, ip_address_route, ip_address_computer = 'None', 'None', 'None'
    try: 
        bios_name_index = bios_computer['bios_name'].index('.')
        bios_name = bios_computer['bios_name'][0:bios_name_index]
    except ValueError: bios_name = bios_computer['bios_name']
    except TypeError: bios_name, bios_date_and_time = 'None', 'None'
    for network_adapter in names_network_adapter: all_network_adapters.append({'name': network_adapter}) 
    return {'name': os_information.node, 'architecture': platform.architecture()[0], 'os': os_information.system, 'release': os_information.release, 'type_os': platform.win32_edition(), 'version': os_information.version, 'languaga': language_os, 'date_create_os': f'date: {date_create_os["date"].replace('/', '.')} | time: {date_create_os["time"]}', 'key_product': key_product_os, 'bios': {'name': bios_name, 'date': bios_date_and_time}, 'processor': f'{cpu_count()} kernels | {platform.processor()}', 'video_controller': name_video_controller, 'memory': os_memory, 'size_disk_C': size_disk_C, 'size_disk_D': size_disk_D, 'size_disk_E': size_disk_E, 'network_adapters': all_network_adapters, 'ip_address_route': ip_address_route, 'ip_address': ip_address_computer, 'mac_address': mac_address, 'ipv6_address': ipv6_address_computer} 
def search_wifi():
    searching_all_wifi = subprocess.run('netsh wlan show all'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    information_about_wifi = searching_all_wifi.stdout.decode('cp866')
    all_names_wifi, all_mac_address_wifi, all_signals_wifi = re.findall(r'SSID\s\d+[:]\s(\S+.+)\r', information_about_wifi), re.findall(r'\sBSSID\s\d+[:]\s+(\S+)', information_about_wifi), re.findall(r'\s+.+[:]\s+(\d+%)', information_about_wifi)
    try: all_signals_wifi = all_signals_wifi[1:]
    except IndexError: all_signals_wifi = 'None'
    all_information_wifi, all_information_wifi_for_variable_or_format_json = list(zip(all_names_wifi, all_mac_address_wifi, all_signals_wifi)), []
    for information_about_wifi in all_information_wifi: all_information_wifi_for_variable_or_format_json.append({'ssid': information_about_wifi[0], 'mac_address': information_about_wifi[1], 'signal': information_about_wifi[2]})
    if all([all_information_wifi, all_information_wifi_for_variable_or_format_json]) == False: all_information_wifi, all_information_wifi_for_variable_or_format_json = ['NOT FOUND INFORMATION'] * 2
    if all_information_wifi and all_information_wifi_for_variable_or_format_json == 'NOT FOUND INFORMATION': 
        all_names_wifi, all_mac_address_wifi, all_signals_wifi = re.findall(r'SSID\s\d+\s[:]\s(\S+.+)\r', information_about_wifi), re.findall(r'\sBSSID\s\d+\s+[:]\s(\S+)', information_about_wifi), re.findall(r'\s+.+[:]\s+(\d+%)', information_about_wifi)
        try: all_signals_wifi = all_signals_wifi[1:]
        except IndexError: all_signals_wifi = 'None'
        all_information_wifi, all_information_wifi_for_variable_or_format_json = list(zip(all_names_wifi, all_mac_address_wifi, all_signals_wifi)), []
        for information_about_wifi in all_information_wifi: all_information_wifi_for_variable_or_format_json.append({'ssid': information_about_wifi[0], 'mac_address': information_about_wifi[1], 'signal': information_about_wifi[2]})
        if all([all_information_wifi, all_information_wifi_for_variable_or_format_json]) == False: all_information_wifi, all_information_wifi_for_variable_or_format_json = ['NOT FOUND INFORMATION'] * 2
    return all_information_wifi_for_variable_or_format_json
def connecting_network(): 
    searching_ssid_network = subprocess.run('netsh wlan show all'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    all_ssid_networks, connected_network_ssid = re.findall(r'SSID\s\d+[:]\s(\S+.+)\r', searching_ssid_network.stdout.decode('cp866')), []
    if all_ssid_networks == []: all_ssid_networks = re.findall(r'SSID\s\d+\s[:]\s(\S+.+)\r', searching_ssid_network.stdout.decode('cp866'))
    for ssid_network in all_ssid_networks:
        if subprocess.run(f'netsh wlan connect name="{ssid_network}"'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL).returncode == 0: 
            connected_network_ssid.append(ssid_network) 
            return connected_network_ssid[0]
        else: return "Didn't connect"
def disconnecting_network(): subprocess.run('netsh wlan disconnect'.split(), stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL) 
def scanner(target_ip_address):
    try: ip_address(target_ip_address), print(f'Scanning host: {target_ip_address}')
    except ValueError: print('Not correct ip-address')
    def _output(port, service):
        if len(str(port)) == 1: 
             if len(service)  == 4: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}        {service}       open')
             else: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}       {service}     open')
        elif len(str(port)) == 2:
             if len(service) == 3: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}        {service}       open')
             elif len(service) == 4: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}       {service}       open')
             elif len(service) == 5: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}       {service}      open')
             elif len(service) == 6: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}      {service}      open')
             else: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}      {service}     open')
        elif len(str(port)) == 3:
             if len(service) == 3: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}      {service}       open')
             elif len(service) == 4: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}      {service}       open')
             elif len(service) == 5: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}      {service}      open')
             elif len(service) == 6: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}     {service}      open')
             elif len(service) == 8: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}    {service}     open')
             elif len(service) == 10: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}    {service}   open')
             elif len(service) == 11: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}   {service}   open')
             elif len(service) == 12: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}   {service}  open')
             elif len(service) == 13: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port}  {service}  open')
             else: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n {port} {service} open')
        else:
             if len(service) == 3: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n{port}       {service}       open')
             elif len(service) == 4: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n{port}      {service}       open')
             elif len(service) == 11:  print('-' * 25 + f'\nPORT     SERVICE     TYPE\n{port}   {service}   open')
             else: print('-' * 25 + f'\nPORT     SERVICE     TYPE\n{port}  {service} open')
    try:
        how_much_service, services = -1, ['echo', 'discard', 'chargen', 'ftp', 'ssh', 'telnet', 'smtp', 'rsftp', 'time', 'dns', 'http', 'tor', 'pop3', 'sunrpc', 'mcidas', 'auth or ident', 'ntp', 'ms-rpc', 'netbios-ns', 'netbios-dgm', 'netbios-ssn', 'imap', 'snmp', 'snmptrap', 'dgp', 'ldp', 'https', 'snpp', 'microsoft-ds', 'smpts', 'shell or syslog', 'rtsp', 'imaps', 'pop3s', 'rpc', 'dcom or cap', 'dcom', 'upnp', 'rdp', 'upnp', 'vnc', 'sdk', 'http', 'http', 'sun-answerbook']
        for port in [7, 9, 19, 21, 22, 23, 25, 26, 37, 53, 80, 81, 110, 111, 112, 113, 123, 135, 137, 138, 139, 143, 161, 162, 179, 389, 443, 444, 445, 465, 514, 554, 993, 995, 1025, 1026, 1029, 1900, 3389, 5000, 5900, 8000, 8008, 8080, 8888]: 
            for _ in services: 
                 how_much_service += 1
                 break
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanning:
                    try: scanning.connect((target_ip_address, port))
                    except: pass
                    else: _output(port = port, service = services[how_much_service])
    except KeyboardInterrupt: return
def search_all_ip_addresses_connected_to_network():
    searching_all_ip_addresses, searching_mac_address_computer = subprocess.run('arp -a'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL), subprocess.run('netsh wlan show all'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    all_ip_addresses, all_mac_addresses, mac_address_computer = re.findall(r'\d+[.]\d+[.]\d+[.]\d+', searching_all_ip_addresses.stdout.decode('cp866')), re.findall(r'\w+[:]\w+[:]\w+[:]\w+[:]\w+[:]\w+', searching_all_ip_addresses.stdout.decode('cp866').replace('-', ':')), re.search(r'\s+.+([a-z-0-9]{2}[:][a-z-0-9]{2}[:][a-z-0-9]{2}[:][a-z-0-9]{2}[:][a-z-0-9]{2})', searching_mac_address_computer.stdout.decode('cp866'))
    if mac_address_computer: mac_address_computer = mac_address_computer.group(1)
    else: mac_address_computer = 'None'
    ip_addresses_and_mac_addresses, ip_addresses_and_mac_addresses_for_variable_or_format_json = set(zip(all_ip_addresses[2:], all_mac_addresses[1:])), [[{'ip_address_route': all_ip_addresses[1], 'mac_address_route': all_mac_addresses[0], 'ip_address_computer': all_ip_addresses[0], 'mac_address_computer': mac_address_computer}]]
    for ip_address_and_mac_address in ip_addresses_and_mac_addresses: ip_addresses_and_mac_addresses_for_variable_or_format_json.append([{'ip_address': ip_address_and_mac_address[0], 'mac_address': ip_address_and_mac_address[1]}])
    return ip_addresses_and_mac_addresses_for_variable_or_format_json
def get_network_password():
    searching_network_ssid_with_password = subprocess.run('netsh wlan show profile'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
    ssid_netwok_with_password, network_ssid, network_type_connection, network_type, network_authentication_check, network_encryption, network_password, _network_all_information, _all_information_about_network = re.findall(r'[:]\s([A-Z]{2}\S+)', searching_network_ssid_with_password.stdout.decode('cp866')), [], [], [], [], [], [], [], []
    for ssid in ssid_netwok_with_password:
        geting_network_password = subprocess.run(f'netsh wlan show profile {ssid} key=clear'.split(), stdout = subprocess.PIPE, stderr = subprocess.DEVNULL)
        searching_information_about_network, searching_authentication_network_and_searching_network_encryption, searching_network_type_connection = re.findall(r'\s[:]\s(\S+)', geting_network_password.stdout.decode('cp866')), re.findall(r'\s+\w+[:]\s+([A-Z]\S+)', geting_network_password.stdout.decode('cp866')), re.findall(r'\s+\w+[:]\s+(\w+.+)\r', geting_network_password.stdout.decode('cp866'))
        try: network_ssid.append(searching_information_about_network[0]), network_type_connection.append(searching_network_type_connection[1]), network_type.append(searching_information_about_network[-2]), network_authentication_check.append(searching_authentication_network_and_searching_network_encryption[0]), network_encryption.append(searching_authentication_network_and_searching_network_encryption[1]), network_password.append(searching_information_about_network[-1])
        except IndexError: 
            ssid, password, ident = re.search(r'SSID name\s+[:]\s"(\S+)"', geting_network_password.stdout.decode('cp866')), re.search(r'Key Content\s+[:]\s(\S+)', geting_network_password.stdout.decode('cp866')), True
            if ssid and password:
                _network_all_information.append(list(zip(ssid.group(1).split(), password.group(1).split())))
            else: _all_information_about_network = 'NOT FOUND INFORMATION'
    network_all_information, all_information_about_network = list(zip(network_ssid, network_type_connection, network_type, network_authentication_check, network_encryption, network_password)), []
    for network_information in network_all_information: all_information_about_network.append({'ssid': network_information[0], 'network_type_connection': network_information[1], 'network_type': network_information[2], 'network_authentication_check': network_information[3], 'network_encryption': network_information[4], 'password': network_information[5]})
    try:
        if ident: 
            for _network in _network_all_information: _all_information_about_network.append({'ssid':_network[0][0], 'password': _network[0][1]})
    except UnboundLocalError: pass
    if all_information_about_network == []: 
        if _all_information_about_network == []: return 'NOT FOUND INFORMATION'
        else: return _all_information_about_network
    else: return all_information_about_network