# Title:   MeshCleanup.Manual2D.SplitElement.TriTo4Tris()
# Desc:    Convert a single triangle element into four triangular elements.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Manual2D.SplitElement.TriTo4Tris
# ---
# Prepare model
Geometry.Part.Cube(ilAxialNodes=[3, 3, 3], iPartColor=7463537)

# Devide Triangle Element 76 into 4 smaller trianbles.  # [hl]
MeshCleanup.Manual2D.SplitElement.TriTo4Tris(crlElems=[Elem(76)], iMethod=8, iAutoExecute=1, iMergeNode=1)
