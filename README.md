# rr-control
Robot Ronny Control tools

## Install
```
git clone https://github.com/robot-ronny/rr-control.git

cd rr-control

sudo pip3 install -e .
```

## Add udev rules
/etc/udev/rules.d/10-ronny-wheels.rules
```
SUBSYSTEMS=="usb", ACTION=="add", KERNEL=="ttyUSB*", ATTRS{devpath}=="1.3", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", SYMLINK+="ttyRonnyWheels", TAG+="systemd", ENV{SYSTEMD_ALIAS}="/dev/ttyRonnyWheels"
```

/etc/udev/rules.d/10-ronny-body.rules
```
SUBSYSTEMS=="usb", ACTION=="add", KERNEL=="ttyUSB*", ATTRS{devpath}=="1.5", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", SYMLINK+="ttyRonnyBody", TAG+="systemd", ENV{SYSTEMD_ALIAS}="/dev/ttyRonnyBody"
```

## Service enable
```
pm2 --interpreter "python3" start rr-control-wheels -- --device /dev/ttyRonnyWheels

pm2 --interpreter "python3" start rr-control-body -- --device /dev/ttyRonnyBody

pm2 save
```

## Usage
```
rr-control-wheels --help

rr-control-body --help
```
