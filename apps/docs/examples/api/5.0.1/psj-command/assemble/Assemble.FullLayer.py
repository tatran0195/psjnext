# Title:   Assemble.FullLayer()
# Desc:    Create a layer (PRISM6 part) with the entire surface mesh of the part offset inward
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assemble/Assemble.FullLayer
# ---
cube = Geometry.Part.Cube()
flag = Assemble.FullLayer(crPart=cube)  # [hl]
JPT.Debugger(flag)
