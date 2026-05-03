---
title: "MeshEdit.SeparateNodes()"
description: "Separate nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > SeparateNodes"
---

## Description

Separate nodes

## Syntax

```psj
MeshEdit.SeparateNodes(crlShareNodes=[], crlTargets=[], iKeepNodeIDsOn=0)
```

## Inputs

### `crlShareNodes` @type(List\[Cursor]) @default(\[])

- The share nodes.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `iKeepNodeIDsOn` @type(Integer) @default(0)

- The keep node i ds on.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.SeparateNodes(crlShareNodes=[], crlTargets=[], iKeepNodeIDsOn=0)
```
