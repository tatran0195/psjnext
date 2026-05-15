---
title: "MufflerT.SpecialModeling.Rod.Rod()"
description: "create rod"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MufflerT > SpecialModeling > Rod > Rod"
---

## Description

Create rod

## Syntax

```psj
MufflerT.SpecialModeling.Rod.Rod(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlNodes

- Specify the node.

<!-- @since:5.0.1 @required -->
### dRadius

- Specify the radius.

<!-- @since:5.0.1 @required -->
### iType

- Specify the type.

<!-- @since:5.0.1 @required -->
### dMeshSize

- Specify the mesh size.

<!-- @since:5.0.1 @required -->
### dStartDist

- Specify the start dist.

<!-- @since:5.0.1 @required -->
### dWeldDist

- Specify the weld dist.

<!-- @since:5.0.1 @required -->
### iDivNumber

- Specify the divide number.

<!-- @since:5.0.1 @required -->
### dDeformWidth

- Specify the deformation width.

<!-- @since:5.0.1 @required -->
### iTransitionElem

- Specify the transition element.

<!-- @since:5.0.1 @required -->
### dlPosDir

- Specify the position direction.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerT.SpecialModeling.Rod.Rod(crlNodes, dRadius, iType, dMeshSize, dStartDist, dWeldDist, iDivNumber, dDeformWidth, iTransitionElem, dlPosDir)
```
