# Title:   Connections.Pretension.SunShine()
# Desc:    Create bolt pretension for the SunShine solver
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.Pretension.SunShine
# ---
Geometry.Part.Cylinder(dTopOuterRadius=0.003, dBottomOuterRadius=0.003, iPartColor=7697908)
Geometry.Part.Cylinder(strName="Cylinder_2", dlOrigin=[0.0, 0.01, 0.0], dTopOuterRadius=0.003, dBottomOuterRadius=0.003, iPartColor=7463537)
Meshing.SetMeshAttribute(crlParts=[Part(1, 2)], surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0))
Meshing.SurfaceMeshing(crlParts=[Part(1, 2)], surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634, iPerformanceMode=1, dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0))

#Pretension SunShine
Connections.Pretension.SunShine(dForceValue=123.0, crlTargets=[Part(1, 2)])  # [hl]
