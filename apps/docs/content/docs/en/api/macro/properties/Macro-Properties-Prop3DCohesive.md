---
title: "Prop3DCohesive()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create property 3d cohesive

## Syntax

```psj
Prop3DCohesive(string strName, color propertyColor, cursor crMaterial, int iResponse, int iSpecifyThick,
double dInitialThick, cursor[] taTarget, cursor crEdit, int FLG, int iID, int iSolverType,
int iADVCResponseType, int iADVCStackDir, bool bADVCThickness, double dADVCThickness)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Prop3DCohesive name

<!-- @since:5.1.0 -->
### 2. Color

Color of the property.

<!-- @since:5.1.0 -->
### 3. Cursor

Material cursor(22:Material ID)

<!-- @since:5.0.1 -->
### 4. Int

Response type

- 0: Traction Separation
- 1: Continuum
- 2: Gasket

<!-- @since:5.1.0 -->
### 5. Int

Initial thickness type

- 0: Geometry
- 1: Specified

<!-- @since:5.1.0 -->
### 6. Double

Initial thickness value, corresponding to cohesive solver type 0

<!-- @since:5.1.0 -->
### 7. Cursor\[]

Target entities cursor

<!-- @since:5.1.0 -->
### 8. Cursor

Edit Cursor

<!-- @since:5.0.1 -->
### 9. Int

FLG

<!-- @since:5.0.1 -->
### 10. Int

Property ID

<!-- @since:5.0.1 -->
### 11. Int

Cohesive solver type

- 0: ABAQUS
- 1: ADVC

<!-- @since:5.0.1 -->
### 12. Int

ADVC response type

- 0: Continuum
- 1: Continuum2

<!-- @since:5.1.0 -->
### 13. Int

Stack direction type

- 0: Blank
- 1: Stack 0
- 2: Stack 1
- 3: Stack 2

<!-- @since:5.1.0 -->
### 14. Bool

ADVC thickness bool flag True = 1, False = 0

<!-- @since:5.1.0 -->
### 15. Double

ADVC thickness value

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 2. Cursor

Material cursor(22:Material ID)

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 3. Int

Response type

- 0: Traction Separation
- 1: Continuum
- 2: Gasket

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 5. Double

Initial thickness value, corresponding to cohesive solver type 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 6. Cursor\[]

Target entities cursor

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 7. Cursor

Edit Cursor

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 8. Int

FLG

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 13. Bool

ADVC thickness bool flag True = 1, False = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 14. Double

ADVC thickness value

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Prop3DCohesive("Cohensive Property 8", 9011056, 22:5, 2, 1, 20, [3:1], 0:0, 1, 6, 0, 0, 3, 1, 10)
```
