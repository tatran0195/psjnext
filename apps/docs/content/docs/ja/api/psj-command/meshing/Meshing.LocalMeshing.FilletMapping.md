---
title: "Meshing.LocalMeshing.FilletMapping()"
description: "Select and mesh all the existing fillet faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > LocalMeshing > FilletMapping"
---

## Description

Select and mesh all the existing fillet faces.

## Syntax

```psj
Meshing.LocalMeshing.FilletMapping(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the list of target parts to search for fillet faces.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the list of target faces to search for fillet faces.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dMinArcLength

- Specify the minimum length of fillet edge in meter. This is a search criterion.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMaxArcLength

- Specify the maximum length of fillet edge in meter. This is a search criterion.
- The default value is 0.009.

<!-- @since:5.0.1 @optional -->
### dMinArcRadius

- Specify the minimum radius of fillet edge in meter. This is a search criterion.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMaxArcRadius

- Specify the maximum radius of fillet edge in meter. This is a search criterion.
- The default value is 1.0.

### `bConvex`

- A _Boolean_ to enable (_True_) or disable (_False_) the search for convex fillet.
- The default value is _True_.

### `bConcave`

- A _Boolean_ to enable (_True_) or disable (_False_) the search for concave fillet.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### dLayerAngle

- Specify the angle between each fillet layer in degrees.
- The default value is 30.

<!-- @since:5.0.1 @optional -->
### dAxisAspectRatio

- Specify the ratio of the length to the width of a layer.
- The default value is 3.

<!-- @since:5.0.1 @optional -->
### dAxisMinSize

- Specify the minimum size for each dimension of a layer cell, in meter.
- The default value is 0.001

<!-- @since:5.0.1 @optional -->
### bAxisMinSize

- Specify whether to use min size criterion or not.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### dAxisMaxSize

- Specify the maximum size for each dimension of a layer cell, in meter.
- The default value is 0.003.

<!-- @since:5.0.1 @optional -->
### bAxisMaxSize

- Specify whether to use max size criterion or not.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### iAxisMinMeshCount

- Specify the minimum node count on each dimension of every fillet faces. If a fillet faces has a dimension whose node count is less than the criterion, map meshing on the face will be skipped.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### bAxisMinMeshCount

- Specify whether to use min mesh count criterion or not.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### iElementType

- Specify the type 2D element to be created. It can be one of the following:
  - 0: Tri3.
  - 1: Quad4.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSingleLayerLength

- Specify the maximum length of the single layer in meter.
- The default value is 0.001.

<!-- @since:5.0.1 @optional -->
### bSingleLayerLength

- Specify whether to use single layer length criterion or not.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### dSingleLayerRadius

- Specify the maximum radius of the single layer in meter.
- The default value is 0.001.

<!-- @since:5.0.1 @optional -->
### bSingleLayerRadius

- Specify whether to use single layer radius criterion or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iMinNumLayer

- Specify the minimum number of layers to be created.
- The default value is 3.

<!-- @since:5.0.1 @optional -->
### bMinNumLayer

- Specify whether to use single min number of layers criterion or not.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bCreateReference=False

- Specify whether to create a reference part after meshing or not.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bRemeshTheEnd

- Specify whether to use local remesh for ending position of fillet to fit with surrounding mesh size or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bSkipComplexFace

- Specify whether to skip complex fillet faces or not.
- The default value is _False_.

## Return Code

A _List of Cursor_ specifying the meshed fillet faces, or None if failed.

## Sample Code

```psj {8,9}
Geometry.Part.Cube()
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])

fillet _faces = Meshing.LocalMeshing.SelectFillet(crlParts=[Part(1)], 
                                                 crlFaces=[])

fillet _meshing = \
Meshing.LocalMeshing.FilletMapping(crlFaces=[Face(*[int(str(_).split(":")[-1].strip()) 
                                                    for _ in fillet _faces])])

JPT.Debugger(fillet _meshing)
```
