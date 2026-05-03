---
title: "BoundaryConditions.LBCCopyMisc()"
description: "Copy the loads and boundary conditions set on one part to another part."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > LBCCopyMisc"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Copy the loads and boundary conditions set on one part to another part."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Copy the loads and boundary conditions set on one part to another part.

## Syntax

```psj
BoundaryConditions.LBCCopyMisc(...)
```

## Inputs

### `iMethod` @type(Integer) @default(0)

- The method.

### `iMatchMethod` @type(Integer) @default(0)

- The match method.

### `dlTransVec` @type(Double List) @default(\[0,0,0])

- The trans vector.

### `dTransMag` @type(Double) @default(0)

- The trans mag.

### `dTransOffset` @type(Double) @default(0)

- The trans offset.

### `dTransTol` @type(Double) @default(0)

- The trans tolerance.

### `crTranscrCoord` @type(Cursor) @default(None)

- The transcr coordinate.

### `dlTransaxisVec` @type(Double List) @default(\[0,0,0])

- The transaxis vector.

### `dlTranscenterVec` @type(Double List) @default(\[0,0,0])

- The transcenter vector.

### `dRotateAngle` @type(Double) @default(0)

- The rotate angle.

### `dRotateTol` @type(Double) @default(0)

- The rotate tolerance.

### `crRotatecrCoord` @type(Cursor) @default(None)

- The rotatecr coordinate.

### `veclMirrorPoint` @type(Vector List) @default(\[])

- The mirror point.

### `dMirrordOffset` @type(Double) @default(0)

- The mirrord offset.

### `dMirrorTol` @type(Double) @default(0.1)

- The mirror tolerance.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopyMisc(iMethod=0, iMatchMethod=0, dlTransVec=[0,0,0], dTransMag=0, dTransOffset=0, dTransTol=0, crTranscrCoord=None, dlTransaxisVec=[0,0,0], dlTranscenterVec=[0,0,0], dRotateAngle=0, dRotateTol=0, crRotatecrCoord=None, veclMirrorPoint=[], dMirrordOffset=0, dMirrorTol=0.1, crlTargets=[])
```
