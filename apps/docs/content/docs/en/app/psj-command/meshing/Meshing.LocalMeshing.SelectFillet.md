---
title: "Meshing.LocalMeshing.SelectFillet()"
description: "Select all the existing fillet faces based on the selected entities"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > LocalMeshing > SelectFillet"
---

## Description

Select all the existing fillet faces based on the selected entities.

## Syntax

```psj
Meshing.LocalMeshing.SelectFillet(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The list of target parts to search for fillet faces.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The list of target faces to search for fillet faces.

### `dMinArcLength` @type(Double) @default(0.0)

- The minimum length of fillet edge in meter. This is a search criterion.

### `dMaxArcLength` @type(Double) @default(0.009)

- The maximum length of fillet edge in meter. This is a search criterion.

### `dMinArcRadius` @type(Double) @default(0.0)

- The minimum radius of fillet edge in meter. This is a search criterion.

### `dMaxArcRadius` @type(Double) @default(1.0)

- The maximum radius of fillet edge in meter. This is a search criterion.

### `bConvex` @type(Boolean) @default(True)

- To enable (_True_) or disable (_False_) the search for convex fillet.

### `bConcave` @type(Boolean) @default(True)

- To enable (_True_) or disable (_False_) the search for concave fillet.

## Return Code

A _List of Cursor_ specifying the found fillet faces if succeeded, or None if failed.

## Sample Code

```psj {4,5}
Geometry.Part.Cube()
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])

faces = Meshing.LocalMeshing.SelectFillet(crlParts=[Part(1)], 
                                          crlFaces=[])
                                        
JPT.Debugger(faces)
```
