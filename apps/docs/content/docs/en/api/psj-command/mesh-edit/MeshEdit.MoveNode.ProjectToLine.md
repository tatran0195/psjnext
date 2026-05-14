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

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlRefNodes`

- The reference nodes.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlObjNodes`

- The object nodes.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.ProjectToLine(crlRefNodes=[], crlObjNodes=[], iType=0)
```
