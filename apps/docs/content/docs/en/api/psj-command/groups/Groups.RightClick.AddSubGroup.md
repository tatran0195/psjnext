---
title: "Groups.RightClick.AddSubGroup()"
description: "Create a sub group to the Group tree in the Group Window"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Groups > RightClick > AddSubGroup"
---

## Description

Create a sub group to the Group tree in the Group Window.

## Syntax

```psj
Groups.RightClick.AddSubGroup(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crSubGroupSelected`

- The master subgroup to add a sub group onto.

## Return Code

A _Cursor_ specifying the created sub group.

## Sample Code

```psj {9}
# Prepare model
Geometry.Part.Cube()

# Create groups
Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Face(26)])
Tools.Group.CreateGroup(strGroupName="Group2", crlTargets=[Face(24)])

# Add subgroups
created _sub _group = Groups.RightClick.AddSubGroup()
Assembly.RightClick.Rename(strNewName="SubGroup - 1", crItem=SubGroup(1))
JPT.Debugger(created _sub _group)
```
