---
title: "Geometry.LogoRemoval()"
description: "Removal logos or bolts"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Logo Removal"
macro_link: "[LogoRemoval](../../macro/geometry/LogoRemoval)"
---

## Description

This method is used to automatically remove faces that configure logos or bolts.

## Syntax

```psj
Geometry.LogoRemoval(crlStartFaces, crlStopFaces, iLayers=5, bMergeFaces=False)
```

## Inputs

### `crlStartFaces` @type(List\[Cursor]) @required

- The faces of the logo or bolt to be removed.

### `crlStopFaces` @type(List\[Cursor]) @required

- The faces adjacent to the geometry to be removed.

### `iLayers` @type(Integer) @default(5)

- The number of layers in the depth direction of the target faces when removing bolts.

### `bMergeFaces` @type(Boolean) @default(False)

- Whether the adjacent faces should be merged after the removal operation.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.0045, 0.002, 0.0095], dlLength=[0.001, 0.006, 0.001])

Geometry.Part.Cube(dlOrigin=[0.003, 0.001, 0.0095], dlLength=[0.004, 0.001, 0.001])

Geometry.Part.Cube(dlOrigin=[0.003, 0.008, 0.0095], dlLength=[0.004, 0.001, 0.001])

Assemble.BooleanEx([Part(2, 3, 4)])

Geometry.MergeEntities.Faces(crlFaces=[Face(51, 52, 77, 78, 103, 104)])

Assemble.BooleanEx([Part(1, 2)], iBooleanType=1)

Geometry.LogoRemoval(crlStartFaces=[Face(51)], crlStopFaces=[Face(26)])
```
