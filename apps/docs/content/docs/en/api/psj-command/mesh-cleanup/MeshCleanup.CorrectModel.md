---
title: "MeshCleanup.CorrectModel()"
description: "correct model"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > CorrectModel"
---

## Description

Correct model

## Syntax

```psj
MeshCleanup.CorrectModel(crlParts, iEnableBreakEdge=0, dEdgeAngle=0, iEnableMergeEdge=0, dMergeEdgeAngle=0, iEnableMergePlanarFace=0, iEnableRemoveExtraVertex=0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableBreakEdge`

- The enable break edge.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dEdgeAngle`

- The edge angle.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableMergeEdge`

- The enable merge edge.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMergeEdgeAngle`

- The merge edge angle.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableMergePlanarFace`

- The enable merge planar face.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableRemoveExtraVertex`

- The enable remove extra vertex.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.CorrectModel(crlParts, iEnableBreakEdge=0, dEdgeAngle=0, iEnableMergeEdge=0, dMergeEdgeAngle=0, iEnableMergePlanarFace=0, iEnableRemoveExtraVertex=0)
```
