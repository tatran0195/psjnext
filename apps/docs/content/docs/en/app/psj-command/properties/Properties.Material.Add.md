---
title: "Properties.Material.Add()"
description: "Create a new material to the current User database library"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Material > Add"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a new material to the current User database library.

> This command is not compatible with V5.0 series. If you wish to use scripts currently running on V5.0.1-V5.0.4 with V5.1, please modify your scripts accordingly.

## Syntax

```psj
Properties.Material.Add(...)
```

## Inputs

### `strMaterialName` @type(String) @required

- The material name.

### `dictMaterialProperty` @type(dictionary) @required @since(5.1.0)

- &#xNAN;_[dictMatProps](../../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_.

### `listMaterialProperty` @type(List\[MATERIAL PROPERTY])

- All attributes of property such a&#x73;_&#x64;ensity_,_elasticity_, etc.

:::caution
This input is discarded from V5.1. Please use dictMaterialProperty instead.
:::

### `iMaterialID` @type(Integer) @required

- Th&#x65;_&#x4E;asI&#x44;_&#x6F;f material to be added.
- Th&#x65;_&#x4E;asI&#x44;_&#x63;an be referred in \*.mlib material library file.

### `iMaterialColor` @type(Integer) @default(0) @since(5.1.0)

- The ID of color .

### `strDescription` @type(String) @default("") @since(5.1.0)

- The description of material.

## Return Code

A _Cursor_ specifying the new material created.

## Sample Code

```psj {30-34}
#Prepare material with unit
dict_mat_prop = {
    'Density': {
        'density': {
            'DENSITY': [8.3e-9],
        },
    },
    'Elastic': {
        'elastic': {
            'POISSONS_RATIO': [0.3],
            'YOUNGS_MODULUS': [1.1e+5],
            'SHEAR_MODULUS': [5.2e+3],
        }
    },
    'Unit': {
        'Density': {
            'density': {  
                'DENSITY': JPT.DensityUnit.Density_t_mm3
            }
        },
        'Elastic': {
            'elastic': {  
                'YOUNGS_MODULUS': JPT.ModulusUnit.Modulus_N_mm2
            }
        }
    }
}

#Add new material to document
new_material=Properties.Material.Add(
    strMaterialName="NewMaterial", 
    dictMaterialProperty=dict_mat_prop,
    iMaterialID=1, 
    iMaterialColor=9614382)

JPT.Debugger(new_material) #for checking return value
```
