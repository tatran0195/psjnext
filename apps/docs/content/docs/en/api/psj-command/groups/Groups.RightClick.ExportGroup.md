---
title: "Groups.RightClick.ExportGroup()"
description: "Export specified group to *CSV file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Groups > RightClick > ExportGroup"
macro _link: ""
---

## Description

Export specified group to \*CSV file.

## Syntax

```psj
Groups.RightClick.ExportGroup(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The groups to be exported.

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- The paths of \*CSV files.

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

```psj {19-23}
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

temp _path=JPT.GetAppPathInfo(JPT.PathType.TEMP _PATH)

groups=JPT.GetAllGroups()
for group in groups:
    # Export groups
    Groups.RightClick.ExportGroup(
        crlTargets=[Group(group.id)], 
        strlPaths=[os.path.join(temp _path,f"Group_{group.id}.csv")],
        iEncode=1,
        bWithBOM=True)
```
