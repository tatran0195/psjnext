---
title: "Geometry.MergeEntities.PartFaces()"
description: "Merge Faces in Part"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Merge Entities > Part Faces"
---

## Description

This method merges adjacent faces of the given part by recursively finding adjacent faces that are at an angle of less than or equal to the specified angle or face width is not greater than the specified value. The operation will ignore the specified preserved faces.

## Syntax

```psj
Geometry.MergeEntities.PartFaces(crlParts=[], crlFaces=[], bAngle=True, dTolAngle=20, bWidth=True,
    dTolWidth=0.2)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The target parts that faces need merging belong to.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The preserved faces not to be merged.

### `bAngle` @type(Boolean) @default(True)

- Whether to find the adjacent faces by face angle.

### `dTolAngle` @type(Double) @default(20.0)

- The maximum allowable angle between two adjacent faces. I&#x66;_&#x62;Angl&#x65;_&#x69;s specified, the adjacent faces that are at an angle of less than or equal to will be merged.

### `bWidth` @type(Boolean) @default(True)

- Whether to find the adjacent faces by face width.

### `dTolWidth` @type(Double) @default(0.2)

- The maximum allowable face width. I&#x66;_&#x62;Widt&#x68;_&#x69;s specified, the faces that have a width less than or equal to will be merged to an adjacent face.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Trapezoid(dTopXLength=5.0)

Geometry.MergeEntities.PartFaces(crlParts=[Part(1)], dTolAngle=89.0, bWidth=False)
```
