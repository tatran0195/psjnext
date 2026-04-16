# Title:   Assemble.AddRib()
# Desc:    Add the ribs to the body as a union part
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assemble/Assemble.AddRib
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0025, 0.01, 0.005], dlLength=[0.005, 0.01, 0.002], strName="Cube_4", iPartColor=15429611)
result = Assemble.AddRib(crPart=Part(1), crlFaces=[Face(47)], dWidth=0.01)
print(result)
