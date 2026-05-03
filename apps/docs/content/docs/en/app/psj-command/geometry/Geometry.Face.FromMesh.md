---
title: "Geometry.Face.FromMesh()"
description: "Create a new geometric face from the specified mesh face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Face > Face from Mesh Face"
macro_link: "[CreateFaceFromMeshFace](../../macro/geometry/CreateFaceFromMeshFace)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create geometric face from mesh face","Create a new geometric face from the specified mesh face"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a new part entity containing the new geometric face from the specified mesh face.

## Syntax

```psj
Geometry.Face.FromMesh(...)
```

## Inputs

### `crFace` @type(Cursor) @required

- The mesh face that the new face is created base on.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {3}
Geometry.Part.Cube()

created_face = Geometry.Face.FromMesh(crFace=Face(26))
JPT.Debugger(created_face)
```
