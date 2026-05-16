import json

with open('aune-sagesse-data.js', 'r') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
data = json.loads(json_str)

print("Part 19:", data[19]['title'])
for i, sub in enumerate(data[19]['subparts']):
    print(f"  Subpart {i} ({sub['title']}): {len(sub.get('content', []))} items")
    for item in sub.get('content', []):
        print(f"    {item.get('number', 'None')}")

