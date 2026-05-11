---
title: Plastic
id: Plastic
---

## Description

This is an instance of a Plastic class, represents Plastic characteristic of material.

## Properties

| Attribute                  | Description                                                                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| plastic                    | A _List of Tuple_ specifying all data of [Plastic characteristic](#plastic-characteristic).         |
| harden                     | An _Integer_ specifying the hardening type.                                                         |
| curve                      | An _Integer_ specifying the curve type.                                                             |
| curve_ForCombined          | An _Integer_ specifying the curve type that used for Combined Hardening.                            |
| dataType                   | An _Integer_ specifying data type that used for Combined Hardening.                                 |
| temperatureDependency      | A _Boolean_ specifying whether to use temperature-dependent data.                                   |
| dependencies               | An _Integer_ specifying the number of field variables.                                              |
| useStrain                  | A _Boolean_ specifying whether to use Strain-Range-Dependent data for Isotropic/Combined Hardening. |
| exportAdvc                 | A _Boolean_ specifying whether to export as mises (ADVC).                                           |
| backStress                 | An _Integer_ specifying the number of back stresses for Combined Hardening.                         |
| subOption_Type             | An _Integer_ specifying the type of sub option                                                      |
| subOption_FieldNum         | An _Integer_ specifying the number of fields used for sub option.                                   |
| subOption_UseTempDependent | A _Boolean_ specifying the whether to use temperature-dependent data for sub option.                |
| subOption_UseParameter     | A _Boolean_ specifying whether to use parameter for sub option.                                     |

## Plastic Characteristic {#plastic-characteristic}

Either `KEY NAME` or `ID` can be used to define the material property. The ID of material property which was primarily
used in functions can be referred to in the [Int Notation](../../../material-types) column. However, in order to
explicitly describe meaning of material properties, user can use the `KEY NAME` instead of specifying `ID`. For example:
`PRESSURE_FORCE_LOADING` is equal to ID = 63.

<details>

<summary> **`harden = Isotropic`** </summary>

| INT Notation | Key Name        | Description                                           |
| ------------ | --------------- | ----------------------------------------------------- |
| 40           | STRESS          | A _Tuple_ specifying the yield stress data.           |
| 41           | STRAIN          | A _Tuple_ specifying the plastic train data.          |
| 140          | STRAIN_RATE     | A _Tuple_ specifying the strain-rate-dependent data.  |
| 130          | TEMPERATURE     | A _Tuple_ specifying the temperature-dependent data.  |
| 143          | EXTRA_FIELDS    | A _Tuple_ specifying the extra fields data.           |
| 60           | EQUIV_STRESS    | A _Tuple_ specifying the equivalent stress data.      |
| 62           | Q_INFINITY      | A _Tuple_ specifying the Q infinity data.             |
| 68           | HARDENING_B     | A _Tuple_ specifying the hardening B data.            |
| 133          | TEMPERATURE_SUB | A _Tuple_ specifying the temperature sub option data. |

```psj {2-6} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[Plastic(plastic=[
                                        (STRESS, [0.0005]),
                                        (STRAIN, [0.2]),
                                        (STRAIN_RATE, [0.2]),
                                        (TEMPERATURE, [100.0])],
                                        temperatureDependency=True,
                                        useStrain=True,
                                        exportAdvc=True,
                                        subOption_Type=1)],
                                        iMaterialID=1,
                                        iMaterialColor=16131973)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>

<summary> **`harden = Kinematic`** </summary>

| INT Notation | Key Name        | Description                                           |
| ------------ | --------------- | ----------------------------------------------------- |
| 40           | STRESS          | A _Tuple_ specifying the yield stress data.           |
| 41           | STRAIN          | A _Tuple_ specifying the plastic train data.          |
| 130          | TEMPERATURE     | A _Tuple_ specifying the temperature-dependent data.  |
| 60           | EQUIV_STRESS    | A _Tuple_ specifying the equivalent stress data.      |
| 62           | Q_INFINITY      | A _Tuple_ specifying the Q infinity data.             |
| 68           | HARDENING_B     | A _Tuple_ specifying the hardening B data.            |
| 133          | TEMPERATURE_SUB | A _Tuple_ specifying the temperature sub option data. |

```psj {2-5} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[Plastic(plastic=[
                                        (STRESS, [0.0005]),
                                        (STRAIN, [0.2]),
                                        (TEMPERATURE, [1000.0])],
                                        harden=1,
                                        temperatureDependency=True)],
                                        iMaterialID=1,
                                        iMaterialColor=16131973)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>

