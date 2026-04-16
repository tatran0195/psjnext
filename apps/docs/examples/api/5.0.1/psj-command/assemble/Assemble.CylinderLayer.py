# Title:   Assemble.CylinderLayer()
# Desc:    Create an inner cylindrical face based on specified top face/bottom face of the cylinder
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assemble/Assemble.CylinderLayer
# ---
Geometry.Part.Cylinder(bHollow=True, 
                       dTopInnerRadius=0.007, 
                       dBottomInnerRadius=0.007)
Geometry.Edge.OffsetLine(crlFaces=[Face(5)], 
                         crlEdges=[Edge(2)], 
                         iOffsetMethod=1,
                         dlOffsetDistance=[0.0015], 
                         iImprintMethod=0)

creating_status = Assemble.CylinderLayer(crFace=Face(5), crNode=Node(41))  # [hl]

JPT.Debugger(creating_status)
