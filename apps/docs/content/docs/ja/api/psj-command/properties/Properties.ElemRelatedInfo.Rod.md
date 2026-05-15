---
title: "Properties.ElemRelatedInfo.Rod()"
description: "Modify information such as direction vectors and end releases for the selected rod elements, individually"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > ElemRelatedInfo > Rod"
---

## Description

Modify information such as direction vectors and end releases for the selected rod elements, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Rod(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### listERIRodData

- Specify the element related information of rod.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEricontEndProp

- Specify the ericont end property.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {19-25}
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
Properties.Rod(
    strName="ROD _1", 
    iPropertyColor=3742001, 
    crMat=Material(5), 
    dArea=2e-07, 
    crlTargets=[Elem(89, 88, 87)])
ret = Properties.ElemRelatedInfo.Rod(
        listERIRodData=[
            ERIROD _DATA(
                iElemId=87, 
                iPropId=1, 
                iEndA=79, 
                iEndB=78)])
print(ret)
```
