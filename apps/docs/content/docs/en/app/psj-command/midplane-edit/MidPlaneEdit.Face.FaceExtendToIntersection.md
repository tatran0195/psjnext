---
title: "MidPlaneEdit.Face.FaceExtendToIntersection()"
description: "Face Extend To Intersection"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlaneEdit > Face > FaceExtendToIntersection"
---

## Description

Face Extend To Intersection

## Syntax

```psj
MidPlaneEdit.Face.FaceExtendToIntersection(crEdge0, crEdge1)
```

## Inputs

### `crEdge0` @type(Cursor) @required

- The edge0.

### `crEdge1` @type(Cursor) @required

- The edge1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.Face.FaceExtendToIntersection(crEdge0, crEdge1)
```
