---
title: "Meshing.LocalMeshing.FilletMapping()"
description: "Select and mesh all the existing fillet faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > LocalMeshing > FilletMapping"
---

## Description

Select and mesh all the existing fillet faces.

## Syntax

```psj
Meshing.LocalMeshing.FilletMapping(...)
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

### `dLayerAngle` @type(Double) @default(30)

- The angle between each fillet layer in degrees.

### `dAxisAspectRatio` @type(Double) @default(3)

- The ratio of the length to the width of a layer.

### `dAxisMinSize` @type(Double) @default(0.001)

- The minimum size for each dimension of a layer cell, in meter.

### `bAxisMinSize` @type(Boolean) @default(True)

- Whether to use min size criterion or not.

### `dAxisMaxSize` @type(Double) @default(0.003)

- The maximum size for each dimension of a layer cell, in meter.

### `bAxisMaxSize` @type(Boolean) @default(True)

- Whether to use max size criterion or not.

### `iAxisMinMeshCount` @type(Integer) @default(1)

- The minimum node count on each dimension of every fillet faces. If a fillet faces has a dimension whose node count is less than the criterion, map meshing on the face will be skipped.

### `bAxisMinMeshCount` @type(Boolean) @default(True)

- Whether to use min mesh count criterion or not.

### `iElementType` @type(Integer) @default(0)

- The type 2D element to be created. It can be one of the following:
  - 0: Tri3.
  - 1: Quad4.

### `dSingleLayerLength` @type(Double) @default(0.001)

- The maximum length of the single layer in meter.

### `bSingleLayerLength` @type(Boolean) @default(True)

- Whether to use single layer length criterion or not.

### `dSingleLayerRadius` @type(Double) @default(0.001)

- The maximum radius of the single layer in meter.

### `bSingleLayerRadius` @type(Boolean) @default(False)

- Whether to use single layer radius criterion or not.

### `iMinNumLayer` @type(Integer) @default(3)

- The minimum number of layers to be created.

### `bMinNumLayer` @type(Boolean) @default(True)

- Whether to use single min number of layers criterion or not.

### `bCreateReference=False` @type(Boolean) @default(True)

- Whether to create a reference part after meshing or not.

### `bRemeshTheEnd` @type(Boolean) @default(False)

- Whether to use local remesh for ending position of fillet to fit with surrounding mesh size or not.

### `bSkipComplexFace` @type(Boolean) @default(False)

- Whether to skip complex fillet faces or not.

## Return Code

A _List of Cursor_ specifying the meshed fillet faces, or None if failed.

## Sample Code

```psj {8,9}
Geometry.Part.Cube()
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])

fillet_faces = Meshing.LocalMeshing.SelectFillet(crlParts=[Part(1)], 
                                                 crlFaces=[])

fillet_meshing = \
Meshing.LocalMeshing.FilletMapping(crlFaces=[Face(*[int(str(_).split(":")[-1].strip()) 
                                                    for _ in fillet_faces])])

JPT.Debugger(fillet_meshing)
```
