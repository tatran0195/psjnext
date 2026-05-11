---
title: Resistivity
id: Resistivity
---

## Description

This is an instance of a Resistivity class, represents Resistivity characteristic of material.

## Properties

| Attribute             | Description                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------- |
| resistivity           | A _List of Tuple_ specifying all data of [Resistivity characteristic](#resistivity-characteristic). |
| temperatureDependency | A _Boolean_ specifying the use of temperature-dependent data.                                       |

## Resistivity Characteristic {#resistivity-characteristic}

Either `KEY NAME` or `ID` can be used to define the material property. The ID of material property which was primarily
used in functions can be referred to in the [Int Notation](../../material-types) column. However, in order to explicitly
describe meaning of material properties, user can use the `KEY NAME` instead of specifying `ID`. For example:
`PRESSURE_FORCE_LOADING` is equal to ID = 63.

| INT Notation | Key Name    | Description                                          |
| ------------ | ----------- | ---------------------------------------------------- |
| 128          | RESISTIVITY | A _Tuple_ specifying the resistivity data            |
| 130          | TEMPERATURE | A _Tuple_ specifying the temperature-dependent data. |

```psj {2-4} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[Resistivity(resistivity=[
                                        (RESISTIVITY, [0.0005]),
                                        (TEMPERATURE, [573.15])],
                                        temperatureDependency=True)],
                                        iMaterialID=1,
                                        iMaterialColor=3742001)
JPT.Debugger(sample_Mat) #for checking return value
```
