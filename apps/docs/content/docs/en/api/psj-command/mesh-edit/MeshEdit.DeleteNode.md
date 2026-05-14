---
title: "MeshEdit.DeleteNode()"
description: "Delete floating nodes in db"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > DeleteNode"
---

## Description

Delete floating nodes in db

## Syntax

```psj
MeshEdit.DeleteNode(crlNodes=[], bRemoveVertex=True)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The node.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bRemoveVertex`

- The remove vertex.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.DeleteNode(crlNodes=[], bRemoveVertex=True)
```
