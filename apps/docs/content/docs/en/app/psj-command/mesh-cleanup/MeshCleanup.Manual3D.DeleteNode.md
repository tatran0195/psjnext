---
title: "MeshCleanup.Manual3D.DeleteNode()"
description: "remove node for solid element."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > Manual3D > DeleteNode"
---

## Description

Remove node for solid element.

## Syntax

```psj
MeshCleanup.Manual3D.DeleteNode(crlNodes)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @required

- The node.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.DeleteNode(crlNodes)
```
