---
title: "Tools.Coordinates.CylinderFace()"
description: "create Coordinate by Cylinder Face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Coordinates > CylinderFace"
---

## Description

Create Coordinate by Cylinder Face

## Syntax

```psj
Tools.Coordinates.CylinderFace(strName="CRect1", iCoordType=0, crFace=None)
```

## Inputs

### `strName` @type(String) @default("CRect1")

- The name.

### `iCoordType` @type(Integer) @default(0)

- The coordinate type.

### `crFace` @type(Cursor) @default(None)

- The face.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Coordinates.CylinderFace(strName="CRect1", iCoordType=0, crFace=None)
```
