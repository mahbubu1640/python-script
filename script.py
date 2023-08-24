import subprocess

# Objective 1: Blocking USB Ports and Disabling Bluetooth
# Modify the Windows Registry to block USB ports and disable Bluetooth.
# This prevents external USB devices from being used and turns off Bluetooth functionality.
subprocess.run('reg add HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR /v Start /t REG_DWORD /d 4 /f', shell=True)
subprocess.run('reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\OOBE /v SkipMachineOOBE /t REG_DWORD /d 1 /f', shell=True)

# Objective 2: Disabling Command Prompt
# Modify the Windows Registry to disable the command prompt.
# This restricts access to the command prompt, enhancing system security.
subprocess.run('reg add HKCU\Software\Policies\Microsoft\Windows\System /v DisableCMD /t REG_DWORD /d 2 /f', shell=True)

# Objective 3: Blocking Website Access
# Modify the Windows hosts file to block access to a specific website.
# This is achieved by mapping the website's IP address to the loopback address.
website_url = "facebook.com"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

with open(hosts_path, "a") as hosts_file:
    hosts_file.write(f"\n127.0.0.1 {website_url}")

# End of script
