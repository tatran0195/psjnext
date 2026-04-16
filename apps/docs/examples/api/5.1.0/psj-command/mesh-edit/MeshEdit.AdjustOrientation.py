# Title:   MeshEdit.AdjustOrientation()
# Desc:    Adjust the orientation (normal direction) of parts, faces, or elements.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.AdjustOrientation
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
MainWindow.RightClick.FlipElement(crlTargets=[Face(26)])
MainWindow.RightClick.FlipElement(crlTargets=[Elem(699, 702, 684, 701)])

# Adjust orientation
MeshEdit.AdjustOrientation(crlParts=[Part(1)], crlElems=[Elem(322)])

