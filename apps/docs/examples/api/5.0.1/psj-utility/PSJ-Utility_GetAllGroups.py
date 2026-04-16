# Title:   JPT.GetAllGroups()
# Desc:    Get all the information of all existing groups
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetAllGroups
# ---
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Part(1)])
Tools.Group.CreateGroup(strGroupName="Group2", crlTargets=[Face(47, 48, 49, 50, 51, 52)])
Tools.Group.CreateGroup(strGroupName="Group3", crlTargets=[Elem(2784, 2296, 2677, 2295, 3144, 2977)])
JPT.ViewFitToModel()

# Get the information of all existing groups
listDGroups = JPT.GetAllGroups()  # [hl]
JPT.Debugger(listDGroups)

# Print all the related information of each existing group in list
for group in listDGroups:
    JPT.Debugger(group)
