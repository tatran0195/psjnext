# Title:   MeshCleanup.Manual2D.CreateElement()
# Desc:    Create a Tri/Quad element
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Manual2D.CreateElement
# ---
Geometry.Part.Cube(iPartColor=6409934)
MeshCleanup.Manual2D.DeleteElement(crlElems=[Elem(1028)])
element = MeshCleanup.Manual2D.CreateElement(crParentEntity=Face(26),   # [hl:start]
                                            crlNodes=[Node(470, 469, 461)])  # [hl:end]
JPT.Debugger(element)
