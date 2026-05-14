---
title: "Meshing.LocalMeshing.SelectFillet()"
description: "Select all the existing fillet faces based on the selected entities"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > LocalMeshing > SelectFillet"
---

## Description

Select all the existing fillet faces based on the selected entities.

## Syntax

```psj
Meshing.LocalMeshing.SelectFillet(...)
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
