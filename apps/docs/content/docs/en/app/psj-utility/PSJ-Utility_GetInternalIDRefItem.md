---
title: "JPT.GetInternalIDRefItem()"
description: "Get internal ID of reference entity."
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Get internal ID of a reference entity.

## Syntax

```psj
JPT.GetInternalIDRefItem(...)
```

## Inputs

### `DItemType` @type(Enum) @required

- Th&#x65;_[DItemType](../data-type/psj-command/DItem-types)_&#x64;escribing the type of entity (reference entities here).

### `externalID` @type(Int) @required

- External ID of reference item.

### `bUsedRef` @type(Bool)

- If the target is reference item.
- The defalut value is True.

## Return Code

A _Int_ value that indicates internal ID of the reference entity.

## Sample Code

```psj {37}
Geometry.Part.Cube()

Tools.Renumber(
    listRenumberItem=[
        RENUMBER_ITEM(crTarget=Part(1), 
        iBeginID=1000, 
        iTargetType=5,
        iCount=6, 
        ilOffset=[10000, 100, 1], 
    dlCoordTolerance=[0.1, 0.1, 0.1], 
    bEnable=True)])

Meshing.AdjustCircleVertex(crlParts=[Part(1)], bInModeSurfaceMesh=True)

Meshing.SetMeshAttribute(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(
        dMaxElemSize=0.05, 
        dMinElemSize=0.0001, 
        dGeomAngle=0.7853981634,
        dGeomMinSize=0.0001, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0)
         )

Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE_MESH(
        dMaxElemSize=0.05, 
        dMinElemSize=0.0001, 
        dGeomAngle=0.7853981634, 
        dGeomMinSize=0.0001, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0)
        )

result=JPT.GetInternalIDRefItem(JPT.DItemType.REF_FACE,1005)
print(result)
```
