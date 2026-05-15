---
title: "Prop2DShell()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create property 2D shell

## Syntax

```psj
Prop2DShell(String m _strName,int m _ulId, color propertyColor, Cursor m _crMatMembrane,Cursor m _crMatBend,
    Cursor m _crMatShear,Cursor m _crMatCoupl,double m _matOrient[0],double m _matOrient[1],
    double m _matOrient[2],double m _dThickness,double m _dBendStiff,double m _dThickRatio,
    double m _dNSM,double m _dFiberDist[0],double m _dFiberDist[1],double m _dPlateOff,
    int m _iItgPts,int m _matOrientType,Cursor m _crLocalCS,Cursor[] taTarget,Cursor crEdit,
    int duplicateOpt, int iPanelLabelERP, string strPanelLabelName, int iPanelLabelId, int m _iTempVaraitation)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Name of property 2D shell

<!-- @since:5.0.1 -->
### 2. Int

Key of property 2D shell

<!-- @since:5.1.0 -->
### 3. Color

Color of the property.

<!-- @since:5.0.1 -->
### 4. Cursor

Cursor of membrane material

<!-- @since:5.0.1 -->
### 5. Cursor

Cursor of bending material

<!-- @since:5.0.1 -->
### 6. Cursor

Cursor of shear material

<!-- @since:5.1.0 -->
### 7. Cursor

Cursor of coupling material

<!-- @since:5.0.1 -->
### 8. Double

Theta\[degree]

<!-- @since:5.0.1 -->
### 9. Double

Not used

<!-- @since:5.0.1 -->
### 10. Double

Not used

<!-- @since:5.0.1 -->
### 11. Double

Thickness

<!-- @since:5.0.1 -->
### 12. Double

Bending stiffness

<!-- @since:5.0.1 -->
### 13. Double

Thickness ratio

<!-- @since:5.0.1 -->
### 14. Double

Nonstructural mass

<!-- @since:5.0.1 -->
### 15. Double

Fiber dist 1

<!-- @since:5.0.1 -->
### 16. Double

Fiber dist 2

<!-- @since:5.1.0 -->
### 17. Double

Plate offset

<!-- @since:5.0.1 -->
### 18. Int

No SHELL Integration points

<!-- @since:5.1.0 -->
### 19. Int

Material orientation by\[0: Theta; 1: coordinate system]

<!-- @since:5.1.0 -->
### 20. Cursor

Local coordinate system

<!-- @since:5.1.0 -->
### 21. Cursor\[]

Targets

<!-- @since:5.1.0 -->
### 22. Cursor

Edit cursor

<!-- @since:5.1.0 -->
### 23. Int

Answer of message box when targets are duplicated\[0: targets are not duplicated; 2: cancel; 6: yes; 7: no]

<!-- @since:5.1.0 -->
### 24. Int

Status of ERP check box.\[0: OFF, 1: ON]

<!-- @since:5.1.0 -->
### 25. String

Panel Label Name.

<!-- @since:5.1.0 -->
### 26. Int

Panel Label ID.

<!-- @since:5.1.0 -->
### 27. Int

The number of temperature layers.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 3. Cursor

cursor of membrane material

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 7. Double

theta\[degree]

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 17. Int

No SHELL Integration points

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 19. Cursor

local coordinate system

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 20. Cursor\[]

targets

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 21. Cursor

edit cursor

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 22. Int

answer of message box when targets are duplicated\[0: targets are not duplicated; 2: cancel; 6: yes; 7: no]

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Property2DShell("Shell Property 1", 1, 0, 22:2, 22:2, 22:2, 22:2, 1.79769e+308, 1.79769e+308,
    1.79769e+308, 0.002, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308,
    1.79769e+308, 2147483647, 0, 0:0, [3:2, 6:27], 0:0, 0, 1, "", 0, 3)
```
