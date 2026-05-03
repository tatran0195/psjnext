---
title: "MeshCleanup.CorrectModel()"
description: "correct model"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > CorrectModel"
---

## Description

Correct model

## Syntax

```psj
MeshCleanup.CorrectModel(crlParts, iEnableBreakEdge=0, dEdgeAngle=0, iEnableMergeEdge=0, dMergeEdgeAngle=0, iEnableMergePlanarFace=0, iEnableRemoveExtraVertex=0)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The part.

### `iEnableBreakEdge` @type(Integer) @default(0)

- The enable break edge.

### `dEdgeAngle` @type(Double) @default(0)

- The edge angle.

### `iEnableMergeEdge` @type(Integer) @default(0)

- The enable merge edge.

### `dMergeEdgeAngle` @type(Double) @default(0)

- The merge edge angle.

### `iEnableMergePlanarFace` @type(Integer) @default(0)

- The enable merge planar face.

### `iEnableRemoveExtraVertex` @type(Integer) @default(0)

- The enable remove extra vertex.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.CorrectModel(crlParts, iEnableBreakEdge=0, dEdgeAngle=0, iEnableMergeEdge=0, dMergeEdgeAngle=0, iEnableMergePlanarFace=0, iEnableRemoveExtraVertex=0)
```
