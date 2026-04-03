import json

with open(r'd:\Projet_Data_science\exploration_dataset.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print("Total cells in notebook:", len(nb['cells']))

print("\n--- Phase 5 Execution Results ---\n")
for cell in nb['cells']:
    cid = cell.get('id', '?')
    if 'phase5' in str(cid) and cell['cell_type'] == 'code':
        print(f"Cell ID: {cid}")
        for out in cell.get('outputs', []):
            if out.get('output_type') == 'stream':
                print(out.get('text', ''))
            elif out.get('output_type') in ['display_data', 'execute_result']:
                data = out.get('data', {})
                print(f"[Graphical Output: {list(data.keys())}]")
        print("-" * 40)
