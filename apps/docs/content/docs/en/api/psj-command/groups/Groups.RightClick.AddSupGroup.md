---
title: "Groups.RightClick.AddSupGroup()"
description: "Create a sub group to the Group tree in the Group Window"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Groups > RightClick > AddSupGroup"
---

## Description

Create a sub group to the Group tree in the Group Window.

## Syntax

```psj
Groups.RightClick.AddSupGroup(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crSupGroupSelected`

- The group to add a sub group onto.

## Return Code

A _Cursor_ specifying the created sub group.

## Sample Code

```psj {1}
created _sub _group = Groups.RightClick.AddSupGroup()

JPT.Debugger(created _sub _group)
```
