## Telegram bot for Spotify-connect-web

So you have an OSMC running in your raspberry pi and you want to use spotify on it.

[Spotify-connect-web](https://github.com/Fornoth/spotify-connect-web) is a usefull plugin/add-on on OSMC for such
purpose.
The problem comes when many people want to connect its Spotify account to the OSMC.

So here's a possible solution for the problem. Using a telegram bot, it will handle the process of killing
(gracefully) any previous instance of Spotify-connect-web, and run a new one with the correct user.


### Installation

1. Ssh into your raspberry pi with a OSMC instance running.
2. Fulfill the pre-requisites
3. Clone this project at /home/osmc
4. Copy service/telegram_spotify.service to /etc/systemd/system/
5. Run ```sudo systemctl enable telegram_spotify.service```
6. Copy your spotify key to the *keys* folder
7. Create a file inside the script folder
    1. Filename: run-spotify-${TELEGRAM_USER_ID}.sh. The TELEGRAM_USER_ID value is mandatory. The same bot will prompt
    your ID when you try to use it without being authorized.
    2. Inside the file, modify your key file name and credentials in order to match path and filenames.
8. Reboot the system

### Usage

1. Open a dialog with the telegram's bot you've just create.  
2. Send a ```/start``` message.  
3. In a few seconds (~10) you will see a new device available (osmc) inside your spotify app (desktop or mobile).
4. Select that device and listen to some wonderful music. 

### Pre-requisites

1. [Install a spotify web server in your RPi-OSMC](https://discourse.osmc.tv/t/howto-setup-a-spotify-connect-web-server-on-a-raspberry-pi-with-osmc/15818)
2. Create your won telegram bot, you can follow some steps [here](https://github.com/Viperey/telegram_transmission/blob/master/README.md)
    1. Ignore the step for adding the command to the /etc/rc.local file.


### Bibliography

https://discourse.osmc.tv/t/howto-setup-a-spotify-connect-web-server-on-a-raspberry-pi-with-osmc/15818
https://discourse.osmc.tv/t/osmc-running-custom-script-at-boot/2425/2
