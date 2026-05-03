---
title: "Tools.Group.CreateGroup()"
description: "Create a group of arbitrary entities."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Group > CreateGroup"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Create a group of arbitrary entities."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a group of arbitrary entities.

## Syntax

```psj
Tools.Group.CreateGroup(strGroupName, crlTargets=[], crEdit=None)
```

## Inputs

### `strGroupName` @type(String) @required

- The group name.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A _List of Cursor_ specifying the created group.

## Sample Code

```psj {2}
Geometry.Part.Cube(iPartColor=6409934)
created_group = Tools.Group.CreateGroup(strGroupName="Part_Group1", crlTargets=[Part(1)])
for group in created_group:
    JPT.Debugger(JPT.MacroTCursorToDItem(str(group)))
```
