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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "CRect1".

<!-- @since:5.0.1 @optional -->
### iCoordType

- Specify the coordinate type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crFace

- Specify the face.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Coordinates.CylinderFace(strName="CRect1", iCoordType=0, crFace=None)
```
