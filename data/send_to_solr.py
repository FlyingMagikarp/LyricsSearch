from time import sleep
import requests


HEADERS_XML = {'Content-Type': 'application/xml'}

# FILE = 'data/out_save1_bu.xml'
# FILE = 'data/out_utf8_bu1.xml'
# FILE = 'data/out_utf8.xml'
# FILE = 'data/test.xml'
FILES = [
    'data/out.xml_0',
    'data/out.xml_1',
    'data/out.xml_2',
    'data/out.xml_3',
    'data/out.xml_4',
    'data/out.xml_5',
    'data/out.xml_6',
    'data/out.xml_7',
    'data/out.xml_8',
    'data/out.xml_9'
]

headers = {'Content-Type': 'application/xml'}

for f in FILES:
    sleep(1)
    with open(f, 'r', encoding='utf-8') as file:
        data = file.read().replace('\n', '')

    # http://localhost:8983/solr/mll/update?_=1640026553865&commitWithin=1000&overwrite=true&wt=json
    r = requests.post('http://localhost:8983/solr/mll/update?commitWithin=1000',
                      data=data.encode('utf-8', 'replace'),
                      headers=HEADERS_XML)

    print('SENDING FILE', f)
    print("Response Code: ", r.status_code)
    print(r.content)
    print('SENT FILE', f)
    print('----------')
