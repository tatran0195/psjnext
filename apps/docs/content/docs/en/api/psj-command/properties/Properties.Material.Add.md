---
title: "Properties.Material.Add()"
description: "Create a new material to the current User database library"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Material > Add"
---

## Description

Create a new material to the current User database library.

> This command is not compatible with V5.0 series. If you wish to use scripts currently running on V5.0.1-V5.0.4 with V5.1, please modify your scripts accordingly.

## Syntax

```psj
Properties.Material.Add(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strMaterialName`

- The material name.

<!-- @since:5.1.0 @type:dictMatProps @required -->
### `dictMaterialProperty`

- The _[dictMatProps](../../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_.

<!-- @since:5.0.1 @type:List[MATERIAL PROPERTY] @required -->
<!-- @since:5.1.0 @optional -->
### `listMaterialProperty`

- The all attributes of property such as _density_, _elasticity_, etc.

:::caution
This input is discarded from V5.1. Please use dictMaterialProperty instead.
:::

<!-- @since:5.0.1 @type:Integer @required -->
### `iMaterialID`

- The _NasID_ of material to be added.
- The _NasID_ can be referred in \*.mlib material library file.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iMaterialColor`

- The ID of color .

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strDescription`

- The description of material.

## Return Code

A _Cursor_ specifying the new material created.

## Sample Code

```psj {30-34}
#Prepare material with unit
dict _mat _prop = {
    'Density': {
        'density': {
            'DENSITY': [8.3e-9],
        },
    },
    'Elastic': {
        'elastic': {
            'POISSONS _RATIO': [0.3],
            'YOUNGS _MODULUS': [1.1e+5],
            'SHEAR _MODULUS': [5.2e+3],
        }
    },
    'Unit': {
        'Density': {
            'density': {  
                'DENSITY': JPT.DensityUnit.Density _t_mm3
            }
        },
        'Elastic': {
            'elastic': {  
                'YOUNGS _MODULUS': JPT.ModulusUnit.Modulus _N_mm2
            }
        }
    }
}

#Add new material to document
new _material=Properties.Material.Add(
    strMaterialName="NewMaterial", 
    dictMaterialProperty=dict _mat _prop,
    iMaterialID=1, 
    iMaterialColor=9614382)

JPT.Debugger(new _material) #for checking return value
```
