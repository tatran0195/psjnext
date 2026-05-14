---
title: "BoundaryConditions.LBCCopyMisc()"
description: "Copy the loads and boundary conditions set on one part to another part."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > LBCCopyMisc"
---

## Description

Copy the loads and boundary conditions set on one part to another part.

## Syntax

```psj
BoundaryConditions.LBCCopyMisc(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMatchMethod`

- The match method.

<!-- @since:5.0.1 @type:Double List @optional @default:[0,0,0] -->
### `dlTransVec`

- The trans vector.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dTransMag`

- The trans mag.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dTransOffset`

- The trans offset.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dTransTol`

- The trans tolerance.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crTranscrCoord`

- The transcr coordinate.

<!-- @since:5.0.1 @type:Double List @optional @default:[0,0,0] -->
### `dlTransaxisVec`

- The transaxis vector.

<!-- @since:5.0.1 @type:Double List @optional @default:[0,0,0] -->
### `dlTranscenterVec`

- The transcenter vector.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dRotateAngle`

- The rotate angle.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dRotateTol`

- The rotate tolerance.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crRotatecrCoord`

- The rotatecr coordinate.

<!-- @since:5.0.1 @type:Vector List @optional @default:[] -->
### `veclMirrorPoint`

- The mirror point.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMirrordOffset`

- The mirrord offset.

<!-- @since:5.0.1 @type:Double @optional @default:0.1 -->
### `dMirrorTol`

- The mirror tolerance.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.LBCCopyMisc(iMethod=0, iMatchMethod=0, dlTransVec=[0,0,0], dTransMag=0, dTransOffset=0, dTransTol=0, crTranscrCoord=None, dlTransaxisVec=[0,0,0], dlTranscenterVec=[0,0,0], dRotateAngle=0, dRotateTol=0, crRotatecrCoord=None, veclMirrorPoint=[], dMirrordOffset=0, dMirrorTol=0.1, crlTargets=[])
```
