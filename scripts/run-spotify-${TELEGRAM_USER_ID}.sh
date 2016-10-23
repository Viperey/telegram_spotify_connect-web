#!/bin/bash
sudo cp -f /home/osmc/telegram_spotify/keys/${USERNAME}_spotify_appkey.key /home/osmc/spotify-connect-web-chroot/usr/src/app/
/home/osmc/spotify-connect-web.sh --username ${USERNAME} --password ${PASSWORD} --bitrate 320 --name osmc
