# python-notifi.it-script
 
steps to get this script working
- download and install python3 from https://www.python.org/downloads/
- once python is installed, using command prompt, get to python script directory by doing the command 
 `cd C:\Users\<userName>\AppData\Local\Programs\Python\Python310\Scripts`
- run command `pip install requests`. Once finished, you can close command prompt
- download the [iOS app](https://developer.apple.com/app-store/marketing/guidelines/images/badge-example-preferred_2x.png) or [Android app](https://play.google.com/store/apps/details?id=it.notifi.notifi) for Notifi.it
- Once downloaded open the app, it should display the key you can use for push notifications
- Download the script from this repository, open script and adjust necessary values. Save script
- Ensure script works by double clicking on file and verifying notification is sent to your phone
- Right click on script and create shortcut.
- Go to windows search bar, type Run, hit enter, type in `shell:startup`
- Copy shortcut of script into startup folder.

Now you have phone push notifications that occur when your windows pc is rebooted/restarted.
