---
title: "Groups.RightClick.ExportSubGroup()"
description: "Export specified subgroup to folder and *CSV file"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Groups > RightClick > ExportSubGroup"
macro _link: ""
---

## Description

Export specified subgroup to folder and \*CSV file.

## Syntax

```psj
Groups.RightClick.ExportSubGroup(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### strFolderPath

- Specify the path of folder to save files.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### crlSubGroups

- Specify the subgroup to be exported.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crlGroups

- Specify the groups to be exported.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iEncode

- Specify encoding type.
  - -1: None
  - 0: UTF-8
  - 1: SHIFT-JIS
- The default value is -1.

<!-- @since:5.1.0 @optional -->
### bWithBOM

- Specify whether or not include BOM for UTF-8 format.
- The default value is _False_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: Export the group successfully.
  - _False_: Cannot export the group.

## Sample Code

```psj {24-28}
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

temp _path=JPT.GetAppPathInfo(JPT.PathType.TEMP _PATH)

subgroups=JPT.GetAllSubGroups()
for subgroup in subgroups:
    # Export subgroups
    Groups.RightClick.ExportSubGroup(
        strFolderPath=temp _path,
        crlSubGroups=[SubGroup(1)],
        iEncode=1,
        bWithBOM=True)
```
