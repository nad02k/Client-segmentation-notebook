import json

with open(r'd:\Projet_Data_science\exploration_dataset.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print("Total cells:", len(nb['cells']))

target_ids = ['phase5-grid', 'phase5-redo-pareto', 'phase5-redo-coherence']

for cell in nb['cells']:
    cid = cell.get('id', '?')
    if cid in target_ids:
        print(f"\n--- Cell: {cid} ---")
        for out in cell.get('outputs', []):
            if out.get('output_type') == 'stream':
                print(out.get('text', ''))
            elif out.get('output_type') in ['display_data', 'execute_result']:
                print(f"[Plot Data: {list(out.get('data', {}).keys())}]")
