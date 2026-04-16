# Title:   Assemble.AddRibEx.Curve()
# Desc:    Specify multiple points to define the path of the rib and the attachment surface, and add the rib shape to the existing surface mesh.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assemble/Assemble.AddRibEx.Curve
# ---
Geometry.Part.Cube()

Assemble.AddRibEx.Curve(  # [hl:start]
  dOffsetX=2.22222e-06, 
  dOffsetY=1.11111e-06, 
  dOffsetZ=1e-05, 
  dlPositions=[
    [0.002222222222222222, 0.001111111111111111, 0.01], 
    [0.005555555555555556, 0.003333333333333333, 0.01], 
    [0.006666666666666666, 0.006666666666666666, 0.01], 
    [0.003333333333333333, 0.008888888888888889, 0.01]], 
    crlFaces=[Face(26)])  # [hl:end]
