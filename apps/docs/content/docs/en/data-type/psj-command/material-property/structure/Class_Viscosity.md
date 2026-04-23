---
title: Viscosity
id: Viscosity
---

## Description

This is an instance of a Viscosity class, represents Viscosity characteristic of material.

## Properties

| Attribute             | Description                                                                                     |
| --------------------- | ----------------------------------------------------------------------------------------------- |
| viscosity             | A _List of Tuple_ specifying all data of [Viscosity characteristic](#viscosity-characteristic). |
| viscosityType         | An _Integer_ specifying the type of Viscosity.                                                  |
| temperatureDependency | A _Boolean_ specifying the use of temperature-dependent data.                                   |
| dependencies          | An _Integer_ specifying the number of dependencies in temperature.                              |

## Viscosity Characteristic {#viscosity-characteristic}

Either `KEY NAME` or `ID` can be used to define the material property.
The ID of material property which was primarily used in functions can be referred to in the [Int Notation](../../material-types) column.
However, in order to explicitly describe meaning of material properties, user can use the `KEY NAME` instead of specifying `ID`.
For example: `PRESSURE_FORCE_LOADING` is equal to ID = 63.

<details>

<summary> **`viscosityType = NewTonian`** </summary>

| INT Notation | Key Name    | Description                                          |
| ------------ | ----------- | ---------------------------------------------------- |
| 79           | VISCOSITY   | A _Tuple_ specifying the viscosity data.             |
| 130          | TEMPERATURE | A _Tuple_ specifying the temperature-dependent data. |

```py {2-4} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[StructuralViscosity(viscosity=[
                                        (VISCOSITY, [100.0]),
                                        (TEMPERATURE, [300.0])],
                                        temperatureDependency=True)], iMaterialID=1,
                                        iMaterialColor=12901750)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>
