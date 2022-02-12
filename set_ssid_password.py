from fritzconnection import FritzConnection
import locale
import datetime

locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")

emojis = {
    "Montag": "(*__*)",
    "Dienstag": "(@__*)",
    "Mittwoch": "(@_@)",
    "Donnerstag": "\(@_@)",
    "Freitag": "\(@_@)/",
    "Samstag": "\(^_^)/",
    "Sonntag": "(*_@)"
}


def set_ssid_and_password(f_connection, new_ssid, new_password, wifi_config='WLANConfiguration:3'):
    print("Setting ssid and password on {}".format(f_connection.address))
    security_keys = f_connection.call_action(wifi_config, 'GetSecurityKeys')
    security_keys['NewKeyPassphrase'] = new_password
    f_connection.call_action(wifi_config,
                             'SetSecurityKeys',
                             arguments=security_keys)
    ssid = f_connection.call_action(wifi_config, 'GetSSID')
    ssid['NewSSID'] = new_ssid
    f_connection.call_action(wifi_config,
                             'SetSSID',
                             arguments=ssid)


day = datetime.datetime.now().strftime("%A")
guest_ssid = 'Heute ist ' + day + ' ' + emojis[day]
guest_password = "<mypassword>"

devices = [
    FritzConnection(address='192.168.178.1', user='<username>', password='<password>', use_tls=False)
]

for device in devices:
    set_ssid_and_password(device, guest_ssid, guest_password)
