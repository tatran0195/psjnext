---
title: "Properties.ElemRelatedInfo.Shell()"
description: "Modify information such as direction vectors and end releases for the selected shell elements or elements contained in a face, individually"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > ElemRelatedInfo > Shell"
---

## Description

Modify information such as direction vectors and end releases for the selected shell elements or elements contained in a face, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Shell(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### listERIShellData

- Specify the element related information of shell.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listErishellThetaProp

- Specify the erishell theta property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listErishellCsProp

- Specify the erishell cs property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listErishellZoffsProp

- Specify the erishell zoffs property.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {22-31}
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
Properties.Shell(
    crlTargets=[Part(1)], 
    strName="ShellProperty _1", 
    iPropertyId=2, 
    iPropertyColor=3315481, 
    crMatMembrane=Material(5), 
    crMatBend=Material(5), 
    crMatShear=Material(5), 
    dThickness=0.0002)
ret = Properties.ElemRelatedInfo.Shell(
        listERIShellData=[
            ERISHELL _DATA(
                iElemId=117, 
                iPropId=2, 
                dTheta=0.523599), 
            ERISHELL _DATA(
                iElemId=118, 
                iPropId=2, 
                dTheta=0.523599)])
print(ret)
```
