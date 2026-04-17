---
title: FatigueCrackGrowth
id: FatigueCrackGrowth
---

## Description

This is an instance of a Fatigue Crack Growth class, represents Fatigue Crack Growth characteristic of material.

## Properties

| Attribute            | Description                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Fatigue Crack Growth | A _List of Tuple_ specifying all data of [Fatigue Crack Growth characteristic](#fatiguecrackgrowth-characteristic). <br /> |

## Fatigue Crack Growth Characteristic {#fatiguecrackgrowth-characteristic}

Either `KEY NAME` or `ID` can be used to define the material property.
The ID of material property which was primarily used in functions can be referred to in the [Int Notation](../../material-types) column.
However, in order to explicitly describe meaning of material properties, user can use the `KEY NAME` instead of specifying `ID`.
For example: `PRESSURE_FORCE_LOADING` is equal to ID = 63.

| INT Notation | Key Name                | Description                                         |
| ------------ | ----------------------- | --------------------------------------------------- |
| 156          | FATIGUE_GROWTH_CONSTANT | A _Tuple_ specifying the constant of crack growth C |
| 157          | FATIGUE_GROWTH_EXPONENT | A _Tuple_ specifying the exponent of crack growth m |
| 158          | FATIGUE_GROWTH_CRIT_DMG | A _Tuple_ specifying the critical damage            |

```psj {2-14} title="Sample Code"
sample_Mat = Properties.Material.Add(
    strMaterialName="Sample_Material",
    dictMaterialProperty={
        'FatigueCrackGrowth': {
            'fatigueCrackGrowth': {
                'FATIGUE_GROWTH_CONSTANT': [0.3],
                'FATIGUE_GROWTH_EXPONENT': [0.1],
                'FATIGUE_GROWTH_CRIT_DMG': [0.5]
            }
        }
    },
    iMaterialID=1,
    iMaterialColor=16131973
)

JPT.Debugger(sample_Mat) #for checking return value
```
