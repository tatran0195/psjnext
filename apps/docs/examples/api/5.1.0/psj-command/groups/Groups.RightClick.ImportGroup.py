# Title:   Groups.RightClick.ImportGroup()
# Desc:    Create a group to the Group tree in the Group Window by importing a *CSV file
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/groups/Groups.RightClick.ImportGroup
# ---
import os 

# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Tools.Group.CreateGroup(
    strGroupName="Group1", 
    crlTargets=[Face(26, 24)])
JPT.ViewFitToModel()

Tools.Group.CreateGroup(
    strGroupName="Group2", 
    crlTargets=[Node(45, 46, 100, 101, 102, 145, 146, 153, 154)])

temp_path=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)

groups=JPT.GetAllGroups()

max_group_num=len(groups)
for i, group in enumerate(groups):
    # Export groups
    Groups.RightClick.ExportGroup(
        crlTargets=[Group(group.id)], 
        strlPaths=[os.path.join(temp_path,f"Group_{i}.csv")],
        iEncode=1,
        bWithBOM=True)
    # Delete the group
    Groups.RightClick.DeleteGroup(crlGroups=[Group(group.id)])

# Re-import groups
for i in range(max_group_num):  # [hl:start]
    Groups.RightClick.ImportGroup(
        strlPaths=[os.path.join(temp_path,f"Group_{i}.csv")])  # [hl:end]
