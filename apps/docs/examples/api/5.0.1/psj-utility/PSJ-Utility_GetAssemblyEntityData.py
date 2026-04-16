# Title:   JPT.GetAssemblyEntityData()
# Desc:    Get information from Assembly Tree
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetAssemblyEntityData
# ---
# Prepare model
JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_1", 7105764, 0:0)')
JPT.Exec('CreateCube([0.02, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_2", 6409934, 0:0)')
JPT.Exec('CreateCube([0, 0.02, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_3", 13259210, 0:0)')
JPT.Exec('PressureGeneral("Pressure2", 1e+08, 0, 0:0, 0, 0, 0:0, "", 0:0, [1.7976931e+308, 1.7976931e+308, 1.7976931e+308], "", "", "", 1, [6:52], 0:0)')
JPT.Exec('ForceGeneral("Force2", [-100, 1.7976931e+308, 1.7976931e+308], [1.7976931e+308, 1.7976931e+308, 1.7976931e+308], 0, 0, 0:0, 0:0, 0:0, 0, 0, 0:0, "", "", "", "", "", "", [6:23], 0:0)')
JPT.Exec('FixedConstraint("Constraint1", 7, 0:0, 0, 0, 0:0, 0, [6:77], 0:0)')
JPT.Exec('BoundaryTemperature("BoundaryTemperature_1", 293.15, 0:0, [6:78], 0:0)')
JPT.ViewFitToModel()

# Get information of Cube_1 from assembly tree
PartDict = JPT.GetAssemblyEntityData(JPT.DItemType.BODY, 1)  # [hl]

# Dump out result
pprint(PartDict)

# Print out the color of Feature Edge and convert to RGB format
colorRGB = JPT.ConvertJPTColorToRGB(int(PartDict["Part"]["Surface"]["Colors"]["Feature Edge"]))  # [hl]
print("Feature Edge Color: " + colorRGB)

# Get information of Boundary Constraint from assembly tree
ConstraintDict = JPT.GetAssemblyEntityData(JPT.DItemType.LBC_CONSTRAINT, 1)  # [hl]
pprint(ConstraintDict)

# Get information of Force from assembly tree
ForceDict = JPT.GetAssemblyEntityData(JPT.DItemType.LBC_FORCE, 2)  # [hl]
pprint(ForceDict)

# Get information of Pressure from assembly tree
PressureDict = JPT.GetAssemblyEntityData(JPT.DItemType.LBC_G_PRESSURE, 1)  # [hl]
pprint(PressureDict)

# Get information of Pressure from assembly tree
TempDict = JPT.GetAssemblyEntityData(JPT.DItemType.LBC_TEMP_BOUNDARY, 1)  # [hl]
pprint(TempDict)
