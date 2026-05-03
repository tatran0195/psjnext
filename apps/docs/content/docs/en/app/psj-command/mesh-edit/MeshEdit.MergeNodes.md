---
title: "MeshEdit.MergeNodes()"
description: "Merge nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > MergeNodes"
---

## Description

Merge nodes

## Syntax

```psj
MeshEdit.MergeNodes(dTolerance=0.01, iKeepType=0, crlTargets=[], bGroup=False, bEquivalence=True)
```

## Inputs

### `dTolerance` @type(Double) @default(0.01)

- The tolerance.

### `iKeepType` @type(Integer) @default(0)

- The keep type.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `bGroup` @type(Boolean) @default(False)

- The group.

### `bEquivalence` @type(Boolean) @default(True)

- The equivalence.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshEdit.MergeNodes(dTolerance=0.01, iKeepType=0, crlTargets=[], bGroup=False, bEquivalence=True)
```
