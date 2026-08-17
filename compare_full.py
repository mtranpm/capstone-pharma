import json

with open('graphify-out/graph_v2.json', 'r') as f:
    v2 = json.load(f)

with open('graphify-out/graph_v3.json', 'r') as f:
    v3 = json.load(f)

v2_nodes = {n['id']: n for n in v2['nodes']}
v3_nodes = {n['id']: n for n in v3['nodes']}

v2_ids = set(v2_nodes.keys())
v3_ids = set(v3_nodes.keys())

removed = v2_ids - v3_ids
added = v3_ids - v2_ids

print("=== ALL REMOVED NODES (V2 -> V3) ===")
for n_id in sorted(removed):
    n = v2_nodes[n_id]
    print(f"  - {n['label']} ({n['source_file']}:{n['source_location']}) [id={n_id}]")

print("\n=== ALL ADDED NODES (V2 -> V3) ===")
for n_id in sorted(added):
    n = v3_nodes[n_id]
    print(f"  + {n['label']} ({n['source_file']}:{n['source_location']}) [id={n_id}]")