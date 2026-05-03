---
title: "Geometry.RemoveRibBoss()"
description: "Remove Rib or Boss geometry"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Remove Rib/Boss"
---

## Description

This method removes Boss or Rib geometry and replaces it with a smooth face.

## Syntax

```psj
Geometry.RemoveRibBoss(crlFaces, dGradiation=1.0, iContinuity=1)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The adjacent faces around the Rib or Boss geometry. These faces must be connected to each other.

### `dGradiation` @type(Double) @default(1.0)

- The gradation value. It defines the rate at which the mesh transitions between high mesh density and low mesh density for the new smooth face. Possible values are greater than or equal to 0.5.

### `iContinuity` @type(Integer) @default(1)

- The connection continuity factor. It defines the rate at which the smooth shape transition between the bound face and the new smooth face. The possible values tha&#x74;_&#x69;Continuit&#x79;_&#x63;an take are 0, 1, and 2.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube(ilAxialNodes=[11, 11, 11])

Geometry.Edge.Line(dllPoints=[[0.01, 0.01, 0.005], [0, 0.01, 0.005]], crlFaces=[Face(22)])

Geometry.Part.Cylinder(dlOrigin=[0.005, 0.01, 0.005], dTopRadius=0.002, dBottomRadius=0.002,
    dHeight=0.003)

Assemble.BooleanEx([Part(1, 2)])

Geometry.RemoveRibBoss(crlFaces=[Face(35, 37)])
```
