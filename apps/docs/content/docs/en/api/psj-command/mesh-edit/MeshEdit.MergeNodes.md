---
title: "MeshEdit.MergeNodes()"
description: "Merge nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > MergeNodes"
---

## Description

Merge nodes

## Syntax

```psj
MeshEdit.MergeNodes(dTolerance=0.01, iKeepType=0, crlTargets=[], bGroup=False, bEquivalence=True)
```

## Inputs

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dTolerance`

- The tolerance.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iKeepType`

- The keep type.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bGroup`

- The group.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bEquivalence`

- The equivalence.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MergeNodes(dTolerance=0.01, iKeepType=0, crlTargets=[], bGroup=False, bEquivalence=True)
```
