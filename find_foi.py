import json
import sys

def find():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    for p_idx, part in enumerate(data):
        for s_idx, subpart in enumerate(part.get('subparts', [])):
            title = subpart.get('title', '')
            if 'degrés de la foi' in title.lower():
                print(f"Found at Part Index {p_idx}, Subpart Index {s_idx}, Title: {title}")
                # check existing hadiths
                for h in subpart.get('hadiths', []):
                    print(f"  - Hadith: {h['number']}")
                return

if __name__ == '__main__':
    find()
