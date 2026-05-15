---
title: "Exchange.AssembleSolidMesh()"
description: "Assemble solid mesh parts"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Exchange > AssembleSolidMesh"
macro _link: ""
---

## Description

Assemble solid mesh parts.

## Syntax

```psj
Exchange.AssembleSolidMesh(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crNewPart

- Specify the new assembly part.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crlAssembleParts

- Specify the original assembly part.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crlNewFaces

- Specify the face to be shared on the new assembly part.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crlAssembleFaces

- Specify the face to be shared on the original assembly part.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### dTolerance

- Specify the tolerance value.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iConnectPosition

- Specify the position to create the shared face.
  - 0: Mid
  - 1: Mater
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iRemeshLayer

- Specify the number of layers to be remeshed around the new shared face.
- The default value is 2.

<!-- @since:5.1.0 @optional -->
### bRemeshAuto

- Specify whether to set the mesh size automatically.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### dAvg

- Specify the average mesh size.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dMin

- Specify the minimum mesh size.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dMax

- Specify the maximum mesh size.
- The default value is 0.0.

## Return Code

A _Boolean_ specifying the function successfully executed or not.

## Sample Code

```psj {34,35}
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.0101, 0.0, 0.0], strName="Cube _2", iPartColor=14903267)
Meshing.AdjustCircleVertex(crlParts=[Part(2)], bInModeSurfaceMesh=True)
Meshing.SetMeshAttribute(
    crlParts=[Part(2)], 
    surfaceMesh=SURFACE _MESH(
        dAvgElemSize=0.0015,
         dGeomAngle=0.7853981634, 
         iPerformanceMode=1, 
         dAutoMergeTinyFacesAngle=0.5235987756, 
         bGeomApprox=True))
Meshing.SurfaceMeshing(
    crlParts=[Part(2)], 
    surfaceMesh=SURFACE _MESH(
        dAvgElemSize=0.0015, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bGeomApprox=True), 
    iThreadNum=16)
Meshing.SolidMeshing(
    rlParts=[Part(2, 1)], 
    dGradingFactor=1.05, 
    dStretchLimit=0.1, 
    iSpeedVsQual=1, 
    iRegion=1, 
    bSafeMode=False, 
    iParallel=16, 
    bInternalMeshOnly=False, 
    iPartColor=65280)

# Assemble solid mesh
ret = Exchange.AssembleSolidMesh(crNewPart=Part(2), crlAssembleParts=[Part(1)], dTolerance=0.0002, 
    iConnectPosition=1, bRemeshAuto=False, dAvg=0.0012, dMin=0.0001, dMax=0.002)
print(assemble _sretolid)
```
