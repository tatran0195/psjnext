---
title: "MeshCleanup.Manual3D.DeleteNode()"
description: "remove node for solid element."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual3D > DeleteNode"
---

## Description

Remove node for solid element.

## Syntax

```psj
MeshCleanup.Manual3D.DeleteNode(crlNodes)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlNodes`

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.DeleteNode(crlNodes)
```
