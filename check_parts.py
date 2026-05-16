import json

with open('aune-sagesse-data.js', 'r') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
data = json.loads(json_str)

for i in range(19, 49):
    if i < len(data):
        print(f"Part {i}: {data[i]['title']}")
        for j, sub in enumerate(data[i]['subparts']):
            print(f"  Subpart {j}: {sub['title']} ({len(sub.get('content', []))} items)")

