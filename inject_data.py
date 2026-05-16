import json
import re

def main():
    # Read the JS file
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract JSON part
    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    json_str = content[start_idx:end_idx]
    
    try:
        data = json.loads(json_str)
    except Exception as e:
        print("Error parsing JSON:", e)
        return

    # Clear content for Part 19, Subparts 1 and 2
    if len(data) > 19:
        if len(data[19]['subparts']) > 1:
            data[19]['subparts'][1]['content'] = []
        if len(data[19]['subparts']) > 2:
            data[19]['subparts'][2]['content'] = []

    # Clear content for all Parts >= 20
    for i in range(20, 49):
        if i < len(data):
            for sub in data[i]['subparts']:
                sub['content'] = []

    # Inject data
    # (The data will be loaded from a separate JSON file that we will create)
    with open('batch_data.json', 'r', encoding='utf-8') as f:
        new_batch = json.load(f)

    for item in new_batch:
        part_idx = item['part_idx']
        subpart_idx = item['subpart_idx']
        
        if part_idx < len(data) and subpart_idx < len(data[part_idx]['subparts']):
            data[part_idx]['subparts'][subpart_idx]['content'].extend(item['content'])
        else:
            print(f"Warning: Part {part_idx} or Subpart {subpart_idx} not found.")

    # Convert back to JSON
    new_json_str = json.dumps(data, ensure_ascii=False, indent=4)
    
    # Re-assemble the JS file
    new_content = content[:start_idx] + new_json_str + content[end_idx:]
    
    with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Injection complete!")

if __name__ == '__main__':
    main()
