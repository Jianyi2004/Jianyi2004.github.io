from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
from urllib.parse import parse_qs, urlparse

def normalize_scholar_id(value: str) -> str:
    value = value.strip()
    if value.startswith('http://') or value.startswith('https://'):
        query = parse_qs(urlparse(value).query)
        value = query.get('user', [''])[0]
    if not value:
        raise ValueError('GOOGLE_SCHOLAR_ID must be a Google Scholar user id or profile URL')
    return value

google_scholar_id = normalize_scholar_id(os.environ['GOOGLE_SCHOLAR_ID'])
author: dict = scholarly.search_author_id(google_scholar_id)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
