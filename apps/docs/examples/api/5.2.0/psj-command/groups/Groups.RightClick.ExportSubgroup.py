# Title:   Groups.RightClick.ExportSubGroup()
# Desc:    Export specified subgroup to folder and *CSV file
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/groups/Groups.RightClick.ExportSubgroup
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)

Groups.RightClick.AddSubGroup()

Assembly.RightClick.Rename(strNewName="SubGroup1", crItem=SubGroup(1))

Tools.Group.CreateGroup(
    strGroupName="Group1", 
    crlTargets=[Face(26, 24)])
JPT.ViewFitToModel()

Tools.Group.CreateGroup(
    strGroupName="Group2", 
    crlTargets=[Node(45, 46, 100, 101, 102, 145, 146, 153, 154)])

Groups.RightClick.CopyGroup(crlGroups=[Group(1, 2)], crSubGroup=SubGroup(1))

temp_path=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)

subgroups=JPT.GetAllSubGroups()
for subgroup in subgroups:
    # Export subgroups
    Groups.RightClick.ExportSubGroup(  # [hl:start]
        strFolderPath=temp_path,
        crlSubGroups=[SubGroup(1)],
        iEncode=1,
        bWithBOM=True)    # [hl:end]
