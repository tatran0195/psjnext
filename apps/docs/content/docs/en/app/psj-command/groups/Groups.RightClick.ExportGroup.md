---
title: "Groups.RightClick.ExportGroup()"
description: "Export specified group to *CSV file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Groups > RightClick > ExportGroup"
macro_link: ""
---

## Description

Export specified group to \*CSV file.

## Syntax

```psj
Groups.RightClick.ExportGroup(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The groups to be exported.

### `strlPaths` @type(List\[String]) @required

- The paths of \*CSV files.

### `iEncode` @type(Integer) @default(-1)

- Encoding type.
  - -1: None
  - 0: UTF-8
  - 1: SHIFT-JIS

### `bWithBOM` @type(Boolean) @default(False)

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

temp_path=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)

groups=JPT.GetAllGroups()
for group in groups:
    # Export groups
    Groups.RightClick.ExportGroup(
        crlTargets=[Group(group.id)], 
        strlPaths=[os.path.join(temp_path,f"Group_{group.id}.csv")],
        iEncode=1,
        bWithBOM=True)
```
