import json

with open(r'd:\Projet_Data_science\exploration_dataset.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")

ids_to_check = ['phase5-pareto-names-code', 'phase5-coh-names-code', 'phase5-grid-names-code']

for cell in nb['cells']:
    cid = cell.get('id', '?')
    if cid in ids_to_check:
        print(f"\n--- Resultats: {cid} ---")
        for out in cell.get('outputs', []):
            if out.get('output_type') == 'stream':
                print(out.get('text', ''))
            elif out.get('output_type') == 'display_data':
                 print(f"[Graphique/Tableau genere: {list(out.get('data', {}).keys())}]")
