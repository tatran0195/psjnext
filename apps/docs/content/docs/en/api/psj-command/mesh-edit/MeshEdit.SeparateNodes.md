---
title: "MeshEdit.SeparateNodes()"
description: "Separate nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > SeparateNodes"
---

## Description

Separate nodes

## Syntax

```psj
MeshEdit.SeparateNodes(crlShareNodes=[], crlTargets=[], iKeepNodeIDsOn=0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlShareNodes`

- The share nodes.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iKeepNodeIDsOn`

- The keep node i ds on.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.SeparateNodes(crlShareNodes=[], crlTargets=[], iKeepNodeIDsOn=0)
```
