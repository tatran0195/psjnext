---
title: "MeshEdit.DeleteNode()"
description: "Delete floating nodes in db"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > DeleteNode"
---

## Description

Delete floating nodes in db

## Syntax

```psj
MeshEdit.DeleteNode(crlNodes=[], bRemoveVertex=True)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @default(\[])

- The node.

### `bRemoveVertex` @type(Boolean) @default(True)

- The remove vertex.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.DeleteNode(crlNodes=[], bRemoveVertex=True)
```
