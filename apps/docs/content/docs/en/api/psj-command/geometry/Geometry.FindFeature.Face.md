---
title: "Geometry.FindFeature.Face()"
description: "Find and select the specific faces according to their characteristic"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > FindFeature > Faces"
---

## Description

Find and select the specific faces according to their characteristic.

## Syntax

```psj
Geometry.FindFeature.Face(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The parts to find the specific faces.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFaceType`

- The specific type of Faces.
  - If _iFaceType=0_, find and select the faces that are bounded by four corners.
  - If _iFaceType=1_, find and select the planar faces.
  - If _iFaceType=2_, find and select the faces of the cylindrical surface.
  - If _iFaceType=3_, find and select the faces of the semi-cylindrical surface.
  - If _iFaceType=4_, find and select the disk-shaped faces.
  - If _iFaceType=5_, find and select the faces of map mesh.
  - If _iFaceType=6_, find and select the circular chamfer faces.
  - If _iFaceType=7_, find and select the fillet faces.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bCylinder`

- Whether to find cylinder face of map mesh. This argument is to be used if _iOption=5_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDisc`

- Whether to find disk-shaped face of map mesh. This argument is to be used if _iOption=5_.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bFourCorners`

- Whether to find the faces that are bounded by four corners of map mesh. This argument is to be used if _iFaceType=5_.

<!-- @since:5.0.1 @type:Double @optional @default:0.1 -->
### `dMinThickness`

- The minimum thickness of the circular chamfer surface. This argument is to be used if _iFaceType=6_.

<!-- @since:5.0.1 @type:Double @optional @default:2.0 -->
### `dMaxThickness`

- The maximum thickness of the circular chamfer surface. This argument is to be used if _iFaceType=6_.

## Return Code

A _List cursor_ of faces if success, or _None_ if fail.

## Sample Code

```psj {2}
cube = Geometry.Part.Cube()
faces = Geometry.FindFeature.Face(crlParts=[cube])
JPT.Debugger(faces)
```
