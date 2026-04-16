# Title:   Connections.RigidWall()
# Desc:    Define a rigid wall contact setting to simulate impact analyses with planar rigid walls
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.RigidWall
# ---
Geometry.Part.Cube(iPartColor=16053365)
created_wall = Connections.RigidWall(crlTargets=[Face(24)])  # [hl]
JPT.Debugger(created_wall)
