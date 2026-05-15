---
title: "Properties.Material.Delete()"
description: "Delete an existing material in the User database by inputting its ID"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Material > Delete"
---

## Description

Delete an existing material in the User database by inputting its ID.

## Syntax

```psj
Properties.Material.Delete(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### iMaterialID

- Specify the material identification number (ID).

## Return Code

A _Boolean_ specifying whether the inputted material is deleted successfully or not.

## Sample Code

```psj {9}
structure _steel = Properties.Material.Add(strMaterialName = "Structural _Steel",
                                          listMaterialProperty = [Density([(DENSITY, 
                                                                            7.85e-09)]),
                                                                  Elastic([(YOUNGS _MODULUS, 
                                                                            200000.0), 
                                                                           (POISSONS _RATIO, 
                                                                            0.3)])])

del _mat = Properties.Material.Delete(1) # 1 is the ID of the created material

JPT.Debugger(del _mat) # For checking return value
```
