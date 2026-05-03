---
title: "Groups.RightClick.Rename()"
description: "Rename the specified group in the Group tree of the Group Window"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Groups > RightClick > Rename"
---

## Description

Rename the specified group in the Group tree of the Group Window.

## Syntax

```psj
Groups.RightClick.Rename(...)
```

## Inputs

### `strNewName` @type(String) @required

- The new name of the group to be renamed.

### `crItem` @type(Cursor) @required

- The current group to be renamed.

## Return Code

A _Boolean_ specifying the status of the deleting process:

- _True_: The name of the inputted group has been changed successfully.
- _False_: The name of the inputted group cannot be changed.

## Sample Code

```psj {5}
Geometry.Part.Cube()

Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Part(1)])

rename_status = Groups.RightClick.Rename(strNewName = "new name", crItem = Group(1))

JPT.Debugger(rename_status)
```
