---
title: "HexModeling.Curve()"
description: "Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) along a specified curve."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > Curve"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["make hex by sweeping curve","Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) along a specified curve."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Hexahedral and pentahedral elements are created by sweeping a surface mesh (composed of triangular and quadrilateral first-order elements) along a specified curve.

## Syntax

```psj
HexModeling.Curve(...)
```

## Inputs

### `crFace` @type(Cursor) @default(None)

- The face.

### `crlEdges` @type(List\[Cursor]) @default(\[])

- The edge.

### `crlRefEdge` @type(List\[Cursor]) @default(\[])

- The reference edge.

### `dMeshSize` @type(Double) @default(0.1)

- The mesh size.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {28}
Geometry.Part.Cube()
Geometry.Bar.Spline(crlNodes=[Node(1, 8, 7)], strName="Bar_2")
Geometry.Part.Cylinder(dTopOuterRadius=0.001, dBottomOuterRadius=0.001, iPartColor=6409934)

Geometry.DeleteEntity.Face(crlFaces=[Face(32, 34)])
Geometry.DeleteEntity.Part(crlParts=[Part(1)])

Meshing.SetMeshAttribute(crlParts=[Part(3)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.002, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, bGeomApprox=True, 
        iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(
    crlParts=[Part(3)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.002, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

HexModeling.Curve(crFace=Face(33), crlEdges=[Edge(27)], dMeshSize=0.002)
```