<summary> **`harden = Johnson_Cook`** </summary>

| INT Notation | Key Name        | Description                                           |
| ------------ | --------------- | ----------------------------------------------------- |
| 42           | A               | A _Tuple_ specifying the A data.                      |
| 43           | B               | A _Tuple_ specifying the B data.                      |
| 44           | M               | A _Tuple_ specifying the M data.                      |
| 45           | N               | A _Tuple_ specifying the N data.                      |
| 46           | MELTING_TEMP    | A _Tuple_ specifying the melting temperature data.    |
| 47           | TRANSITION_TEMP | A _Tuple_ specifying transition temperature data.     |
| 60           | EQUIV_STRESS    | A _Tuple_ specifying the equivalent stress data.      |
| 62           | Q_INFINITY      | A _Tuple_ specifying the Q infinity data.             |
| 68           | HARDENING_B     | A _Tuple_ specifying the hardening B data.            |
| 133          | TEMPERATURE_SUB | A _Tuple_ specifying the temperature sub option data. |

```psj {2-8} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                listMaterialProperty=[Plastic(plastic=[
                                    (A, [10.0]),
                                    (B, [20.0]),
                                    (M, [30.0]),
                                    (N, [40.0]),
                                    (MELTING_TEMP, [50.0]),
                                    (TRANSITION_TEMP, [60.0])],
                                    harden=2)],
                                    iMaterialID=1,
                                    iMaterialColor=16131973)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>

<summary> **`harden = User`** </summary>

| INT Notation | Key Name        | Description                                           |
| ------------ | --------------- | ----------------------------------------------------- |
| 48           | HARDENING_PROP  | A _Tuple_ specifying the hardening properties data.   |
| 60           | EQUIV_STRESS    | A _Tuple_ specifying the equivalent stress data.      |
| 62           | Q_INFINITY      | A _Tuple_ specifying the Q infinity data.             |
| 68           | HARDENING_B     | A _Tuple_ specifying the hardening B data.            |
| 133          | TEMPERATURE_SUB | A _Tuple_ specifying the temperature sub option data. |

```psj {2-3} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                listMaterialProperty=[Plastic(plastic=[
                                    (HARDENING_PROP, [10.0])],
                                    harden=3)],
                                    iMaterialID=1,
                                    iMaterialColor=16131973)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>

<details>

<summary> **`harden = Combined`** </summary>

| INT Notation | Key Name        | Description                                                         |
| ------------ | --------------- | ------------------------------------------------------------------- |
| 40           | STRESS          | A _Tuple_ specifying the yield stress data.                         |
| 41           | STRAIN          | A _Tuple_ specifying the plastic train data.                        |
| 130          | TEMPERATURE     | A _Tuple_ specifying the temperature-dependent data.                |
| 60           | EQUIV_STRESS    | A _Tuple_ specifying the equivalent stress data.                    |
| 62           | Q_INFINITY      | A _Tuple_ specifying the Q infinity data.                           |
| 68           | HARDENING_B     | A _Tuple_ specifying the hardening parameter b data.                |
| 133          | TEMPERATURE_SUB | A _Tuple_ specifying the temperature-dependent for sub option data. |
| 49           | GAMMA           | A _Tuple_ specifying the gamma data.                                |
| 50           | HARD_PARAM      | A _Tuple_ specifying the hardening parameter data.                  |

```psj {2-9} title="Sample Code"
sample_Mat = Properties.Material.Add(strMaterialName="Sample_Material",
                                    listMaterialProperty=[Plastic(plastic=[
                                        (STRESS, [0.0005]),
                                        (STRAIN, [200.0]),
                                        (TEMPERATURE, [500.0]),
                                        (EQUIV_STRESS, [200.0]),
                                        (Q_INFINITY, [10.0]),
                                        (HARDENING_B, [11.0]),
                                        (TEMPERATURE_SUB, [22.0])],
                                        harden=4,
                                        temperatureDependency=True,
                                        backStress=2,
                                        subOption_Type=3,
                                        subOption_UseTempDependent=True,
                                        subOption_UseParameter=True)],
                                        iMaterialID=1,
                                        iMaterialColor=16131973)
JPT.Debugger(sample_Mat) #for checking return value
```

</details>
