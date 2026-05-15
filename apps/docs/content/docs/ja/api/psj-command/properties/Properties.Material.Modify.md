---
title: "Properties.Material.Modify()"
description: "Modify an existing material in the User database library by inputting all information of the modifying material"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Material > Modify"
---

## Description

Modify an existing material in the User database library by inputting all information of the modifying material.

## Syntax

```psj
Properties.Material.Modify(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### iMaterialID

- Specify the material identification number (ID).

<!-- @since:5.1.0 @required -->
### dictMaterialProperty

- Specify _[dictMatProps](../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_.

<!-- @since:5.0.1 @required -->
<!-- @since:5.1.0 @optional -->
### listMaterialProperty

- Specify the list of all attributes of property such as _density_, _elasticity_, etc.

:::caution
This input is discarded from V5.1. Please use dictMaterialProperty instead.
:::

## Return Code

A _Boolean_ specifying whether the material is modified or not.

## Sample Code

```psj {13-23}
structure _steel = Properties.Material.Add(
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

mod _mat = Properties.Material.Modify(
    strMaterialName="Structural _Steel", 
    dictMaterialProperty={
        'Density': {'density': {'DENSITY': [9850.0]}}, 
        'Elastic': {'elastic': {'YOUNGS _MODULUS': [200000000000.0], 
        'POISSONS _RATIO': [0.3]}}, 
        'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
        'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
        'SpecificHeat': {'specificHeat': {'SPECIFIC _HEAT': [461.0]}}}, 
    iMaterialID=5, 
    iMaterialColor=10264731)
JPT.Debugger(mod _mat) #for checking return value
```
