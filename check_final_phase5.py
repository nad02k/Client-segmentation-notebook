import json

with open(r'd:\Projet_Data_science\exploration_dataset.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")

ids = ['phase51-coherence', 'phase52-pareto', 'phase52-coherence', 'phase5-grid-manual']

for cell in nb['cells']:
    cid = cell.get('id', '?')
    if cid in ids:
        print(f"\n--- Cell Results: {cid} ---")
        for out in cell.get('outputs', []):
            if out.get('output_type') == 'stream':
                print(out.get('text', ''))
            elif out.get('output_type') == 'display_data':
                 print(f"[Plot Data: {list(out.get('data', {}).keys())}]")
