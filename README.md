<div align="center">

# RespResponder
###### Voice notifications so you never miss a hash!
</div>

## - TOC
* [The Issue](#The-Issue)
* [The Fix](#The-Fix)
* [Installation](#Installation)
* [Usage](#Usage)

## The Issue
You fire up Responder for some LLMNR poisoning so you can capture some sweet sweet hashes. You leave Responder running in
the background and continue haxoring the network but totally forget that it's running. Two hours later... You finally realize Responder is
still running and check it. O snap! Multiple hashes were captured an hour and a half ago! You really wish you were notified right away.

## The Fix
Use a handy python script that will give voice notifications when a hash is captured.

## Installation
* Python3 required
* Playsound python package required
```bash
pip3 install playsound
```
* If Responder is not installed to default location then open 'respResponder.py` in your favorite editor and add the path on line 8:
```python
### If Responder was not installed to the default location enter log path below ###
##Custom log path:
log_path = "./Responder-Session.log"
```
## Usage
* Run `respResponder.py`
```python
python3 respResponder.py
```
* Run Responder
```bash
sudo responder -I eth0 -dPv
```

