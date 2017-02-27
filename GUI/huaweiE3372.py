import urllib.request
import xmltodict

url = "http://192.168.8.1/"

def signal():
    signalurl = "api/device/signal/"
    signallist = get(signalurl)
    rsrq = signallist['response']['rsrq']
    rsrp = signallist['response']['rsrp']
    rssi = signallist['response']['rssi']
    sinr = signallist['response']['sinr']
    return rsrq, rsrp, rssi, sinr


def get(item):
    xml = urllib.request.urlopen(url + item).read()
    return xmltodict.parse(xml)

