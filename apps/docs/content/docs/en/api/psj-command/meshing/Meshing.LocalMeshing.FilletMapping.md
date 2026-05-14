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

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The list of target parts to search for fillet faces.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The list of target faces to search for fillet faces.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMinArcLength`

- The minimum length of fillet edge in meter. This is a search criterion.

<!-- @since:5.0.1 @type:Double @optional @default:0.009 -->
### `dMaxArcLength`

- The maximum length of fillet edge in meter. This is a search criterion.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMinArcRadius`

- The minimum radius of fillet edge in meter. This is a search criterion.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dMaxArcRadius`

- The maximum radius of fillet edge in meter. This is a search criterion.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bConvex`

- The to enable (_True_) or disable (_False_) the search for convex fillet.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bConcave`

- The to enable (_True_) or disable (_False_) the search for concave fillet.

<!-- @since:5.0.1 @type:Double @optional @default:30 -->
### `dLayerAngle`

- The angle between each fillet layer in degrees.

<!-- @since:5.0.1 @type:Double @optional @default:3 -->
### `dAxisAspectRatio`

- The ratio of the length to the width of a layer.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dAxisMinSize`

- The minimum size for each dimension of a layer cell, in meter.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bAxisMinSize`

- Whether to use min size criterion or not.

<!-- @since:5.0.1 @type:Double @optional @default:0.003 -->
### `dAxisMaxSize`

- The maximum size for each dimension of a layer cell, in meter.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bAxisMaxSize`

- Whether to use max size criterion or not.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iAxisMinMeshCount`

- The minimum node count on each dimension of every fillet faces. If a fillet faces has a dimension whose node count is less than the criterion, map meshing on the face will be skipped.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bAxisMinMeshCount`

- Whether to use min mesh count criterion or not.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iElementType`

- The type 2D element to be created. It can be one of the following:
  - 0: Tri3.
  - 1: Quad4.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dSingleLayerLength`

- The maximum length of the single layer in meter.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bSingleLayerLength`

- Whether to use single layer length criterion or not.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dSingleLayerRadius`

- The maximum radius of the single layer in meter.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSingleLayerRadius`

- Whether to use single layer radius criterion or not.

<!-- @since:5.0.1 @type:Integer @optional @default:3 -->
### `iMinNumLayer`

- The minimum number of layers to be created.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bMinNumLayer`

- Whether to use single min number of layers criterion or not.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bCreateReference=False`

- Whether to create a reference part after meshing or not.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bRemeshTheEnd`

- Whether to use local remesh for ending position of fillet to fit with surrounding mesh size or not.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSkipComplexFace`

- Whether to skip complex fillet faces or not.

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
