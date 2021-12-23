import json
import requests
import datetime


def score_query(obj):
    query = obj.get('query')

    request_url = URL_PREFIX + query + URL_SUFFIX

    r = requests.get(request_url)
    content = r.json().get('response')

    docs = content.get('docs')
    exp = obj.get('expected')
    for i, d in enumerate(docs):
        if d.get('artist') == exp.get('artist') and d.get('song') == exp.get('song'):
            obj.update({'score': obj.get('score') + i+1})
            break
        elif i+1 == content.get('numFound'):
            obj.update({'score': obj.get('score') + 10})

    return obj


URL_PREFIX = 'http://localhost:8983/solr/mll/select?q.op=OR&q='
URL_SUFFIX = '&rows=10'

f = open('gold_standard/gold_standard.json')
query_list = json.load(f)

total_score = 0
total_queries = 0
scored_list = []
for q in query_list:
    obj = query_list.get(q)
    obj_scored = score_query(obj)
    total_queries += 1
    total_score += obj_scored.get('score')
    scored_list.append(obj_scored)

now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
with open('gold_standard/scored_list_'+now+'.json', 'w') as fout:
    json.dump(scored_list, fout)

print('----------')
print('Saved score to ' + str('gold_standard/scored_list_'+now+'.json'))
print('----------')
print('Scored ' + str(total_queries) + ' queries')
print('Total Score: ' + str(total_score))
print('Avg. Score: ' + str(total_score/total_queries))
print('----------')

print('End')
# 'http://localhost:8983/solr/mll/select?q.op=OR&q=lyrics:(*I\'m about to break*) AND artist:(**) AND genre:(**)&rows=10'
