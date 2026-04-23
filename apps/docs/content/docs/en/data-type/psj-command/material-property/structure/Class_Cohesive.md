---
title: Cohesive
id: Cohesive
---

## Description

This is an instance of a Expansion class, represents Expansion characteristic of material.

## Properties

| Attribute             | Description                                                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| expansion             | A _List of Tuple_ specifying all data of Expansion characteristic. <br /> The data includes ALPHA11, ALPHA22, TEMPERATURE, and EXTRA_FIELDS. |
| expansionType         | An _Integer_ specifying the type of Expansion.                                                                                               |
| temperatureReference  | A _Double_ specifying data of temperature reference.                                                                                         |
| temperatureDependency | A _Boolean_ specifying the use of temperature-dependent data.                                                                                |
| dependencies          | An _Integer_ specifying the number of dependencies in temperature.                                                                           |

## Sample Code

```py {1-4}
structure_steel = Properties.Material.Add(strMaterialName="Structural_Steel",
    listMaterialProperty=[Density([(DENSITY, 7.85e-09)]),
    Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])],
    iMaterialID=5)

JPT.Debugger(structure_steel) #for checking return value
```
