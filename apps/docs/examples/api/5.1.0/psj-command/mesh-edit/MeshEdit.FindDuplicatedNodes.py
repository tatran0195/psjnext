# Title:   MeshEdit.FindDuplicatedNodes()
# Desc:    Find nodes with overlapping positions.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.FindDuplicatedNodes
# ---
# Preapre model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(
    dlLength=[0.0105, 0.011, 0.01], 
    strName="Cube_2", 
    iPartColor=7961077)

# Find duplication
dupnodes=MeshEdit.FindDuplicatedNodes(  # [hl:start]
    crlTargets=[Part(1, 2)], 
    bSelect=True)  # [hl:end]

print(f"{len(dupnodes)} nodes are duplicated")
print(f"nodes' id:{[i.getID() for i in dupnodes]}")
