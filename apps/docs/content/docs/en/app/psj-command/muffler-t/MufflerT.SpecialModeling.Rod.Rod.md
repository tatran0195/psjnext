---
title: "MufflerT.SpecialModeling.Rod.Rod()"
description: "create rod"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MufflerT > SpecialModeling > Rod > Rod"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create rod

## Syntax

```psj
MufflerT.SpecialModeling.Rod.Rod(...)
```

## Inputs

### `crlNodes` @type(List\[Cursor]) @required

- The node.

### `dRadius` @type(Double) @required

- The radius.

### `iType` @type(Integer) @required

- The type.

### `dMeshSize` @type(Double) @required

- The mesh size.

### `dStartDist` @type(Double) @required

- The start dist.

### `dWeldDist` @type(Double) @required

- The weld dist.

### `iDivNumber` @type(Integer) @required

- The divide number.

### `dDeformWidth` @type(Double) @required

- The deformation width.

### `iTransitionElem` @type(Integer) @required

- The transition element.

### `dlPosDir` @type(Double List) @required

- The position direction.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MufflerT.SpecialModeling.Rod.Rod(crlNodes, dRadius, iType, dMeshSize, dStartDist, dWeldDist, iDivNumber, dDeformWidth, iTransitionElem, dlPosDir)
```
