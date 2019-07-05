
<img src="./calathes2.svg"  height="300"></img>

# Calathis
RPI timelapse camera app

# Quickstart raspberry pi installation
```

#enable camera in raspiconfig and reboot
sudo raspi-config
sudo reboot

# By default it assumes it can write to /media/pi/data
sudo mkdir -p /media/pi/data
sudo chown pi:pi /media/pi/data

# Install Calathes
sudo pip install https://github.com/martyni/Calathis/archive/master.zip

# Run a basic example
for each in {1..20}
   do take_picture_now
   sleep 5
done
make_gif_today
```
## Use Cron to take multiple pictures and create gifs
```
crontab -e
*/2 3-6 * * * take_picture_now
0 13 * * * make_gif_today
```
