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

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bRemoveVertex

- Specify the remove vertex.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.DeleteNode(crlNodes=[], bRemoveVertex=True)
```
