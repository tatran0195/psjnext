---
title: "Exchange.AssembleSolidMesh()"
description: "Assemble solid mesh parts"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Exchange > AssembleSolidMesh"
macro_link: ""
---

## Description

Assemble solid mesh parts.

## Syntax

```psj
Exchange.AssembleSolidMesh(...)
```

## Inputs

### `crNewPart` @type(Cursor) @default(None)

- The new assembly part.

### `crlAssembleParts` @type(List\[Cursor]) @default(\[])

- The original assembly part.

### `crlNewFaces` @type(List\[Cursor]) @default(\[])

- The face to be shared on the new assembly part.

### `crlAssembleFaces` @type(List\[Cursor]) @default(\[])

- The face to be shared on the original assembly part.

### `dTolerance` @type(Double) @default(0.0)

- The tolerance value.

### `iConnectPosition` @type(Integer) @default(0)

- The position to create the shared face.
  - 0: Mid
  - 1: Mater

### `iRemeshLayer` @type(Integer) @default(2)

- The number of layers to be remeshed around the new shared face.

### `bRemeshAuto` @type(Boolean) @default(True)

- Whether to set the mesh size automatically.

### `dAvg` @type(Double) @default(0.0)

- The average mesh size.

### `dMin` @type(Double) @default(0.0)

- The minimum mesh size.

### `dMax` @type(Double) @default(0.0)

- The maximum mesh size.

## Return Code

A _Boolean_ specifying the function successfully executed or not.

## Sample Code

```psj {34,35}
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.0101, 0.0, 0.0], strName="Cube_2", iPartColor=14903267)
Meshing.AdjustCircleVertex(crlParts=[Part(2)], bInModeSurfaceMesh=True)
Meshing.SetMeshAttribute(
    crlParts=[Part(2)], 
    surfaceMesh=SURFACE_MESH(
        dAvgElemSize=0.0015,
         dGeomAngle=0.7853981634, 
         iPerformanceMode=1, 
         dAutoMergeTinyFacesAngle=0.5235987756, 
         bGeomApprox=True))
Meshing.SurfaceMeshing(
    crlParts=[Part(2)], 
    surfaceMesh=SURFACE_MESH(
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
print(assemble_sretolid)
```
