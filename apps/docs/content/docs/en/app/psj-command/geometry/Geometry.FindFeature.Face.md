---
title: "Geometry.FindFeature.Face()"
description: "Find and select the specific faces according to their characteristic"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > FindFeature > Faces"
---

## Description

Find and select the specific faces according to their characteristic.

## Syntax

```psj
Geometry.FindFeature.Face(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The parts to find the specific faces.

### `iFaceType` @type(Integer) @default(0)

- The specific type of Faces.
  - I&#x66;_&#x69;FaceType=0_, find and select the faces that are bounded by four corners.
  - I&#x66;_&#x69;FaceType=1_, find and select the planar faces.
  - I&#x66;_&#x69;FaceType=2_, find and select the faces of the cylindrical surface.
  - I&#x66;_&#x69;FaceType=3_, find and select the faces of the semi-cylindrical surface.
  - I&#x66;_&#x69;FaceType=4_, find and select the disk-shaped faces.
  - I&#x66;_&#x69;FaceType=5_, find and select the faces of map mesh.
  - I&#x66;_&#x69;FaceType=6_, find and select the circular chamfer faces.
  - I&#x66;_&#x69;FaceType=7_, find and select the fillet faces.

### `bCylinder` @type(Boolean) @default(True)

- Whether to find cylinder face of map mesh. This argument is to be used i&#x66;_&#x69;Option=5_.

### `bDisc` @type(Boolean) @default(False)

- Whether to find disk-shaped face of map mesh. This argument is to be used i&#x66;_&#x69;Option=5_.

### `bFourCorners` @type(Boolean) @default(True)

- Whether to find the faces that are bounded by four corners of map mesh. This argument is to be used i&#x66;_&#x69;FaceType=5_.

### `dMinThickness` @type(Double) @default(0.1)

- The minimum thickness of the circular chamfer surface. This argument is to be used i&#x66;_&#x69;FaceType=6_.

### `dMaxThickness` @type(Double) @default(2.0)

- The maximum thickness of the circular chamfer surface. This argument is to be used i&#x66;_&#x69;FaceType=6_.

## Return Code

A _List cursor_ of faces if success, or _None_ if fail.

## Sample Code

```psj {2}
cube = Geometry.Part.Cube()
faces = Geometry.FindFeature.Face(crlParts=[cube])
JPT.Debugger(faces)
```
