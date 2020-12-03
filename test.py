import urllib.request, urllib.parse, urllib.error
import json

serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'


address=input('Enter location: ')


print('Retrieving URL')

url=serviceurl+urllib.parse.urlencode({'address':address})
urlh=urllib.request.urlopen(url)
data=urlh.read().decode()

print(data)

#try:
#    js=json.loads(data)
#except:
#    js=None

#if not js or 'status' not in js or js['status']!='ok':
#    print ('Failure to retrieve')
#    print(data)
#    continue
