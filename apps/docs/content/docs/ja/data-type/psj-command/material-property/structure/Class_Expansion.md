---
title: Expansion
id: Expansion
---

## Description

This is an instance of an Expansion class, represents Expansion characteristic of material.

## Properties

| Attribute               | Description                                                                                                                                                       |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `expansion`             | A _List of Tuple_ specifying all data of [Expansion characteristic](#expansion-characteristic).                                                                   |
| `expansionType`         | An _Integer_ specifying the type of Expansion.<br /> According to the [selected type](#expansion-characteristic), there will be corresponding elastic parameters. |
| `temperatureReference`  | A _Double_ specifying data of temperature reference.                                                                                                              |
| `temperatureDependency` | A _Boolean_ specifying the use of temperature-dependent data.                                                                                                     |
| `dependencies`          | An _Integer_ specifying the number of dependencies in temperature.                                                                                                |

## Expansion Characteristic {#expansion-characteristic}

Either `KEY NAME` or `ID` can be used to define the material property. The ID of material property which was primarily
used in functions can be referred to in the [Int Notation](../../material-types) column. However, in order to explicitly
describe meaning of material properties, user can use the `KEY NAME` instead of specifying `ID`. For example: `ALPHA` is
equal to ID = 69.

<details>
<summary> **`expansionType = ISOTROPIC`** </summary>

| INT Notation | Key Name       | Description                                                |
| ------------ | -------------- | ---------------------------------------------------------- |
| 69           | `ALPHA`        | A _Tuple_ specifying the expansion coefficient alpha data. |
| 130          | `TEMPERATURE`  | A _Tuple_ specifying the temperature-dependent data.       |
| 143          | `EXTRA_FIELDS` | A _Tuple_ specifying the extra fields data.                |

```psj {2-4} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[Expansion(expansion=[
                                        (ALPHA, [1.2e-05]),
                                        (TEMPERATURE, [100.0])],
                                        temperatureDependency=True)],
                                        iMaterialID=1,
                                        iMaterialColor=11399605,
                                        strDescription=Expansion-ISOTROPIC)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>
<summary> **`expansionType = ORTHOTROPIC(2D)`** </summary>

| INT Notation | Key Name       | Description                                          |
| ------------ | -------------- | ---------------------------------------------------- |
| 70           | `ALPHA11`      | A _Tuple_ specifying the Alpha11(A1) data.           |
| 71           | `ALPHA22`      | A _Tuple_ specifying the Alpha22(A2) data.           |
| 130          | `TEMPERATURE`  | A _Tuple_ specifying the temperature-dependent data. |
| 143          | `EXTRA_FIELDS` | A _Tuple_ specifying the extra fields data.          |

```psj {2-5} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[Expansion(expansion=[
                                        (ALPHA11, [1.2e-05]),
                                        (ALPHA22, [1.5e-05]),
                                        (TEMPERATURE, [100.0])],
                                        expansionType=1,
                                        temperatureDependency=True)],
                                        iMaterialID=1,
                                        iMaterialColor=11399605,
                                        strDescription=Expansion-ISOTROPIC(2D))
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>
<summary> **`expansionType = ORTHOTROPIC(3D)`** </summary>

| INT Notation | Key Name       | Description                                          |
| ------------ | -------------- | ---------------------------------------------------- |
| 70           | `ALPHA11`      | A _Tuple_ specifying the Alpha11(A1) data.           |
| 71           | `ALPHA22`      | A _Tuple_ specifying the Alpha22(A2) data.           |
| 72           | `ALPHA33`      | A _Tuple_ specifying the Alpha33(A3) data.           |
| 130          | `TEMPERATURE`  | A _Tuple_ specifying the temperature-dependent data. |
| 143          | `EXTRA_FIELDS` | A _Tuple_ specifying the extra fields data.          |

```psj {2-6} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[Expansion(expansion=[
                                        (ALPHA11, [1.2e-05]),
                                        (ALPHA22, [1.5e-05]),
                                        (ALPHA33, [2e-05]),
                                        (TEMPERATURE, [100.0])],
                                        expansionType=2,
                                        temperatureDependency=True)],
                                        iMaterialID=1,
                                        iMaterialColor=11399605,
                                        strDescription=Expansion-ORTHOTROPIC(3D))
JPT.Debugger(density) #for checking return value
```

</details>

<details>
<summary> **`expansionType = ANISOTROPIC(2D)`** </summary>

| INT Notation | Key Name       | Description                                          |
| ------------ | -------------- | ---------------------------------------------------- |
| 70           | `ALPHA11`      | A _Tuple_ specifying the Alpha11(A1) data.           |
| 71           | `ALPHA22`      | A _Tuple_ specifying the Alpha22(A2) data.           |
| 73           | `ALPHA12`      | A _Tuple_ specifying the Alpha12(A3) data.           |
| 130          | `TEMPERATURE`  | A _Tuple_ specifying the temperature-dependent data. |
| 143          | `EXTRA_FIELDS` | A _Tuple_ specifying the extra fields data.          |

```psj {2-6} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[Expansion(expansion=[
                                        (ALPHA11, [1.2e-05]),
                                        (ALPHA22, [1.5e-05]),
                                        (ALPHA12, [2e-05]),
                                        (TEMPERATURE, [100.0])],
                                        expansionType=4,
                                        temperatureDependency=True)],
                                        iMaterialID=1,
                                        iMaterialColor=11399605,
                                        strDescription=Expansion-ANISOTROPIC(2D))
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>
<summary> **`expansionType = ANISOTROPIC(3D)`** </summary>

| INT Notation | Key Name       | Description                                          |
| ------------ | -------------- | ---------------------------------------------------- |
| 70           | `ALPHA11`      | A _Tuple_ specifying the Alpha11(A1) data.           |
| 71           | `ALPHA22`      | A _Tuple_ specifying the Alpha22(A2) data.           |
| 72           | `ALPHA33`      | A _Tuple_ specifying the Alpha33(A3) data.           |
| 73           | `ALPHA12`      | A _Tuple_ specifying the Alpha12(A4) data.           |
| 74           | `ALPHA23`      | A _Tuple_ specifying the Alpha12(A5) data.           |
| 75           | `ALPHA13`      | A _Tuple_ specifying the Alpha12(A6) data.           |
| 130          | `TEMPERATURE`  | A _Tuple_ specifying the temperature-dependent data. |
| 143          | `EXTRA_FIELDS` | A _Tuple_ specifying the extra fields data.          |

```psj {2-9} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[Expansion(expansion=[
                                        (ALPHA11, [1e-05]),
                                        (ALPHA22, [2e-05]),
                                        (ALPHA33, [3e-05]),
                                        (ALPHA12, [4e-05]),
                                        (ALPHA13, [5e-05]),
                                        (ALPHA23, [6e-05]),
                                        (TEMPERATURE, [100.0])],
                                        expansionType=5,
                                        temperatureDependency=True)],
                                        iMaterialID=1,
                                        iMaterialColor=11399605,
                                        strDescription=Elastic-LAMINA)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>
