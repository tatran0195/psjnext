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

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the part.

<!-- @since:5.0.1 @optional -->
### iEnableBreakEdge

- Specify the enable break edge.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dEdgeAngle

- Specify the edge angle.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableMergeEdge

- Specify the enable merge edge.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMergeEdgeAngle

- Specify the merge edge angle.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableMergePlanarFace

- Specify the enable merge planar face.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableRemoveExtraVertex

- Specify the enable remove extra vertex.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.CorrectModel(crlParts, iEnableBreakEdge=0, dEdgeAngle=0, iEnableMergeEdge=0, dMergeEdgeAngle=0, iEnableMergePlanarFace=0, iEnableRemoveExtraVertex=0)
```
