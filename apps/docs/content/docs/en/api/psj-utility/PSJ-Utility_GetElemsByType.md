---
title: "JPT.GetElemsByType()"
description: "Get a list of elements by inputting their type (Tri3, Hex8, Tet10, etc.)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get a _List of Elements_ by inputting their type (Tri3, Hex8, Tet10, etc.).

## Syntax

```psj
JPT.GetElemsByType(ElemType)
```

## Inputs

<!-- @since:5.0.1 @type:ElemType @required -->
### `ElemType`

- The _[ElemType](../data-type/psj-command/element-types)_ of elements in Jupiter.

## Return Code

An _[ElemVector](../data-type/psj-utility/pre-utility/built-in-types/ElemVector)_ object or _List of [DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ objects containing all the information of the related elements having the element type is the same as the inputted element type.

## Sample Code

```psj {77-84}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube _2",
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                   strName="Cube _3",
                   iPartColor=13259210)
Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0],
                   strName="Cube _4",
                   iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0],
                   strName="Cube _5",
                   iPartColor=7463537)
Geometry.Part.Cube(dlOrigin=[0.05, 0.0, 0.0],
                   strName="Cube _6",
                   iPartColor=7434735)
Geometry.Part.Cube(dlOrigin=[0.06, 0.0, 0.0],
                   strName="Cube _7",
                   iPartColor=14903267)
Geometry.Part.Cube(dlOrigin=[0.07, 0.0, 0.0],
                   strName="Cube _8",
                   iPartColor=15658599)

Meshing.SetMeshAttribute(crlParts=[Part(5, 6, 7, 8)],
                         surfaceMesh=SURFACE _MESH(dGeomAngle=0.7853981634,
                                                  iPerformanceMode=1,
                                                  dAutoMergeTinyFacesAngle=0.5235987756,
                                                  bOutputQuadMesh=True,
                                                  bGeomApprox=True,
                                                  iNextEntityOffsetId=0))
Meshing.SurfaceMeshing(crlParts=[Part(5, 6, 7, 8)],
                       surfaceMesh=SURFACE _MESH(dGeomAngle=0.7853981634,
                                                iPerformanceMode=1,
                                                dAutoMergeTinyFacesAngle=0.5235987756,
                                                bOutputQuadMesh=True,
                                                bGeomApprox=True,
                                                iNextEntityOffsetId=0),
                                                iThreadNum=12)
MeshEdit.SurfaceMesh(crlParts=[Part(2, 4, 8, 6)])
Meshing.SolidMeshing(crlParts=[Part(8, 4, 7, 3)],
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)
Meshing.SolidMeshing(crlParts=[Part(4)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)

del _faces = [208, 182, 178, 204, 206, 177, 203, 179, 205, 180]
extrude _faces = [207, 181]

Geometry.DeleteEntity.Face(crlFaces=[Face(*del _faces)])

HexModeling.Linear(crlFaces=[Face(*extrude _faces)],
                   dLength=0.01,
                   iLayer=2,
                   vecSweepDirection=[0.0,
                                      0.0,
                                      1.0],
                   iLinearMethod=4)

MeshEdit.SolidMesh(crlParts=[Part(8)])
JPT.ViewFitToModel()

listTri3Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE _TRI3)
listTri6Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE _TRI6)
listTet4Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE _TET4)
listTet10Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE _TET10)
listQuad4Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE _QUAD4)
listQuad8Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE _QUAD8)
listHex8Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE _HEX8)
listHex20Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE _HEX20)

JPT.Debugger(listTri3Elems)
JPT.Debugger(listTri6Elems)
JPT.Debugger(listTet4Elems)
JPT.Debugger(listTet10Elems)
JPT.Debugger(listQuad4Elems)
JPT.Debugger(listQuad8Elems)
JPT.Debugger(listHex8Elems)
JPT.Debugger(listHex20Elems)
```
