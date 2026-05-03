---
title: "Geometry.MakeFacePlanar()"
description: "Flatten curved faces into the planar face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Make Face Planar"
macro_link: "[MakeFacePlanar](../../macro/geometry/MakeFacePlanar)"
---

## Description

This method flattens the curved faces or bumpy faces into planar faces defined by a set of three-nodes.

## Syntax

```psj
Geometry.MakeFacePlanar(dlPlanePt1=[0.0,0.0,0.0], dlPlanePt2=[0.0,0.0,0.0],
    dlPlanePt3=[0.0,0.0,0.0], ilFaceIds=[], iMergeFace=0)
```

## Inputs

### `dlPlanePt1` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- The plane point 1.

### `dlPlanePt2` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- The plane point 2.

### `dlPlanePt3` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- The plane point 3.

### `ilFaceIds` @type(List\[Integer]) @default(\[])

- The target face ids.

### `iMergeFace` @type(Integer) @default(0)

- Whether to merge adjacent faces to each other after the operation. Possible values are 0 and 1.
- I&#x66;_&#x69;MergeFace=0_, do not merge faces after the operation.
- I&#x66;_&#x69;MergeFace=1_, merge faces after the operation.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.Part.Trapezoid(dlOrigin=[0.0005, 0.0005, 0.01], dlLength=[0.005, 0.005, 0.005],
    dTopXLength=3.0, strName="Trapezoid_5", iPartColor=7697908)

Geometry.MakeFacePlanar(dlPlanePt1=[0.01, 0.0, 0.01], dlPlanePt2=[0.01, 0.01, 0.01],
    dlPlanePt3=[0.0, 0.01, 0.01], ilFaceIds=[52, 50, 48, 49, 47])
```
