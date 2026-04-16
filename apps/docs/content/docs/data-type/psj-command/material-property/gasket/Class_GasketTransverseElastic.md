---
title: GasketTransverseElastic
id: GasketTransverseElastic
---

## Description

This is an instance of a GasketTransverseElastic class, represents GasketTransverseElastic characteristic of material.

## Properties

| Attribute                 | Description                                                                                                                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `gasketTransverseElastic` | A _List of Tuple_ specifying all data of [GasketTransverseElastic characteristic](#gaskettransverseelastic-characteristic). <br /> The data includes SHEAR_STIFFNESS_H, TEMPERATURE_H, EXTRA_FIELDS_H, SHEAR_STIFFNESS_V, TEMPERATURE_V, and EXTRA_FIELDS_V. |
| `temperatureDependencyH`  | A _Boolean_ specifying whether to use the temperature-dependent data (horizontal transverse).                                                                                                                                                                |
| `dependenciesH`           | An _Integer_ specifying the number of field variables (horizontal transverse).                                                                                                                                                                               |
| `unitH`                   | An _Integer_ specifying the unit type of horizontal transverse.                                                                                                                                                                                              |
| `unitV`                   | An _Integer_ specifying the unit type of vertical transverse                                                                                                                                                                                                 |
| `temperatureDependencyV`  | A _Boolean_ specifying whether to use the temperature-dependent data (vertical transverse).                                                                                                                                                                  |
| `dependenciesV`           | An _Integer_ specifying the number of field variables (vertical transverse).                                                                                                                                                                                 |

## GasketTransverseElastic Characteristic {#gaskettransverseelastic-characteristic}

Either `KEY NAME` or `ID` can be used to define the material property.
The ID of material property which was primarily used in functions can be referred to in the [Int Notation](../../material-types) column.
However, in order to explicitly describe meaning of material properties, user can use the `KEY NAME` instead of specifying `ID`.
For example: `YOUNGS_MODULUS` is equal to ID = 1.

| INT Notation | Key Name            | Description                                                                   |
| ------------ | ------------------- | ----------------------------------------------------------------------------- |
| 137          | `SHEAR_STIFFNESS_H` | A _Tuple_ specifying the shear stiffness data in horizontal transverse.       |
| 138          | `SHEAR_STIFFNESS_V` | A _Tuple_ specifying the shear stiffness data in vertical transverse.         |
| 131          | `TEMPERATURE_H`     | A _Tuple_ specifying the temperature-dependent data in horizontal transverse. |
| 132          | `TEMPERATURE_V`     | A _Tuple_ specifying the temperature-dependent data in vertical transverse.   |
| 144          | `EXTRA_FIELDS_H`    | A _Tuple_ specifying the extra field data in horizontal transverse.           |
| 145          | `EXTRA_FIELDS_V`    | A _Tuple_ specifying the extra field data in vertical transverse.             |

```psj {2-4} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[GasketTransverseElastic(gasketTransverseElastic=[
                                        (SHEAR_STIFFNESS_H, [400.0]),
                                        (TEMPERATURE_H, [200.0])],
                                        unitH=1,
                                        temperatureDependencyH=True,
                                        unitV=1)],
                                        iMaterialID=1,
                                        iMaterialColor=3315481,
                                        strDescription="GasketTransverseElastic")
JPT.Debugger(sample_Mat) #for checking return value
```
