---
title: RDNLK
id: RDNLK
---

## Description

This is an instance of a Plastic class, represents Plastic characteristic of material.

## Properties

| Attribute                  | Description                                                                                                                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| plastic                    | A _List of Tuple_ specifying all data of Plastic characteristic. <br /> The data includes STRESS, STRAIN, STRAIN_RATE, TEMPERATURE, and EXTRA_FIELDS. |
| harden                     | An _Integer_ specifying the hardening option.                                                                                                         |
| curve                      | An _Integer_ specifying the curve option.                                                                                                             |
| curve_ForCombined          | An _Integer_ specifying the curve option that is using in Combined Hardening, this param is different from the “curve” above.                         |
| dataType                   | An _Integer_ specifying data option in Combined Hardening.                                                                                            |
| temperatureDependency      | A _Boolean_ specifying the use of temperature-dependent data.                                                                                         |
| dependencies               | An _Integer_ specifying the number of dependencies in temperature.                                                                                    |
| useStrain                  | A _Boolean_ specifying the option use Strain in Combined Hardening and Isotropic.                                                                     |
| exportAdvc                 | A _Boolean_ specifying the use of exporting ADVC Format.                                                                                              |
| backStress                 | An _Integer_ specifying the number of back stresses in Combined Hardening.                                                                            |
| subOption_Type             | An _Integer_ specifying the type of sub option                                                                                                        |
| subOption_FieldNum         | An _Integer_ specifying the number of fields used for sub option.                                                                                     |
| subOption_UseTempDependent | A _Boolean_ specifying the use of temperature for sub option.                                                                                         |
| subOption_UseParameter     | A _Boolean_ specifying the use of parameter for sub option.                                                                                           |

## Sample Code

```psj {1-4}
structure_steel = Properties.Material.Add(strMaterialName="Structural_Steel",
    listMaterialProperty=[Density([(DENSITY, 7.85e-09)]),
    Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])],
    iMaterialID=5)

JPT.Debugger(structure_steel) #for checking return value
```
