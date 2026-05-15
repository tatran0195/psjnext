---
title: "Tools.Group.CreateGroup()"
description: "Create a group of arbitrary entities."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Group > CreateGroup"
---

## Description

Create a group of arbitrary entities.

## Syntax

```psj
Tools.Group.CreateGroup(strGroupName, crlTargets=[], crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strGroupName

- Specify the group name.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A _List of Cursor_ specifying the created group.

## Sample Code

```psj {2}
Geometry.Part.Cube(iPartColor=6409934)
created _group = Tools.Group.CreateGroup(strGroupName="Part _Group1", crlTargets=[Part(1)])
for group in created _group:
    JPT.Debugger(JPT.MacroTCursorToDItem(str(group)))
```
