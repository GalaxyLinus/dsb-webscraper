import dsbdata
import datetime
from datetime import date
import json

# get settings
try:
    with open('settings.json', 'r') as f:
        settings = json.load(f)
        url = settings['url']
        klasse = settings['klasse']
except FileNotFoundError:
    with open('settings.json', 'w') as f:
        f.write('{"url" : "--write-url-here--","klasse" : "--write-class-here--"}')
    print('ERROR: settings.json not found, enter parameters in settings.json')
    quit()

date = dsbdata.dsbdata.getVertretungen(data=dsbdata.dsbdata.getData(url=url, klasse=klasse), klasse=klasse)[1]

days = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']

weekday = days[datetime.datetime.strptime(date, '%d.%m.%Y').weekday()]

output = "\n".join(dsbdata.dsbdata.getVertretungen(data=dsbdata.dsbdata.getData(url=url, klasse=klasse), klasse=klasse)[0])

print(f'Vertretungen für {weekday}, den {date}:\n')
print(output,end='\n\n')

input()