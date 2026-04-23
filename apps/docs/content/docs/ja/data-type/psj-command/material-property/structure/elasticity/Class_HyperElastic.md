---
title: HyperElastic
id: HyperElastic
---

## Description

This is an instance of a Hyperelastic class, represents Hyperelastic characteristic of material.

## Properties

| Attribute                     | Description                                                                                                  |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------ |
| hyperElastic                  | A _List of Tuple_ specifying all data of [Hyperelastic characteristic](#hyperelastic-characteristic). <br /> |
| hyperElasticType              | A _String_ specifying the type of Hyperelastic.                                                              |
| moduli                        | A _String_ specifying the moduli time scale type (for ViscoElasticity).                                      |
| inputSource                   | An _Integer_ specifying the source input.                                                                    |
| temperatureDependency         | A _Boolean_ specifying the use of temperature-dependent data.                                                |
| strainEnergyPotentialOrder    | An _Integer_ specifying the strain energy potential order.                                                   |
| beta                          | A _String_ specifying the beta parameter.                                                                    |
| compressible                  | A _Boolean_ specifying the use of compressible option.                                                       |
| properties                    | An _Integer_ specifying the use of properties.                                                               |
| deviatoricResponse            | A _String_ specifying the deviatoric response.                                                               |
| volumetricResponse            | A _String_ specifying the volumetric response.                                                               |
| poissonRatio                  | A _Float_ specifying the poisson ratio.                                                                      |
| shearModulusDamping           | A _Float_ specifying the shear modulus damping.                                                              |
| limiStressDamping             | A _Float_ specifying the limit stress damping.                                                               |
| dependencies                  | An _Integer_ specifying the number of field variables.                                                       |
| applySmooth                   | A _Boolean_ the use of smooth applying.                                                                      |
| smoothing                     | An _Integer_ specifying the smoothing.                                                                       |
| includeLateralNormalStrain    | A _Boolean_ specifying the including lateral normal strain.                                                  |
| uniaxialTemperatureDependency | A _Boolean_ specifying the use of uniaxial temperature dependency.                                           |
| uniaxialDependencies          | An _Integer_ specifying the uniaxial dependencies.                                                           |
| bstart                        | A _Float_ specifying the BSTART in test data editor.                                                         |
| tramp                         | A _Float_ specifying the TRAMP in test data editor.                                                          |

## Hyperelastic Characteristic {#hyperelastic-characteristic}

Either `KEY NAME` or `ID` can be used to define the material property.
The ID of material property which was primarily used in functions can be referred to in the [Int Notation](../../../material-types) column.
However, in order to explicitly describe meaning of material properties, user can use the `KEY NAME` instead of specifying `ID`.
For example: `PRESSURE_FORCE_LOADING` is equal to ID = 63.\

<details>

<summary> **`strainEnergyPotentialOrder = ARRUDA_BOYCE`** </summary>

| INT Notation | Key Name              | Description                                          |
| ------------ | --------------------- | ---------------------------------------------------- |
| 92           | MU                    | A _Tuple_ specifying the MU data.                    |
| 93           | LAMDA_M               | A _Tuple_ specifying the lamda data.                 |
| 94           | D                     | A _Tuple_ specifying the D data.                     |
| 130          | TEMPERATURE           | A _Tuple_ specifying the temperature data.           |
| 110          | NOMIAL_STRESS         | A _Tuple_ specifying the nomial stress data.         |
| 111          | NOMIAL_STRAIN         | A _Tuple_ specifying the nomial strain data.         |
| 112          | LATERAL_NOMIAL_STRAIN | A _Tuple_ specifying the lateral nomial strain data. |
| 136          | TEMPERATURE_UNIAXIAL  | A _Tuple_ specifying the uniaxial temperature data.  |
| 149          | EXTRA_FIELDS_UNIAXIAL | A _Tuple_ specifying the extra uniaxial fields data. |
| 40           | STRESS                | A _Tuple_ specifying the yield stress data.          |
| 113          | TIME                  | A _Tuple_ specifying the time data.                  |

```py {2-6} title="Sample Code"
structure_steel = Properties.Material.Modify(strMaterialName="Structural_Steel",
    dictMaterialProperty={'HyperElastic': {'hyperElasticType': 'ARRUDA_BOYCE', 'moduli': 'LONG_TERM',
    'inputSource': 1, 'hyperElastic': {'MU': [3.5e-07], 'LAMDA_M': [1.2], 'D': [3000000.0],
    'TEMPERATURE': [423.15], 'NOMIAL_STRESS': [0.000112], 'NOMIAL_STRAIN': [130.0],
    'LATERAL_NOMIAL_STRAIN': [50.0], 'TEMPERATURE_UNIAXIAL': [288.15],
    'EXTRA_FIELDS_UNIAXIAL': [[80.0], [70.0]], 'STRESS': [0.00032], 'TIME': [124.0]},
    'temperatureDependency': 'True', 'volumetricResponse': 'POISSON_RATIO', 'applySmooth': True,
    'smoothing': 3, 'includeLateralNormalStrain': True, 'uniaxialTemperatureDependency': True,
    'uniaxialDependencies': 2, 'bstart': 25.0, 'tramp': 15.0}}, iMaterialID=1, iMaterialColor=1415085)

JPT.Debugger(structure_steel) #for checking return value
```

</details>
<details>

<summary> **`strainEnergyPotentialOrder = MARLOW`** </summary>

| INT Notation | Key Name              | Description                                          |
| ------------ | --------------------- | ---------------------------------------------------- |
| 110          | NOMIAL_STRESS         | A _Tuple_ specifying the nomial stress data.         |
| 111          | NOMIAL_STRAIN         | A _Tuple_ specifying the nomial strain data.         |
| 112          | LATERAL_NOMIAL_STRAIN | A _Tuple_ specifying the lateral nomial strain data. |
| 136          | TEMPERATURE_UNIAXIAL  | A _Tuple_ specifying the uniaxial temperature data.  |
| 149          | EXTRA_FIELDS_UNIAXIAL | A _Tuple_ specifying the extra uniaxial fields data. |
| 40           | STRESS                | A _Tuple_ specifying the yield stress data.          |
| 113          | TIME                  | A _Tuple_ specifying the time data.                  |

```py {2-5} title="Sample Code"
structure_steel = Properties.Material.Modify(strMaterialName="Structural_Steel",
    dictMaterialProperty={'HyperElastic': {'hyperElasticType': 'MARLOW', 'moduli': 'LONG_TERM',
    'inputSource': 0, 'hyperElastic': {'NOMIAL_STRESS': [0.00011], 'NOMIAL_STRAIN': [75.0],
    'LATERAL_NOMIAL_STRAIN': [100.0], 'TEMPERATURE_UNIAXIAL': [318.15],
    'EXTRA_FIELDS_UNIAXIAL': [[150.0], [180.0]], 'STRESS': [2e-05], 'TIME': [45.0]},
    'deviatoricResponse': 'UNIAXIAL', 'volumetricResponse': 'VOLUMETRIC_DATA', 'applySmooth': True,
    'smoothing': 3, 'includeLateralNormalStrain': True, 'uniaxialTemperatureDependency': True,
    'uniaxialDependencies': 2, 'bstart': 15.0, 'tramp': 36.0}}, iMaterialID=1, iMaterialColor=13770132)

JPT.Debugger(structure_steel) #for checking return value
```

</details>
<details>

<summary> **`strainEnergyPotentialOrder = MOONEY_RIVLIN`** </summary>

| INT Notation | Key Name              | Description                                          |
| ------------ | --------------------- | ---------------------------------------------------- |
| 110          | NOMIAL_STRESS         | A _Tuple_ specifying the nomial stress data.         |
| 111          | NOMIAL_STRAIN         | A _Tuple_ specifying the nomial strain data.         |
| 112          | LATERAL_NOMIAL_STRAIN | A _Tuple_ specifying the lateral nomial strain data. |
| 136          | TEMPERATURE_UNIAXIAL  | A _Tuple_ specifying the uniaxial temperature data.  |
| 149          | EXTRA_FIELDS_UNIAXIAL | A _Tuple_ specifying the extra uniaxial fields data. |
| 40           | STRESS                | A _Tuple_ specifying the yield stress data.          |
| 113          | TIME                  | A _Tuple_ specifying the time data.                  |

```py {2-5} title="Sample Code"
structure_steel = Properties.Material.Modify(strMaterialName="Structural_Steel",
    dictMaterialProperty={'HyperElastic': {'hyperElasticType': 'MOONEY_RIVLIN',
    'moduli': 'LONG_TERM', 'inputSource': 0, 'hyperElastic': {'NOMIAL_STRESS': [7.999999999999999e-05],
    'NOMIAL_STRAIN': [110.0], 'LATERAL_NOMIAL_STRAIN': [30.0], 'TEMPERATURE_UNIAXIAL': [343.15],
    'EXTRA_FIELDS_UNIAXIAL': [[120.0], [100.0]], 'STRESS': [1.5e-05], 'TIME': [360.0]},
    'volumetricResponse': 'VOLUMETRIC_DATA', 'strainEnergyPotentialOrder': 1, 'applySmooth': True,
    'smoothing': 3, 'includeLateralNormalStrain': True, 'uniaxialTemperatureDependency': True,
    'uniaxialDependencies': 2, 'bstart': 10.0, 'tramp': 25.0}}, iMaterialID=1, iMaterialColor=12901750)

JPT.Debugger(structure_steel) #for checking return value
```

</details>
<details>

<summary> **`strainEnergyPotentialOrder = NEO_HOOKE`** </summary>

| INT Notation | Key Name              | Description                                          |
| ------------ | --------------------- | ---------------------------------------------------- |
| 110          | NOMIAL_STRESS         | A _Tuple_ specifying the nomial stress data.         |
| 111          | NOMIAL_STRAIN         | A _Tuple_ specifying the nomial strain data.         |
| 112          | LATERAL_NOMIAL_STRAIN | A _Tuple_ specifying the lateral nomial strain data. |
| 136          | TEMPERATURE_UNIAXIAL  | A _Tuple_ specifying the uniaxial temperature data.  |
| 149          | EXTRA_FIELDS_UNIAXIAL | A _Tuple_ specifying the extra uniaxial fields data. |
| 40           | STRESS                | A _Tuple_ specifying the yield stress data.          |
| 113          | TIME                  | A _Tuple_ specifying the time data.                  |

```py {2-5} title="Sample Code"
structure_steel = Properties.Material.Add(strMaterialName="Structural_Steel",
    dictMaterialProperty={'HyperElastic': {'hyperElasticType': 'NEO_HOOKE', 'moduli': 'LONG_TERM',
    'inputSource': 0, 'hyperElastic': {'NOMIAL_STRESS': [9.999999999999999e-05], 'NOMIAL_STRAIN': [45.0],
    'LATERAL_NOMIAL_STRAIN': [25.0], 'TEMPERATURE_UNIAXIAL': [343.15],
    'EXTRA_FIELDS_UNIAXIAL': [[150.0], [300.0]], 'STRESS': [1.2e-05], 'TIME': [36.0]},
    'volumetricResponse': 'VOLUMETRIC_DATA', 'strainEnergyPotentialOrder': 1, 'applySmooth': True,
    'smoothing': 3, 'includeLateralNormalStrain': True, 'uniaxialTemperatureDependency': True,
    'uniaxialDependencies': 2, 'bstart': 5.0, 'tramp': 45.0}}, iMaterialID=1, iMaterialColor=16131973)

JPT.Debugger(structure_steel) #for checking return value
```

</details>
<details>

<summary> **`strainEnergyPotentialOrder = OGDEN`** </summary>

| INT Notation | Key Name              | Description                                          |
| ------------ | --------------------- | ---------------------------------------------------- |
| 110          | NOMIAL_STRESS         | A _Tuple_ specifying the nomial stress data.         |
| 111          | NOMIAL_STRAIN         | A _Tuple_ specifying the nomial strain data.         |
| 112          | LATERAL_NOMIAL_STRAIN | A _Tuple_ specifying the lateral nomial strain data. |
| 136          | TEMPERATURE_UNIAXIAL  | A _Tuple_ specifying the uniaxial temperature data.  |
| 149          | EXTRA_FIELDS_UNIAXIAL | A _Tuple_ specifying the extra uniaxial fields data. |
| 40           | STRESS                | A _Tuple_ specifying the yield stress data.          |
| 113          | TIME                  | A _Tuple_ specifying the time data.                  |

```py {2-5} title="Sample Code"
structure_steel = Properties.Material.Modify(strMaterialName="Structural_Steel",
    dictMaterialProperty={'HyperElastic': {'hyperElasticType': 'OGDEN', 'moduli': 'LONG_TERM',
    'inputSource': 0, 'hyperElastic': {'NOMIAL_STRESS': [5.999999999999999e-05], 'NOMIAL_STRAIN': [15.0],
    'LATERAL_NOMIAL_STRAIN': [130.0], 'TEMPERATURE_UNIAXIAL': [358.15],
    'EXTRA_FIELDS_UNIAXIAL': [[80.0], [150.0]], 'STRESS': [5.5e-05], 'TIME': [25.0]},
    'volumetricResponse': 'VOLUMETRIC_DATA', 'strainEnergyPotentialOrder': 1, 'applySmooth': True,
    'smoothing': 3, 'includeLateralNormalStrain': True, 'uniaxialTemperatureDependency': True,
    'uniaxialDependencies': 2, 'bstart': 50.0, 'tramp': 20.0}}, iMaterialID=1, iMaterialColor=16131973)

JPT.Debugger(structure_steel) #for checking return value
```

</details>
<details>

<summary> **`strainEnergyPotentialOrder = POLYNOMIAL`** </summary>

| INT Notation | Key Name              | Description                                          |
| ------------ | --------------------- | ---------------------------------------------------- |
| 95           | C10                   | A _Tuple_ specifying the C10 data.                   |
| 96           | C01                   | A _Tuple_ specifying the C10 data.                   |
| 107          | D1                    | A _Tuple_ specifying the D1 data.                    |
| 130          | TEMPERATURE           | A _Tuple_ specifying the temperature data.           |
| 110          | NOMIAL_STRESS         | A _Tuple_ specifying the nomial stress data.         |
| 111          | NOMIAL_STRAIN         | A _Tuple_ specifying the nomial strain data.         |
| 112          | LATERAL_NOMIAL_STRAIN | A _Tuple_ specifying the lateral nomial strain data. |
| 136          | TEMPERATURE_UNIAXIAL  | A _Tuple_ specifying the uniaxial temperature data.  |
| 149          | EXTRA_FIELDS_UNIAXIAL | A _Tuple_ specifying the extra uniaxial fields data. |
| 40           | STRESS                | A _Tuple_ specifying the yield stress data.          |
| 113          | TIME                  | A _Tuple_ specifying the time data.                  |

```py {2-6} title="Sample Code"
structure_steel = Properties.Material.Modify(strMaterialName="Structural_Steel",
    dictMaterialProperty={'HyperElastic': {'hyperElasticType': 'POLYNOMIAL', 'moduli': 'LONG_TERM',
    'inputSource': 1, 'hyperElastic': {'C10': [3.5e-05], 'C01': [1.5e-05], 'D1': [30000000.0],
    'TEMPERATURE': [473.15], 'NOMIAL_STRESS': [0.000112], 'NOMIAL_STRAIN': [130.0],
    'LATERAL_NOMIAL_STRAIN': [50.0], 'TEMPERATURE_UNIAXIAL': [288.15],
    'EXTRA_FIELDS_UNIAXIAL': [[80.0], [70.0]], 'STRESS': [0.00032], 'TIME': [124.0]},
    'temperatureDependency': 'True', 'volumetricResponse': 'POISSON_RATIO',
    'strainEnergyPotentialOrder': 1, 'applySmooth': True, 'smoothing': 3,
    'includeLateralNormalStrain': True, 'uniaxialTemperatureDependency': True, 'uniaxialDependencies': 2,
    'bstart': 25.0, 'tramp': 15.0}}, iMaterialID=1, iMaterialColor=1415085)

JPT.Debugger(structure_steel) #for checking return value
```

</details>
<details>

<summary> **`strainEnergyPotentialOrder = REDUCED_POLYNOMIAL`** </summary>

| INT Notation | Key Name              | Description                                          |
| ------------ | --------------------- | ---------------------------------------------------- |
| 95           | C10                   | A _Tuple_ specifying the C10 data.                   |
| 107          | D1                    | A _Tuple_ specifying the D1 data.                    |
| 130          | TEMPERATURE           | A _Tuple_ specifying the temperature data.           |
| 110          | NOMIAL_STRESS         | A _Tuple_ specifying the nomial stress data.         |
| 111          | NOMIAL_STRAIN         | A _Tuple_ specifying the nomial strain data.         |
| 112          | LATERAL_NOMIAL_STRAIN | A _Tuple_ specifying the lateral nomial strain data. |
| 136          | TEMPERATURE_UNIAXIAL  | A _Tuple_ specifying the uniaxial temperature data.  |
| 149          | EXTRA_FIELDS_UNIAXIAL | A _Tuple_ specifying the extra uniaxial fields data. |
| 40           | STRESS                | A _Tuple_ specifying the yield stress data.          |
| 113          | TIME                  | A _Tuple_ specifying the time data.                  |

```py {2-6} title="Sample Code"
structure_steel = Properties.Material.Modify(strMaterialName="Structural_Steel",
    dictMaterialProperty={'HyperElastic': {'hyperElasticType': 'REDUCED_POLYNOMIAL',
    'moduli': 'LONG_TERM', 'inputSource': 1, 'hyperElastic': {'C10': [9.999999999999999e-06],
    'D1': [15000000.0], 'TEMPERATURE': [473.15], 'NOMIAL_STRESS': [0.000112],
    'NOMIAL_STRAIN': [130.0], 'LATERAL_NOMIAL_STRAIN': [50.0], 'TEMPERATURE_UNIAXIAL': [288.15],
    'EXTRA_FIELDS_UNIAXIAL': [[80.0], [70.0]], 'STRESS': [0.00032], 'TIME': [124.0]},
    'temperatureDependency': 'True', 'volumetricResponse': 'POISSON_RATIO', 'strainEnergyPotentialOrder': 1,
    'applySmooth': True, 'smoothing': 3, 'includeLateralNormalStrain': True,
    'uniaxialTemperatureDependency': True, 'uniaxialDependencies': 2, 'bstart': 25.0, 'tramp': 15.0}},
    iMaterialID=1, iMaterialColor=1415085)

JPT.Debugger(structure_steel) #for checking return value
```

</details>
<details>

<summary> **`strainEnergyPotentialOrder = USER`** </summary>

| INT Notation | Key Name              | Description                                          |
| ------------ | --------------------- | ---------------------------------------------------- |
| 110          | NOMIAL_STRESS         | A _Tuple_ specifying the nomial stress data.         |
| 111          | NOMIAL_STRAIN         | A _Tuple_ specifying the nomial strain data.         |
| 112          | LATERAL_NOMIAL_STRAIN | A _Tuple_ specifying the lateral nomial strain data. |
| 136          | TEMPERATURE_UNIAXIAL  | A _Tuple_ specifying the uniaxial temperature data.  |
| 149          | EXTRA_FIELDS_UNIAXIAL | A _Tuple_ specifying the extra uniaxial fields data. |
| 40           | STRESS                | A _Tuple_ specifying the yield stress data.          |
| 113          | TIME                  | A _Tuple_ specifying the time data.                  |

```py {2-5} title="Sample Code"
structure_steel = Properties.Material.Modify(strMaterialName="Structural_Steel",
    dictMaterialProperty={'HyperElastic': {'hyperElasticType': 'USER', 'moduli': 'LONG_TERM',
    'inputSource': 1, 'hyperElastic': {'NOMIAL_STRESS': [0.000112], 'NOMIAL_STRAIN': [130.0],
    'LATERAL_NOMIAL_STRAIN': [50.0], 'TEMPERATURE_UNIAXIAL': [288.15],
    'EXTRA_FIELDS_UNIAXIAL': [[80.0], [70.0]], 'STRESS': [0.00032], 'TIME': [124.0]},
    'temperatureDependency': 'True', 'compressible': True, 'properties': 10, 'applySmooth': True,
    'smoothing': 3, 'includeLateralNormalStrain': True, 'uniaxialTemperatureDependency': True,
    'uniaxialDependencies': 2, 'bstart': 25.0, 'tramp': 15.0}}, iMaterialID=1, iMaterialColor=1415085)

JPT.Debugger(structure_steel) #for checking return value
```

</details>
<details>

<summary> **`strainEnergyPotentialOrder = VAN_DER_WAALS`** </summary>

| INT Notation | Key Name              | Description                                          |
| ------------ | --------------------- | ---------------------------------------------------- |
| 92           | MU                    | A _Tuple_ specifying the MU data.                    |
| 93           | LAMDA_M               | A _Tuple_ specifying the lamda data.                 |
| 69           | ALPHA                 | A _Tuple_ specifying the Alpha data.                 |
| 100          | BETA                  | A _Tuple_ specifying the Beta data.                  |
| 94           | D                     | A _Tuple_ specifying the D data.                     |
| 130          | TEMPERATURE           | A _Tuple_ specifying the temperature data.           |
| 110          | NOMIAL_STRESS         | A _Tuple_ specifying the nomial stress data.         |
| 111          | NOMIAL_STRAIN         | A _Tuple_ specifying the nomial strain data.         |
| 112          | LATERAL_NOMIAL_STRAIN | A _Tuple_ specifying the lateral nomial strain data. |
| 136          | TEMPERATURE_UNIAXIAL  | A _Tuple_ specifying the uniaxial temperature data.  |
| 149          | EXTRA_FIELDS_UNIAXIAL | A _Tuple_ specifying the extra uniaxial fields data. |
| 40           | STRESS                | A _Tuple_ specifying the yield stress data.          |
| 113          | TIME                  | A _Tuple_ specifying the time data.                  |

```py {2-6} title="Sample Code"
structure_steel = Properties.Material.Modify(strMaterialName="Structural_Steel",
    dictMaterialProperty={'HyperElastic': {'hyperElasticType': 'VAN_DER_WAALS', 'moduli': 'LONG_TERM',
    'inputSource': 1, 'hyperElastic': {'MU': [3e-07], 'LAMDA_M': [0.5], 'ALPHA': [3.0], 'BETA': [2.5],
    'D': [10000000.0], 'TEMPERATURE': [423.15], 'NOMIAL_STRESS': [0.000112], 'NOMIAL_STRAIN': [130.0],
    'LATERAL_NOMIAL_STRAIN': [50.0], 'TEMPERATURE_UNIAXIAL': [288.15],
    'EXTRA_FIELDS_UNIAXIAL': [[80.0], [70.0]], 'STRESS': [0.00032], 'TIME': [124.0]},
    'temperatureDependency': 'True', 'volumetricResponse': 'POISSON_RATIO', 'beta': {'100': [2.5]},
    'applySmooth': True, 'smoothing': 3, 'includeLateralNormalStrain': True,
    'uniaxialTemperatureDependency': True, 'uniaxialDependencies': 2, 'bstart': 25.0, 'tramp': 15.0}},
    iMaterialID=1, iMaterialColor=1415085)

JPT.Debugger(structure_steel) #for checking return value
```

</details>
<details>

<summary> **`strainEnergyPotentialOrder = YEOH`** </summary>

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

```py {2-7} title="Sample Code"
structure_steel = Properties.Material.Modify(strMaterialName="Structural_Steel",
    dictMaterialProperty={'HyperElastic': {'hyperElasticType': 'YEOH', 'moduli': 'LONG_TERM',
    'inputSource': 1, 'hyperElastic': {'C00': [0.00012], 'C20': [5e-05], 'C30': [2e-06],
    'D1': [15000000.0], 'D2': [20000000.0], 'D3': [10000000.0], 'TEMPERATURE': [423.15],
    'NOMIAL_STRESS': [0.000112], 'NOMIAL_STRAIN': [130.0], 'LATERAL_NOMIAL_STRAIN': [50.0],
    'TEMPERATURE_UNIAXIAL': [288.15], 'EXTRA_FIELDS_UNIAXIAL': [[80.0], [70.0]], 'STRESS': [0.00032],
    'TIME': [124.0]}, 'temperatureDependency': 'True', 'volumetricResponse': 'POISSON_RATIO',
    'strainEnergyPotentialOrder': 1, 'applySmooth': True, 'smoothing': 3,
    'includeLateralNormalStrain': True, 'uniaxialTemperatureDependency': True, 'uniaxialDependencies': 2,
    'bstart': 25.0, 'tramp': 15.0}}, iMaterialID=1, iMaterialColor=1415085)


JPT.Debugger(structure_steel) #for checking return value
```

</details>
