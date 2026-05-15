---
title: "Meshing.LocalSettings.BoltEdge()"
description: "Set the mesh setting for bolt edges (Define the settings before surface mesh creation)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Meshing > LocalSettings > BoltEdge"
macro _link: ""
---

## Description

Set the mesh setting for bolt edges (Define the settings before surface mesh creation)

## Syntax

```psj
Meshing.LocalSettings.BoltEdge(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iCircleDivision

- Specify number of division in circumferential direction.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### crlTargets

- Specify the target Edges of the local mesh setting.
- The default value is \[].

## Return Code

A _Cursor_ specifying the created local mesh setting if success, or None if fail.

## Sample Code

```psj {2}
Geometry.Part.Cylinder()
Meshing.LocalSettings.BoltEdge(iCircleDivision=8, crlTargets=[Edge(2, 1)])
```
