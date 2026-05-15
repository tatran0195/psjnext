---
title: "Geometry.AdvancedShellAssembly()"
description: "Advanced Shell Assembly"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Advanced Shell Assembly"
---

## Description

This method connects the given faces between assembly models of multiple shell parts.

## Syntax

```psj
Geometry.AdvancedShellAssembly(crlParts=[], crlFaces=[], iMeshType=0, bSelfIntersection=False,
    iMethod=3, dGapTol=2.1)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the parts to assemble. Either _crlParts_ or _crlFace_ must be specified.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the faces to assemble. Either _crlParts_ or _crlFace_ must be specified.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iMeshType

- Specify the surrounding element type of the connecting region.
- If _iMeshType=0_, the mesh on the face is a triangular primary element.
- If _iMeshType=1_, the mesh on the face is a quadrilateral primary element. The mesh around the assembly edge will be re-meshed into a square mesh.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bSelfIntersection

- Specify whether or not the self-intersecting parts should be assembled.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify how to connect between faces.
- If _iMethod=0_, within the interval threshold, the free edge detects a portion not in contact with the face and stretches the free edge to the face to imprint and connect.
- If _iMethod=1_, connect the edges that exist within the interval threshold.
- If _iMethod=2_, detect face intersections and imprint the edges.
- If _iMethod=3_, the above three patterns are judged automatically. The assembly edges are imprinted and connected appropriately.
- The default value is 3.

<!-- @since:5.0.1 @optional -->
### dGapTol

- Specify the distance to determine that the face and the edge, and the edge and the edge are connected.
- The default value is 2.1.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube(iPartColor=8124407)

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=14441436)

Geometry.AdvancedShellAssembly(crlParts=[Part(2, 1)])
```
