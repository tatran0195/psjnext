---
title: "MeshEdit.MoveNode.ProjectToLine()"
description: "move node by project to line"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MoveNode > ProjectToLine"
---

## Description

Move node by project to line

## Syntax

```psj
MeshEdit.MoveNode.ProjectToLine(crlRefNodes=[], crlObjNodes=[], iType=0)
```

## Inputs

### `crlRefNodes` @type(List\[Cursor]) @default(\[])

- The reference nodes.

### `crlObjNodes` @type(List\[Cursor]) @default(\[])

- The object nodes.

### `iType` @type(Integer) @default(0)

- The type.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MoveNode.ProjectToLine(crlRefNodes=[], crlObjNodes=[], iType=0)
```
