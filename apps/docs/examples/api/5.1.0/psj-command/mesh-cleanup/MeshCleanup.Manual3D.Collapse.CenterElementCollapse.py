# Title:   MeshCleanup.Manual3D.Collapse.CenterElementCollapse()
# Desc:    Collapse the selected element towards the center of its element and connect the surrounding elements
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-cleanup/MeshCleanup.Manual3D.Collapse.CenterElementCollapse
# ---
Geometry.Part.Cube(iPartColor=6409934)
Meshing.SolidMeshing(crlParts=[Part(1)], 
                    dGradingFactor=1.05, 
                    dStretchLimit=0.1, 
                    iSpeedVsQual=1, 
                    iRegion=1, 
                    bSafeMode=False, 
                    iParallel=16, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)
MeshCleanup.Manual3D.Collapse.CenterCollapse(crlElems=[Elem(8756)])  # [hl]
