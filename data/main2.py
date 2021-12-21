import requests
import json
import xml.etree.ElementTree as ET

HEADERS_XML = {'Content-Type': 'application/xml'}
HEADERS_JSON = {'Content-Type': 'application/json'}

# tree = ET.parse('data/out_save1_bu.xml')
'''tree = ET.parse('data/sample_bu.xml')
root = tree.getroot()
children = list(root)

json_list = []
for c in children:
    json_elem = {"artist": "", "song": "", "genre": "", "language": "", "lyrics": ""}
    fields = list(c)
    json_elem['artist'] = fields[0].text
    json_elem['song'] = fields[1].text
    json_elem['genre'] = fields[2].text
    json_elem['language'] = fields[3].text
    json_elem['lyrics'] = fields[4].text
    json_list.append(json_elem)


for j in json_list:
    add_dict = {"add": j}
    add_dict_json = json.dumps(add_dict)
    r = requests.post('http://localhost:8983/solr/mll/update?commitWithin=1000',
                      data=add_dict_json.encode('utf-8', 'replace'),
                      headers=HEADERS_JSON)
    print(r.status_code)
    print(r.content)

print('Finished')

''''''

{"artist":"Rammstein", "song":"Feuer Frei", "genre":"Metal", "language":"de", "lyrics":"Test Lyrics RAMMSTEIN"}
{"artist": "afi", "song": "miss murder (espanol)", "genre": "Pop", "language": "es", "lyrics": "Eh, Srta"}
'''

with open('data/out_save1_bu.xml', 'r', encoding='utf-8') as file:
    data = file.read().replace('\n', '')

headers = {'Content-Type': 'application/xml'}
# http://localhost:8983/solr/mll/update?_=1640026553865&commitWithin=1000&overwrite=true&wt=json
r = requests.post('http://localhost:8983/solr/mll/update?commitWithin=1000',
                  data=data.encode('utf-8', 'replace'),
                  headers=HEADERS_XML)

print("Response Code: ", r.status_code)
print(r.content)
print('END')
