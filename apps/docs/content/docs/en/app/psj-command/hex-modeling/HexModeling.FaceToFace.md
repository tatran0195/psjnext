---
title: "HexModeling.FaceToFace()"
description: "Hexahedral and pentahedral elements are automatically generated for complex-shaped parts that have two opposing identical geometries, like gears."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > FaceToFace"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Hexahedral and pentahedral elements are automatically generated for complex-shaped parts that have two opposing identical geometries, like gears.

## Syntax

```psj
HexModeling.FaceToFace(...)
```

## Inputs

### `crSrcFace` @type(Cursor) @required

- The source face.

### `crDstFace` @type(Cursor) @required

- The dst face.

### `bDeleteOriginalParts` @type(Boolean) @default(True)

- The delete original parts.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {35}
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2", iPartColor=6409934)
Geometry.Transform.Rotation(crlParts=[Part(2)], 
                            posCenter=[0.005, 0.005, 0.005], 
                            vecAxis=[0.0, 0.0, 0.001], 
                            dAngle=0.523599, dTol=1e-05)
Geometry.DeleteEntity.Face(crlFaces=[Face(21, 22, 23, 24, 47, 48, 49, 50, 52, 25)])

Geometry.MergeEntities.Parts(crlParts=[Part(1, 2)], dMergeTolerance=1e-05)
Geometry.Face.Edges(crlEdges=[Edge(20, 38)])
Geometry.Face.Edges(crlEdges=[Edge(19, 37)])
Geometry.Face.Edges(crlEdges=[Edge(18, 36)])
Geometry.Face.Edges(crlEdges=[Edge(17, 35)])

Meshing.SetMeshAttribute(crlParts=[Part(1)], 
                        surfaceMesh=SURFACE_MESH(
                        dAvgElemSize=0.002, 
                        dGeomAngle=0.7853981634, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bOutputQuadMesh=True, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0))

Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                    surfaceMesh=SURFACE_MESH(
                        dAvgElemSize=0.002, 
                        dGeomAngle=0.7853981634, 
                        iPerformanceMode=1, 
                        dAutoMergeTinyFacesAngle=0.5235987756, 
                        bOutputQuadMesh=True, 
                        bGeomApprox=True, 
                        iNextEntityOffsetId=0))
                
HexModeling.FaceToFace(crSrcFace=Face(26), crDstFace=Face(51))
```
