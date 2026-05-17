import json

def find():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    for p_idx, part in enumerate(data):
        title = part.get('title', '')
        if 'fléaux' in title.lower() and '35' in title:
            print(f"Found Part: {title} at Index {p_idx}")
            for s_idx, subpart in enumerate(part.get('subparts', [])):
                print(f"  Subpart {s_idx}: {subpart.get('title', '')}")
                for h in subpart.get('hadiths', []):
                    print(f"    - {h['number']}")

if __name__ == '__main__':
    find()
