---
title: "JPT.GetInternalIDRefItem()"
description: "Get internal ID of reference entity."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get internal ID of a reference entity.

## Syntax

```psj
JPT.GetInternalIDRefItem(...)
```

## Inputs

<!-- @since:5.1.0 @type:DItemType @required -->
### `DItemType`

- The _[DItemType](../data-type/psj-command/DItem-types)_ describing the type of entity (reference entities here).

<!-- @since:5.1.0 @type:Int @required -->
### `externalID`

- The external ID of reference item.

<!-- @since:5.1.0 @type:Bool @optional -->
### `bUsedRef`

- If the target is reference item.
- The defalut value is True.

## Return Code

A _Int_ value that indicates internal ID of the reference entity.

## Sample Code

```psj {37}
Geometry.Part.Cube()

Tools.Renumber(
    listRenumberItem=[
        RENUMBER _ITEM(crTarget=Part(1), 
        iBeginID=1000, 
        iTargetType=5,
        iCount=6, 
        ilOffset=[10000, 100, 1], 
    dlCoordTolerance=[0.1, 0.1, 0.1], 
    bEnable=True)])

Meshing.AdjustCircleVertex(crlParts=[Part(1)], bInModeSurfaceMesh=True)

Meshing.SetMeshAttribute(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(
        dMaxElemSize=0.05, 
        dMinElemSize=0.0001, 
        dGeomAngle=0.7853981634,
        dGeomMinSize=0.0001, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0)
         )

Meshing.SurfaceMeshing(
    crlParts=[Part(1)], 
    surfaceMesh=SURFACE _MESH(
        dMaxElemSize=0.05, 
        dMinElemSize=0.0001, 
        dGeomAngle=0.7853981634, 
        dGeomMinSize=0.0001, 
        iPerformanceMode=1, 
        dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0)
        )

result=JPT.GetInternalIDRefItem(JPT.DItemType.REF _FACE,1005)
print(result)
```
