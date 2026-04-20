# Title:   Meshing.LocalSettings.BoltEdge()
# Desc:    Set the mesh setting for bolt edges (Define the settings before surface mesh creation)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/meshing/Meshing.LocalSettings.BoltEdge
# ---
Geometry.Part.Cylinder()
Meshing.LocalSettings.BoltEdge(iCircleDivision=8, crlTargets=[Edge(2, 1)])  # [hl]
