---
title: "Geometry.AdvancedShellAssembly()"
description: "Advanced Shell Assembly"
version_introduced: "5.0.1"
available_versions: "all"
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

### `crlParts` @type(List\[Cursor]) @default(\[])

- The parts to assemble. Eithe&#x72;_&#x63;rlPart&#x73;_&#x6F;&#x72;_&#x63;rlFac&#x65;_&#x6D;ust be specified.

### `crlFaces` @type(List\[Cursor]) @default(\[])

- The faces to assemble. Eithe&#x72;_&#x63;rlPart&#x73;_&#x6F;&#x72;_&#x63;rlFac&#x65;_&#x6D;ust be specified.

### `iMeshType` @type(Integer) @default(0)

- The surrounding element type of the connecting region.
- I&#x66;_&#x69;MeshType=0_, the mesh on the face is a triangular primary element.
- I&#x66;_&#x69;MeshType=1_, the mesh on the face is a quadrilateral primary element. The mesh around the assembly edge will be re-meshed into a square mesh.

### `bSelfIntersection` @type(Boolean) @default(False)

- Whether or not the self-intersecting parts should be assembled.

### `iMethod` @type(Integer) @default(3)

- How to connect between faces.
- I&#x66;_&#x69;Method=0_, within the interval threshold, the free edge detects a portion not in contact with the face and stretches the free edge to the face to imprint and connect.
- I&#x66;_&#x69;Method=1_, connect the edges that exist within the interval threshold.
- I&#x66;_&#x69;Method=2_, detect face intersections and imprint the edges.
- I&#x66;_&#x69;Method=3_, the above three patterns are judged automatically. The assembly edges are imprinted and connected appropriately.

### `dGapTol` @type(Double) @default(2.1)

- The distance to determine that the face and the edge, and the edge and the edge are connected.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube(iPartColor=8124407)

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=14441436)

Geometry.AdvancedShellAssembly(crlParts=[Part(2, 1)])
```
