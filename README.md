# fritzdemo
Minimalistic example for changing SSID and password on avm routers and repeaters with FritzConnection.

As a base dependency you have to install fritzconnection via

```bash
pip3 install fritzconnection
```

After that just create a connection to your FRITZ!box and every other fritz device that should be updated:
```python
# 
FritzConnection(address='192.168.178.1', user='fritz****', password='<password>', use_tls=False)
```
Please inspect the set_password_and_ssid function in set_ssid_password.py to see how to receive and set the ssid and password of your network. The demo defaults to the guest wifi config "WLANConfiguration:3". You can change this to your needs. 

The example codes generates the phrase "It's dayOtTheWeek \(^_^)/" in german with a specific emoji for every day of the week. Not really useful, just a little easteregg.
