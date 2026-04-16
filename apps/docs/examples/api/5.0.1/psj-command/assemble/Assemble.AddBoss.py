# Title:   Assemble.AddBoss()
# Desc:    Add boss shape to specific body as a union part
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assemble/Assemble.AddBoss
# ---
Geometry.Part.Cube()
result = Assemble.AddBoss(crPart=Part(1), iType=1, posOrgCenter=[0, 0.00555556, 0.00555556], vecOrgDirection=[-1.0, 0.0, 0.0], dOrgOuterRadius=1.2)
print(result)
