---
title: Creep
id: Creep
---

## Description

This is an instance of a Creep class, represents Creep characteristic of material.

## Properties

| Attribute             | Description                                                                             |
| --------------------- | --------------------------------------------------------------------------------------- |
| creep                 | A _List of Tuple_ specifying all data of [Creep characteristic](#creep-characteristic). |
| lawType               | An _Integer_ specifying the law option.                                                 |
| suboption             | An _Integer_ specifying the subordinate option.                                         |
| advcHardenType        | An _Integer_ specifying the ADVC harden option.                                         |
| advcLawType           | An _Integer_ specifying the ADVC law option.                                            |
| temperatureDependency | A _Boolean_ specifying the use of temperature-dependent data.                           |

## Creep Characteristic {#creep-characteristic}

Either `KEY NAME` or `ID` can be used to define the material property. The ID of material property which was primarily
used in functions can be referred to in the [Int Notation](../../../material-types) column. However, in order to
explicitly describe meaning of material properties, user can use the `KEY NAME` instead of specifying `ID`. For example:
`PRESSURE_FORCE_LOADING` is equal to ID = 63.

<details>

<summary> **`lawType = Strain-Hardening`** </summary>

| INT Notation | Key Name             | Description                                          |
| ------------ | -------------------- | ---------------------------------------------------- |
| 118          | POWER_LAW_MULTIPLIER | A _Tuple_ specifying the power law multiplier data.  |
| 121          | EQ_STRESS_ORDER      | A _Tuple_ specifying the Eq stress order data.       |
| 124          | TIME_ORDER           | A _Tuple_ specifying the time order data.            |
| 130          | TEMPERATURE          | A _Tuple_ specifying the temperature-dependent data. |

```psj {2-6} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[Creep(creep=
                                        [(POWER_LAW_MULTIPLIER, [2.0]),
                                        (EQ_STRESS_ORDER, [1.0]),
                                        (TIME_ORDER, [1.0]),
                                        (TEMPERATURE, [300.0])],
                                        lawType=0,
                                        suboption=0,
                                        advcHardenType=1, advcLawType=0,
                                        temperatureDependency=1)],
                                        iMaterialID=1,
                                        iMaterialColor=16131973)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>

<summary> **`lawType = Time-Hardening`** </summary>

| INT Notation | Key Name             | Description                                          |
| ------------ | -------------------- | ---------------------------------------------------- |
| 118          | POWER_LAW_MULTIPLIER | A _Tuple_ specifying the power law multiplier data.  |
| 121          | EQ_STRESS_ORDER      | A _Tuple_ specifying the Eq stress order data.       |
| 124          | TIME_ORDER           | A _Tuple_ specifying the time order data.            |
| 130          | TEMPERATURE          | A _Tuple_ specifying the temperature-dependent data. |

```psj {2-6} title="Sample Code"
sample_Mat = Properties.Material.Modify(strMaterialName="Sample_Material",
                                        listMaterialProperty=[Creep(creep=
                                            [(POWER_LAW_MULTIPLIER, [2.0]),
                                            (EQ_STRESS_ORDER, [1.0]),
                                            (TIME_ORDER, [1.0]),
                                            (TEMPERATURE, [300.0])],
                                            lawType=1,
                                            suboption=0,
                                            advcHardenType=1,
                                            advcLawType=0,
                                            temperatureDependency=1)],
                                            iMaterialID=1, iMaterialColor=16131973)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>

<summary> **`lawType = Hyperbolic-Sine`** </summary>

| INT Notation | Key Name             | Description                                          |
| ------------ | -------------------- | ---------------------------------------------------- |
| 118          | POWER_LAW_MULTIPLIER | A _Tuple_ specifying the power law multiplier data.  |
| 119          | HYPER_LAW_MULTIPLIER | A _Tuple_ specifying the hyper law multiplier data.  |
| 121          | EQ_STRESS_ORDER      | A _Tuple_ specifying the Eq stress order data.       |
| 123          | ACTIVATION_ENERGY    | A _Tuple_ specifying the activation energy data.     |
| 122          | UNIVERSAL_GAS_CONST  | A _Tuple_ specifying the Universal gas const data.   |
| 130          | TEMPERATURE          | A _Tuple_ specifying the temperature-dependent data. |

```psj {2-8} title="Sample Code"
sample_Mat = Properties.Material.Modify(strMaterialName="Sample_Material",
                                        listMaterialProperty=[Creep(creep=
                                            [(POWER_LAW_MULTIPLIER, [2.0]),
                                            (HYPER_LAW_MULTIPLIER, [2.0]),
                                            (EQ_STRESS_MULTIPLIER, [1.0]),
                                            (ACTIVATION_ENERGY, [500.0]),
                                            (UNIVERSAL_GAS_CONST, [10.0]),
                                            (TEMPERATURE, [300.0])],
                                            lawType=2,
                                            suboption=0,
                                            advcHardenType=1,
                                            advcLawType=0,
                                            temperatureDependency=1)],
                                            iMaterialID=1,
                                            iMaterialColor=16131973)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>

<summary> **`lawType = ADVC-Law`** </summary>

| INT Notation | Key Name | Description                       |
| ------------ | -------- | --------------------------------- |
| 101          | C0       | A _Tuple_ specifying the C0 data. |
| 102          | C1       | A _Tuple_ specifying the C1 data. |
| 103          | C2       | A _Tuple_ specifying the C2 data. |
| 104          | C3       | A _Tuple_ specifying the C3 data. |

```psj {2-6} title="Sample Code"
sample_Mat = Properties.Material.Modify(strMaterialName="Sample_Material",
                                        listMaterialProperty=[Creep(creep=
                                            [(C0, [100.0]),
                                            (C1, [200.0]),
                                            (C2, [100.0]),
                                            (C3, [300.0])],
                                            lawType=4,
                                            suboption=0,
                                            advcHardenType=1,
                                            advcLawType=0,
                                            temperatureDependency=1)],
                                            iMaterialID=1,
                                            iMaterialColor=16131973)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>
