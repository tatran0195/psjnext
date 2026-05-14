---
title: "Tools.Coordinates.CylinderFace()"
description: "create Coordinate by Cylinder Face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > Coordinates > CylinderFace"
---

## Description

Create Coordinate by Cylinder Face

## Syntax

```psj
Tools.Coordinates.CylinderFace(strName="CRect1", iCoordType=0, crFace=None)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"CRect1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCoordType`

- The coordinate type.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crFace`

- The face.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Coordinates.CylinderFace(strName="CRect1", iCoordType=0, crFace=None)
```
