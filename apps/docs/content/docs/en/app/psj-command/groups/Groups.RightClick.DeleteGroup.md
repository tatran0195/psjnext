---
title: "Groups.RightClick.DeleteGroup()"
description: "Delete specified groups from the Group tree in the Group Window"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Groups > RightClick > DeleteGroup"
---

## Description

Delete specified groups from the Group tree in the Group Window.

## Syntax

```psj
Groups.RightClick.DeleteGroup(...)
```

## Inputs

### `crlGroups` @type(List\[Cursor]) @required

- The list of group items uses for deleting.

### `bRemoveAll` @type(Boolean) @default(False)

- Enable/disable all group deletion.

## Return Code

A _Boolean_ specifying the status of the deleting process:

- _True_: The inputted groups have been deleted successfully.
- _False_: The inputted groups cannot be deleted.

## Sample Code

```psj {8,9}
Geometry.Part.Cube()

Tools.Group.CreateGroup(strGroupName="Group1",
                        crlTargets=[Face(26)])
Tools.Group.CreateGroup(strGroupName="Group2",
                        crlTargets=[Face(24)])

deleted_groups = Groups.RightClick.DeleteGroup(crlGroups=[Group(1,
                                                                2)])

JPT.Debugger(deleted_groups)
```
