---
title: "Property1DRod()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

1D Rod property

## Syntax

```psj
Property1DRod(string strName, int ID, color propertyColor, cursor crSection, cursor DataMat,
    double dAreaVal, double dTorsConst, double dTorsStress, double dNonstMass,
    int dLocalLengthUnit, int iLocalMassUnit, cursor[] taTarget, cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Property 1D rod name

<!-- @since:5.0.1 -->
### 2. Int

Property 1D ID input

<!-- @since:5.1.0 -->
### 3. Color

Color of the property.

<!-- @since:5.0.1 -->
### 4. Cursor

Section cursor(93:SectionGeneral ID)

<!-- @since:5.1.0 -->
### 5. Cursor

Data material cursor(22:Material ID)

<!-- @since:5.0.1 -->
### 6. Double

Area value

<!-- @since:5.0.1 -->
### 7. Double

Torsional const value

<!-- @since:5.0.1 -->
### 8. Double

Torsional stress coefficient

<!-- @since:5.1.0 -->
### 9. Double

Nonstruct Mass

<!-- @since:5.0.1 -->
### 10. Int

Input length unit

- 0: Mm
- 1: M
- 2: Ft
- 3: In
- 4: Cm

<!-- @since:5.1.0 -->
### 11. Int

Input mass unit

- 1: blank
- 0: T
- 1: kg
- 2: kgf\*s^2/mm
- 3: Lbf\*s^2/in

<!-- @since:5.1.0 -->
### 12. Cursor\[]

Target entities cursor

<!-- @since:5.1.0 -->
### 13. Cursor

Edit cursor

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 3. Cursor

Section cursor(93:SectionGeneral ID)

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 5. Double

Area value

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 9. Int

Input length unit

- 0: Mm
- 1: M
- 2: Ft
- 3: In
- 4: Cm

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 11. Cursor\[]

Target entities cursor

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 12. Cursor

Edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Property1DRod("ROD10", 8, 10239814, 93:1, 22:6, 1e-05, 2e-12, 4, 3e+06, 0, 0, [5:53], 0:0)
```
