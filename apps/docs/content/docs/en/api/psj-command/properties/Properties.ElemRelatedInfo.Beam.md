---
title: "Properties.ElemRelatedInfo.Beam()"
description: "Modify information such as direction vectors and end releases for the selected beam elements or 1D elements contained within the selected edge, individually"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > ElemRelatedInfo > Beam"
---

## Description

Modify information such as direction vectors and end releases for the selected beam elements or 1D elements contained within the selected edge, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Beam(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[ERIBEAM _DATA class] @optional @default:[] -->
### `listERIBeamData`

- The element related information of beam.

<!-- @since:5.0.1 @type:ERIBEAM _END _PROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEribeamEndProp`

- The eribeam end property.

<!-- @since:5.0.1 @type:ERIBEAM _ORI _VEC _PROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEribeamOriVecProp`

- The eribeam ori vector property.

<!-- @since:5.0.1 @type:ERIBEAM _ORI _NODEID _PROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEribeamOriNodeidProp`

- The eribeam ori nodeid property.

<!-- @since:5.0.1 @type:ERIBEAM _OFFSET _VEC _A List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEribeamOffsetVecA`

- The eribeam offset vector a.

<!-- @since:5.0.1 @type:ERIBEAM _OFFSET _VEC _B List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEribeamOffsetVecB`

- The eribeam offset vector .

<!-- @since:5.0.1 @type:ERIBEAM _PIN _APROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEribeamPinAProp`

- The eribeam pin a property.

<!-- @since:5.0.1 @type:ERIBEAM _PIN _BPROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEribeamPinBProp`

- The eribeam pin property.

<!-- @since:5.0.1 @type:ERIBEAM _WARP _PROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEribeamWarpProp`

- The eribeam warp property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {29-36}
Geometry.Part.Cube(iPartColor=6409934)
Properties.Material.Add(
    strMaterialName="Structural _Steel", 
    dictMaterialProperty={
        'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
        'Elastic': {'elastic': {'YOUNGS _MODULUS': [200000000000.0], 
        'POISSONS _RATIO': [0.3]}}, 
        'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
        'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
        'SpecificHeat': {'specificHeat': {'SPECIFIC _HEAT': [461.0]}}}, 
    iMaterialID=5, 
    iMaterialColor=10264731)
Properties.Beam(
    strName="BEAM _1", 
    iPropertyColor=3742001, 
    crMaterial=Material(5), 
    dSectionArea=2e-07, 
    dlSectionOrientation=[DFLT _DBL, DFLT _DBL, DFLT _DBL], 
    dlInertiaMoment=[DFLT _DBL, DFLT _DBL, DFLT _DBL], 
    dStressRecoveryCoeffCy=DFLT _DBL, 
    dStressRecoveryCoeffCz=DFLT _DBL, 
    dStressRecoveryCoeffDy=DFLT _DBL, 
    dStressRecoveryCoeffDz=DFLT _DBL, 
    dStressRecoveryCoeffEy=DFLT _DBL, 
    dStressRecoveryCoeffEz=DFLT _DBL, 
    dStressRecoveryCoeffFy=DFLT _DBL, 
    dStressRecoveryCoeffFz=DFLT _DBL, 
    crlTargets=[Elem(89, 88, 87)])
ret = Properties.ElemRelatedInfo.Beam(
    listERIBeamData=[
        ERIBEAM _DATA(
            iElemId=87, 
            iPropId=1, 
            iEndA=78, 
            iEndB=79, 
            dlOrientVec=[0.0, 0.0, 1.0])])
print(ret)
```
