# Title:   Connections.Plot()
# Desc:    Create 1D plot connection
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/connections/Connections.Plot
# ---
Geometry.Part.Cube()
created_connection = Connections.Plot(crlTargets=[Edge(18)])  # [hl]
JPT.Debugger(created_connection)
