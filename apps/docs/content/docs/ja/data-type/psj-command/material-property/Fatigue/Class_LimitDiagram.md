---
title: LimitDiagram
id: LimitDiagram
---

## Description

This is an instance of a Limit Diagram class, represents Limit Diagram characteristic of material.

## Properties

| Attribute             | Description                                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------------------- |
| limitDiagram          | A _List of Tuple_ specifying all data of [Limit Diagram characteristic](#limitdiagram-characteristic). <br /> |
| temperatureDependency | A _Boolean_ specifying the use of temperature-dependent data.                                                 |
| dependencies          | An _Integer_ specifying the number of dependencies in temperature.                                            |

## Limit Diagram Characteristic {#limitdiagram-characteristic}

Either `KEY NAME` or `ID` can be used to define the material property.
The ID of material property which was primarily used in functions can be referred to in the [Int Notation](../../material-types) column.
However, in order to explicitly describe meaning of material properties, user can use the `KEY NAME` instead of specifying `ID`.
For example: `PRESSURE_FORCE_LOADING` is equal to ID = 63.

| INT Notation | Key Name         | Description                                          |
| ------------ | ---------------- | ---------------------------------------------------- |
| 125          | MEAN_STRESS      | A _Tuple_ specifying the mean stress data.           |
| 126          | STRESS_AMPLITUDE | A _Tuple_ specifying the stress amplitude data.      |
| 130          | TEMPERATURE      | A _Tuple_ specifying the temperature-dependent data. |

```psj {2-5} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[FatigueLimitDiagram(limitDiagram=[
                                        (MEAN_STRESS, [0.8]),
                                        (STRESS_AMPLITUDE, [10.0]),
                                        (TEMPERATURE, [300.0])],
                                        temperatureDependency=True)],
                                        iMaterialID=1,
                                        iMaterialColor=1415085)

JPT.Debugger(sample_Mat) #for checking return value
```
