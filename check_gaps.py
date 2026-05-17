import json
import re

def check():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    all_numbers = []
    
    # Extract all numbers
    for p_idx, part in enumerate(data):
        for s_idx, subpart in enumerate(part.get('subparts', [])):
            for h in subpart.get('hadiths', []):
                num_str = h.get('number', '').strip()
                if num_str.isdigit():
                    all_numbers.append(int(num_str))
                else:
                    # handle non digit or empty
                    match = re.search(r'\d+', num_str)
                    if match:
                        all_numbers.append(int(match.group()))

    # Sort and find gaps
    all_numbers.sort()
    
    if not all_numbers:
        print("No hadiths found.")
        return

    expected = 1
    gaps = []
    
    for num in all_numbers:
        if num > expected:
            gaps.append((expected, num - 1))
        expected = num + 1

    print(f"Total hadiths parsed: {len(all_numbers)}")
    print(f"Max hadith number: {max(all_numbers)}")
    print("Identified gaps in numbering:")
    for start, end in gaps:
        if start == end:
            print(f"Missing: {start}")
        else:
            print(f"Missing: {start} to {end}")

    # Check for duplicates
    duplicates = set([x for x in all_numbers if all_numbers.count(x) > 1])
    if duplicates:
        print(f"Duplicates found: {sorted(list(duplicates))}")
    else:
        print("No duplicates found.")

if __name__ == '__main__':
    check()
