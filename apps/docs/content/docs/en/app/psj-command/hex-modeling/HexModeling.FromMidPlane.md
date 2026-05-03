---
title: "HexModeling.FromMidPlane()"
description: "Hexahedral and pentahedral elements are created by sweeping neutral surface parts or shell meshes—assigned with shell properties (such as specified thickness)—by the defined thickness."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "HexModeling > FromMidPlane"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["HexModeling From MidPlane","Hexahedral and pentahedral elements are created by sweeping neutral surface parts or shell meshes—assigned with shell properties (such as specified thickness)—by the defined thickness."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Hexahedral and pentahedral elements are created by sweeping neutral surface parts or shell meshes—assigned with shell properties (such as specified thickness)—by the defined thickness.

## Syntax

```psj
HexModeling.FromMidPlane(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The part.

### `bRef` @type(Boolean) @default(True)

- The reference.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {40}
import os

#Check license of midplane to use midplane function
MidplaneLicense="JPT_MIDP"
JPT.EnableLicenseFeature(MidplaneLicense, 1)
check=JPT.CheckLicense(MidplaneLicense)

if check == False:
    JPT.MessageBoxPSJ(f"{MidplaneLicense} license is needed to create midplane.\n (This sample needs midplane to execute.)", JPT.MsgBoxType.MB_WARNING_OK)
else:
    cadFile=os.path.join(JPT.GetProgramPath(),'SampleData/bracket.x_t')

    Home.ImportCAD.Parasolid(strlPaths=[cadFile], dScale=0.001)

    MidPlane.PressShell(crlPart=[Part(1)], dTinyHollowDepth=0.0002)

    Meshing.SetMeshAttribute(
        crlParts=[Part(1)], 
        surfaceMesh=SURFACE_MESH(
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
        surfaceMesh=SURFACE_MESH(dAvgElemSize=0.01, 
        dMaxElemSize=0.02, 
        dGeomAngle=0.7853981634, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, 
        bOutputQuadMesh=True, 
        bGeomApprox=True, 
        iNextEntityOffsetId=0))

    HexModeling.FromMidPlane(crlParts=[Part(1)])
```
