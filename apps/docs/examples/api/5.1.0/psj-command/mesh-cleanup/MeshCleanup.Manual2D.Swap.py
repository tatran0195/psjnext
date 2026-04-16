# Title:   MeshCleanup.Manual2D.Swap()
# Desc:    Swap Element Edge
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Manual2D.Swap
# ---
# Prepare model
Geometry.Part.Cube(ilAxialNodes=[3, 3, 3], iPartColor=7463537)
  # [hl]
MeshCleanup.Manual2D.Swap(crplElemEdge=[CursorPair(Node(17), Node(18))])
