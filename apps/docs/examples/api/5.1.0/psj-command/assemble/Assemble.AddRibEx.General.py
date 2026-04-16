# Title:   Assemble.AddRibEx.General()
# Desc:    Add rib part on a part.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assemble/Assemble.AddRibEx.General
# ---
Geometry.Part.Cube()
Assemble.AddRibEx.General(  # [hl:start]
    dlPositions=[
        [0.007777777777777778, 0.003333333333333333, 0.01], 
        [0.002222222222222222, 0.007777777777777778, 0.01]], 
    crlFaces=[Face(26)], 
    dThickness=0.001, 
    dHeight=0.001)  # [hl:end]
