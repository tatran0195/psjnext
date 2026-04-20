# Title:   Assemble.GeneralLayer()
# Desc:    Create a new face inside the part by offsetting a preceding face
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assemble/Assemble.GeneralLayer
# ---
Geometry.Part.Cube()

creating_status = Assemble.GeneralLayer(crlFaces=[Face(26)])  # [hl]

JPT.Debugger(creating_status)
