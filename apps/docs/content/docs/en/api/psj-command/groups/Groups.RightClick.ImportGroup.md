---
title: "Groups.RightClick.ImportGroup()"
description: "Create a group to the Group tree in the Group Window by importing a *CSV file"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Groups > RightClick > ImportGroup"
macro _link: ""
---

## Description

Create a group to the Group tree in the Group Window by importing a \*CSV file.

## Syntax

```psj
Groups.RightClick.ImportGroup(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @required -->
### `strlPaths`

- The path to \*CSV files.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crParentGroup`

- The parent sub group (SUP\_GROUP) to import.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: Import the group successfully.
  - _False_: Cannot import the group.

## Sample Code

```psj {30-32}
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

max _group _num=len(groups)
for i, group in enumerate(groups):
    # Export groups
    Groups.RightClick.ExportGroup(
        crlTargets=[Group(group.id)], 
        strlPaths=[os.path.join(temp _path,f"Group_{i}.csv")],
        iEncode=1,
        bWithBOM=True)
    # Delete the group
    Groups.RightClick.DeleteGroup(crlGroups=[Group(group.id)])

# Re-import groups
for i in range(max _group _num):
    Groups.RightClick.ImportGroup(
        strlPaths=[os.path.join(temp _path,f"Group_{i}.csv")])
```
