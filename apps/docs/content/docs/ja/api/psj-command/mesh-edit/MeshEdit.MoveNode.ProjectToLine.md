---
title: "MeshEdit.MoveNode.ProjectToLine()"
description: "move node by project to line"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MoveNode > ProjectToLine"
---

## Description

Move node by project to line

## Syntax

```psj
MeshEdit.MoveNode.ProjectToLine(crlRefNodes=[], crlObjNodes=[], iType=0)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlRefNodes

- Specify the reference nodes.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlObjNodes

- Specify the object nodes.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iType

- Specify the type.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.ProjectToLine(crlRefNodes=[], crlObjNodes=[], iType=0)
```
