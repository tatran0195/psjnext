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
