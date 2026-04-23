---
title: Conductivity
id: Conductivity
---

## Description

This is an instance of a Conductivity class, represents Conductivity characteristic of material.

## Properties

| Attribute               | Description                                                                                                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `conductivity`          | A _List of Tuple_ specifying all data of [Conductivity characteristic](#conductivity-characteristic).                                                                        |
| `conductivityType`      | An _Integer_ specifying the type of conductivity.<br /> According to the [selected type](#conductivity-characteristic), there will be corresponding conductivity parameters. |
| `temperatureDependency` | A _Boolean_ specifying whether to use the temperature-dependence data.                                                                                                       |
| `dependencies`          | An _Integer_ specifying the number of field variables.                                                                                                                       |

## Conductivity Characteristic {#conductivity-characteristic}

Either `KEY NAME` or `ID` can be used to define the material property.
The ID of material property which was primarily used in functions can be referred to in the [Int Notation](../../material-types) column.
However, in order to explicitly describe meaning of material properties, user can use the `KEY NAME` instead of specifying `ID`.
For example: `CONDUCTIVITY` is equal to ID = 51.

<details>

<summary> **`conductivityType = ISOTROPIC`** </summary>

| Int Notation | Key Name       | Description                                          |
| ------------ | -------------- | ---------------------------------------------------- |
| 51           | `CONDUCTIVITY` | A _Tuple_ specifying the conductivity data.          |
| 130          | `TEMPERATURE`  | A _Tuple_ specifying the temperature-dependent data. |
| 143          | `EXTRA_FIELDS` | A _Tuple_ specifying the extra fields data.          |

```py {2-4} title="Sample Code"
sample_Mat = Properties.Material.Modify(strMaterialName="Sample_Material",
                                        listMaterialProperty=[Conductivity(conductivity=[
                                            (CONDUCTIVITY, [59.0]),
                                            (TEMPERATURE, [200.0])],
                                            temperatureDependency=True)],
                                            iMaterialID=1,
                                            iMaterialColor=13708224,
                                            strDescription=Conductivity)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>

<summary> **`conductivityType = ORTHOTROPIC`** </summary>

| Int Notation | Key Name       | Description                                          |
| ------------ | -------------- | ---------------------------------------------------- |
| 52           | `K11`          | A _Tuple_ specifying the K11 data.                   |
| 53           | `K22`          | A _Tuple_ specifying the K22 data.                   |
| 54           | `K33`          | A _Tuple_ specifying the K33 data.                   |
| 130          | `TEMPERATURE`  | A _Tuple_ specifying the temperature-dependent data. |
| 143          | `EXTRA_FIELDS` | A _Tuple_ specifying the extra fields data.          |

```py {2-4} title="Sample Code"
sample_Mat = Properties.Material.Modify(strMaterialName="Sample_Material",
                                        listMaterialProperty=[Conductivity(conductivity=[
                                            (K11, [10.0]), (K22, [20.0]), (K33, [30.0]),
                                            (TEMPERATURE, [100.0])],
                                            conductivityType=1,
                                            temperatureDependency=True)],
                                            iMaterialID=1,
                                            iMaterialColor=1506702,
                                            strDescription=Conductivity)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>

<summary> **`conductivityType = ANISOTROPIC`** </summary>

| Int Notation | Key Name       | Description                                          |
| ------------ | -------------- | ---------------------------------------------------- |
| 52           | `K11`          | A _Tuple_ specifying the K11 data.                   |
| 53           | `K22`          | A _Tuple_ specifying the K22 data.                   |
| 54           | `K33`          | A _Tuple_ specifying the K33 data.                   |
| 55           | `K12`          | A _Tuple_ specifying the K12 data.                   |
| 56           | `K13`          | A _Tuple_ specifying the K13 data.                   |
| 57           | `K23`          | A _Tuple_ specifying the K23 data.                   |
| 130          | `TEMPERATURE`  | A _Tuple_ specifying the temperature-dependent data. |
| 143          | `EXTRA_FIELDS` | A _Tuple_ specifying the extra fields data.          |

```py {2-5} title="Sample Code"
sample_Mat = Properties.Material.Modify(strMaterialName="Sample_Material",
                                        listMaterialProperty=[Conductivity(conductivity=[
                                            (K11, [10.0]), (K12, [20.0]), (K22, [30.0]),
                                            (K13, [40.0]), (K23, [50.0]), (K33, [60.0]),
                                            (TEMPERATURE, [100.0])],
                                            conductivityType=2,
                                            temperatureDependency=True)],
                                            iMaterialID=1,
                                            iMaterialColor=4738715,
                                            strDescription=Conductivity)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>
