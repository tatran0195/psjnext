---
title: "Properties.Material.Modify()"
description: "Modify an existing material in the User database library by inputting all information of the modifying material"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Material > Modify"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Modify an existing material in the User database library by inputting all information of the modifying material.

## Syntax

```psj
Properties.Material.Modify(...)
```

## Inputs

### `iMaterialID` @type(Integer) @required

- The material identification number (ID).

### `dictMaterialProperty` @type(dictionary) @required @since(5.1.0)

- &#xNAN;_[dictMatProps](../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_.

### `listMaterialProperty` @type(List\[MATERIAL PROPERTY])

- The list of all attributes of property such a&#x73;_&#x64;ensity_,_elasticity_, etc.

:::caution
This input is discarded from V5.1. Please use dictMaterialProperty instead.
:::

## Return Code

A _Boolean_ specifying whether the material is modified or not.

## Sample Code

```psj {13-23}
structure_steel = Properties.Material.Add(
    strMaterialName="Structural_Steel", 
    dictMaterialProperty={
        'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
        'Elastic': {'elastic': {'YOUNGS_MODULUS': [200000000000.0], 
        'POISSONS_RATIO': [0.3]}}, 
        'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
        'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
        'SpecificHeat': {'specificHeat': {'SPECIFIC_HEAT': [461.0]}}}, 
    iMaterialID=5,
    iMaterialColor=10264731)

mod_mat = Properties.Material.Modify(
    strMaterialName="Structural_Steel", 
    dictMaterialProperty={
        'Density': {'density': {'DENSITY': [9850.0]}}, 
        'Elastic': {'elastic': {'YOUNGS_MODULUS': [200000000000.0], 
        'POISSONS_RATIO': [0.3]}}, 
        'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
        'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
        'SpecificHeat': {'specificHeat': {'SPECIFIC_HEAT': [461.0]}}}, 
    iMaterialID=5, 
    iMaterialColor=10264731)
JPT.Debugger(mod_mat) #for checking return value
```
