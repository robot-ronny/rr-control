# rr-control
Robot Ronny Control tools

## Install
```
git clone https://github.com/robot-ronny/rr-control.git

cd rr-control

sudo pip3 install -e .
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
