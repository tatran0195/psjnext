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

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strFolderPath`

- The path of folder to save files.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlSubGroups`

- The subgroup to be exported.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlGroups`

- The groups to be exported.

<!-- @since:5.1.0 @type:Integer @optional @default:-1 -->
### `iEncode`

- The encoding type.
  - -1: None
  - 0: UTF-8
  - 1: SHIFT-JIS

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bWithBOM`

- Whether or not include BOM for UTF-8 format.

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
