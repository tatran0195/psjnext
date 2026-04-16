# Title:   Groups.RightClick.ExportGroup()
# Desc:    Export specified group to *CSV file.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/groups/Groups.RightClick.ExportGroup
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
for group in groups:
    # Export groups
    Groups.RightClick.ExportGroup(  # [hl:start]
        crlTargets=[Group(group.id)], 
        strlPaths=[os.path.join(temp_path,f"Group_{group.id}.csv")],
        iEncode=1,
        bWithBOM=True)  # [hl:end]
