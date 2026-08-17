import json

# Load both graphs
with open('graphify-out/graph_v2.json', 'r') as f:
    v2 = json.load(f)

with open('graphify-out/graph_v3.json', 'r') as f:
    v3 = json.load(f)

# Extract node IDs
v2_nodes = {n['id'] for n in v2['nodes']}
v3_nodes = {n['id'] for n in v3['nodes']}

# Extract edges (normalized as tuples)
v2_edges = set()
for e in v2.get('links', []):
    v2_edges.add((e['source'], e['target']))

v3_edges = set()
for e in v3.get('links', []):
    v3_edges.add((e['source'], e['target']))

# Compare nodes
added_nodes = v3_nodes - v2_nodes
removed_nodes = v2_nodes - v3_nodes
unchanged_nodes = v2_nodes & v3_nodes

# Compare edges
added_edges = v3_edges - v2_edges
removed_edges = v2_edges - v3_edges
unchanged_edges = v2_edges & v3_edges

print(f"V2: {len(v2_nodes)} nodes, {len(v2_edges)} edges")
print(f"V3: {len(v3_nodes)} nodes, {len(v3_edges)} edges")
print()
print(f"NODES ADDED in V3: {len(added_nodes)}")
print(f"NODES REMOVED in V3: {len(removed_nodes)}")
print(f"NODES UNCHANGED: {len(unchanged_nodes)}")
print()
print(f"EDGES ADDED in V3: {len(added_edges)}")
print(f"EDGES REMOVED in V3: {len(removed_edges)}")
print(f"EDGES UNCHANGED: {len(unchanged_edges)}")

# Show some added nodes
print("\n=== SAMPLE ADDED NODES (V3) ===")
for n in sorted(list(added_nodes))[:50]:
    print(f"  + {n}")

print("\n=== SAMPLE REMOVED NODES (V3) ===")
for n in sorted(list(removed_nodes))[:50]:
    print(f"  - {n}")

# Get node details for added/removed
v2_node_map = {n['id']: n for n in v2['nodes']}
v3_node_map = {n['id']: n for n in v3['nodes']}

print("\n=== ADDED NODES WITH DETAILS ===")
for n_id in sorted(list(added_nodes))[:30]:
    n = v3_node_map[n_id]
    print(f"  + {n['label']} ({n['source_file']}:{n['source_location']})")

print("\n=== REMOVED NODES WITH DETAILS ===")
for n_id in sorted(list(removed_nodes))[:30]:
    n = v2_node_map[n_id]
    print(f"  - {n['label']} ({n['source_file']}:{n['source_location']})")