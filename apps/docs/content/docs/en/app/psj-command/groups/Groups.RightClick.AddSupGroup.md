---
title: "Groups.RightClick.AddSupGroup()"
description: "Create a sub group to the Group tree in the Group Window"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Groups > RightClick > AddSupGroup"
---

## Description

Create a sub group to the Group tree in the Group Window.

## Syntax

```psj
Groups.RightClick.AddSupGroup(...)
```

## Inputs

### `crSupGroupSelected` @type(Cursor) @default(None)

- The group to add a sub group onto.

## Return Code

A _Cursor_ specifying the created sub group.

## Sample Code

```psj {1}
created_sub_group = Groups.RightClick.AddSupGroup()

JPT.Debugger(created_sub_group)
```
