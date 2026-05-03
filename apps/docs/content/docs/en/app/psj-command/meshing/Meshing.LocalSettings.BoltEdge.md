---
title: "Meshing.LocalSettings.BoltEdge()"
description: "Set the mesh setting for bolt edges (Define the settings before surface mesh creation)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Meshing > LocalSettings > BoltEdge"
macro_link: ""
---

## Description

Set the mesh setting for bolt edges (Define the settings before surface mesh creation)

## Syntax

```psj
Meshing.LocalSettings.BoltEdge(...)
```

## Inputs

### `iCircleDivision` @type(Integer) @default(0)

- Number of division in circumferential direction.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target Edges of the local mesh setting.

## Return Code

A _Cursor_ specifying the created local mesh setting if success, or None if fail.

## Sample Code

```psj {2}
Geometry.Part.Cylinder()
Meshing.LocalSettings.BoltEdge(iCircleDivision=8, crlTargets=[Edge(2, 1)])
```
