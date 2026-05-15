---
title: "Properties.ElemRelatedInfo.Bar()"
description: "Modify information such as direction vectors and end releases for the selected bar elements or 1D elements contained within the selected edge, individually"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > ElemRelatedInfo > Bar"
---

## Description

Modify information such as direction vectors and end releases for the selected bar elements or 1D elements contained within the selected edge, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Bar(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### listERIRodData

- Specify the element related information of bar.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEribeamEndProp

- Specify the eribeam end property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEribeamOriVecProp

- Specify the eribeam ori vector property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEribeamOriNodeidProp

- Specify the eribeam ori nodeid property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEribeamOffsetVecA

- Specify the eribeam offset vector a.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEribeamOffsetVecB

- Specify the eribeam offset vector .
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEribeamPinAProp

- Specify the eribeam pin a property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEribeamPinBProp

- Specify the eribeam pin property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEribeamWarpProp

- Specify the eribeam warp property.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {21-34}
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
Properties.BAR(
    strName="BAR _1", 
    iPropertyColor=16131973, 
    crMaterial=Material(5), 
    dSectionArea=2e-07, 
    dlSectionOrientation=[0.0, 1.0, 0.0], 
    dlInertiaMoment=[DFLT _DBL, DFLT _DBL, DFLT _DBL], 
    crlTargets=[Elem(88, 87, 89)])
ret = Properties.ElemRelatedInfo.Bar(
    listERIBarData=[
        ERIBAR _DATA(
            iElemId=88, 
            iPropId=1, 
            iEndA=79, 
            iEndB=80, 
            dlOrientVec=[0.0, 0.0, 1.0]), 
        ERIBAR _DATA(
            iElemId=87, 
            iPropId=1, 
            iEndA=78, 
            iEndB=79, 
            dlOrientVec=[0.0, 0.0, 1.0])])
print(ret)
```
