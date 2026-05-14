---
title: "HexModeling.FromMidPlane()"
description: "Hexahedral and pentahedral elements are created by sweeping neutral surface parts or shell meshes—assigned with shell properties (such as specified thickness)—by the defined thickness."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > FromMidPlane"
---

## Description

Hexahedral and pentahedral elements are created by sweeping neutral surface parts or shell meshes—assigned with shell properties (such as specified thickness)—by the defined thickness.

## Syntax

```psj
HexModeling.FromMidPlane(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bRef`

- The reference.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {40}
import os

#Check license of midplane to use midplane function
MidplaneLicense="JPT _MIDP"
JPT.EnableLicenseFeature(MidplaneLicense, 1)
check=JPT.CheckLicense(MidplaneLicense)

if check == False:
    JPT.MessageBoxPSJ(f"{MidplaneLicense} license is needed to create midplane.\n (This sample needs midplane to execute.)", JPT.MsgBoxType.MB _WARNING _OK)
else:
    cadFile=os.path.join(JPT.GetProgramPath(),'SampleData/bracket.x _t')

    Home.ImportCAD.Parasolid(strlPaths=[cadFile], dScale=0.001)

    MidPlane.PressShell(crlPart=[Part(1)], dTinyHollowDepth=0.0002)

    Meshing.SetMeshAttribute(
        crlParts=[Part(1)], 
        surfaceMesh=SURFACE _MESH(
            dAvgElemSize=0.01, 
            dMaxElemSize=0.02, 
            dGeomAngle=0.7853981634, 
            iPerformanceMode=1, 
            dAutoMergeTinyFacesAngle=0.5235987756, 
            bOutputQuadMesh=True, 
            bGeomApprox=True, 
            iNextEntityOffsetId=0))

    Meshing.SurfaceMeshing(
        crlParts=[Part(1)], 
        surfaceMesh=SURFACE _MESH(dAvgElemSize=0.01, 
        dMaxElemSize=0.02, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

    HexModeling.FromMidPlane(crlParts=[Part(1)])
```
