# Title:   Assembly.RightClick.ChangeEdgeColor()
# Desc:    Change the color of the edges of selected part
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assembly/Assembly.RightClick.ChangeEdgeColor
# ---
Geometry.Part.Cube()
JPT.ViewFitToModel()
Assembly.RightClick.ChangeEdgeColor(crlParts=[Part(1)], iColor=12583104)  # [hl]
