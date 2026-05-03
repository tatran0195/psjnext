---
title: "Geometry.ShowAdjacent.Faces()"
description: "Expand the selection in all directions, regardless of the shape of surrounding features or the angle at which objects are joined. It obtained by recursively finding adjacent faces at an angle of less than or equal to the specified angle"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Show Adjacent > Faces"
---

## Description

Expand the selection in all directions, regardless of the shape of surrounding features or the angle at which objects are joined.
It obtained by recursively finding adjacent faces at an angle of less than or equal to the specified angle.

## Syntax

```psj
Geometry.ShowAdjacent.Faces(...)
```

## Inputs

### `dAngle` @type(Double) @default(0.0)

- The angle between elements in degree. The adjacent faces that are at an angle of less than or equal t&#x6F;_&#x64;Angl&#x65;_&#x77;ill be selected.

### `bIncludeStopFaces` @type(Boolean) @default(False)

- Whether to add the stop faces to the selection list or not.

### `iNumOfLayers` @type(Integer) @default(1)

- The number of adjacent layers to be searched.

### `crlStartFaces` @type(List\[Cursor]) @default(\[])

- A sequence of start faces.

### `crlStopFaces` @type(List\[Cursor]) @default(\[])

- A sequence of stop faces.

## Return Code

A _List of Cursor_ specifying a sequence of adjacent faces.

## Sample Code

```psj {2}
Geometry.Part.Cube()
adjacent_faces = Geometry.ShowAdjacent.Faces(dAngle=0, iNumOfLayers=100, crlStartFaces=[Face(26)])
JPT.Debugger(adjacent_faces)
```
