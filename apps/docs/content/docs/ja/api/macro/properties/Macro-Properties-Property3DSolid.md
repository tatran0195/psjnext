---
title: "Property3DSolid()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create property 3D solid

## Syntax

```psj
Property3DSolid(string Name, int Id, color propertyColor, Cursor Material, int CordM, int iN, int OutLoc,
    int ISOP, int iFLflag, int ModifiedElem, int ModifiedElemADVC, bool HasDynaRemesh,
    double DynaRemeshValMin, double DynaRemeshValMax, int HGType, int DispHG,
    Cursor[] Target, Cursor crEdit, int FLG)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Name Property 3d solid

<!-- @since:5.0.1 -->
### 2. Int

ID

<!-- @since:5.1.0 -->
### 3. Color

Color of the property.

<!-- @since:5.1.0 -->
### 4. Cursor

Material

<!-- @since:5.0.1 -->
### 5. Int

Material coordinate \[0:blank; 1:Element CS; 2:Global]

<!-- @since:5.0.1 -->
### 6. Int

Integrating network \[0:blank; 1:TWO; 2:THREE; 3:BUBBLE]

<!-- @since:5.0.1 -->
### 7. Int

Output location \[0:blank; 1:GAUSS; 2:GRID]

<!-- @since:5.0.1 -->
### 8. Int

Integrating schema\[0:blank; 1:REDUCED; 2:FULL]

<!-- @since:5.0.1 -->
### 9. Int

Fluid element flag\[0:blank; 1:PFLUID; 2:SMECH]

<!-- @since:5.0.1 -->
### 10. Int

A bitmask-type flag used to switch the modified element type (Abaqus solver).

- 0 : Don't use any Modified element (binary 000000)
- 1 : Using the Hybrid element (binary 000001)
- 2 : Using the Incompatible element (binary 000010)
- 4 : Using the Modified element (binary 000100)
- 8 : Using the Degenerate Integral element (binary 001000)
- 16 : Using the Coupled Temp-Disp element (binary 100000)
- 32 : Using the Acoustic solid element (binary 100000)

<!-- @since:5.1.0 -->
### 11. Int

A bitmask-type flag used to switch the modified element type (ADVC solver). Based on the specified value, the element formulation and handling within the mesh are switched.

- 0 : Don't use any Modified element (binary 000000)
- 2 : Using the Non-conforming element (binary 000010)
- 4 : Using the Modified element (binary 000100)
- 8 : Using the Degenerate Integral element (binary 001000)
- 256 : Using the First-order solid element (binary 100000000)
- 512 : Using the Incompatible solid element (binary 1000000000)
- 1024: Using the u-p formulation solid element (binary 10000000000)

<!-- @since:5.1.0 -->
### 12. Bool

Has Dyna Remesh flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 13. Double

Remesh \[Min Edge Length]

<!-- @since:5.1.0 -->
### 14. Double

Remesh\[Max Edge Length]

<!-- @since:5.1.0 -->
### 15. Int

Hourglass Type \[Use Default;Enhanced;Stiffness]

<!-- @since:5.1.0 -->
### 16. double

Displacement Hourglass

<!-- @since:5.1.0 -->
### 17. Cursor\[]

Target list

<!-- @since:5.1.0 -->
### 18. Cursor

Edit target (3D Property)

<!-- @since:5.1.0 -->
### 19. Int

FLG

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 3. Cursor

Material

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 4. Int

Material coordinate \[0:blank; 1:Element CS; 2:Global]

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 11. Bool

Has Dyna Remesh flag true = 1, false = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 12. Double

Remesh \[Min Edge Length]

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 14. Int

Hourglass Type \[Use Default;Enhanced;Stiffness]

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 15. double

Displacement Hourglass

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 16. Cursor\[]

Target list

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 17. Cursor

Edit 1D beam

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 18. Int

FLG

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Property3DSolid("Solid Property 1", 1, 16131973, 22:1, -2, 0, 0, 0, 0, 0, 0, 0,
    1.79769e+308, 1.79769e+308, 0, 1.79769e+308, [3:1], 0:0, -1)
```
