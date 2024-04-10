from sys import platform
if platform == 'win32': 
    from Windows.windows_console import start_console_windows 
    start_console_windows()
elif platform == 'linux': 
    from Linux.linux_console import start_console_linux
    start_console_linux()
else: print("Don't support OS")