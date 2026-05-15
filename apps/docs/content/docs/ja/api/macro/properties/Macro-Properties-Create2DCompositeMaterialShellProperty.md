---
title: "Create2DCompositeMaterialShellProperty()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create property 2D composite material shell

## Syntax

```psj
Create2DCompositeMaterialShellProperty(String m _strName, color propertyColor, ??, ??, ??, Cursor ?, ??, int m _ulId, 
    Cursor m _crMatShear,Cursor m _crMatCoupl,double m _matOrient[0],double m _matOrient[1],
    double m _matOrient[2],double m _dThickness,double m _dBendStiff,double m _dThickRatio,
    double m _dNSM,double m _dFiberDist[0],double m _dFiberDist[1],double m _dPlateOff,
    int m _iItgPts,int m _matOrientType,Cursor m _crLocalCS,Cursor[] taTarget,Cursor crEdit,
    int duplicateOpt)
```

Create2DCompositeMaterialShellProperty("ComMatShell2", 13708224, 0, 1.79769e+308, 0, 22:50000000, 1.79769e+308, 3, 1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, \[6:24], 0:0, 0:0, 0, \[1.7976931e+308, 1.7976931e+308, 1.7976931e+308])

## Inputs

<!-- @since:5.1.0 -->
### 1. String

Name of property 2D composite material shell

<!-- @since:5.1.0 -->
### 2. Color

Color of the property.

<!-- @since:5.1.0 -->
### . Int

ID of property 2D shell

<!-- @since:5.1.0 -->
### 4. Cursor

Cursor of membrane material

<!-- @since:5.1.0 -->
### 5. Cursor

Cursor of bending material

<!-- @since:5.1.0 -->
### 6. Cursor

Cursor of shear material

<!-- @since:5.1.0 -->
### 7. Cursor

Cursor of coupling material

<!-- @since:5.1.0 -->
### 8. Double

Theta\[degree]

<!-- @since:5.1.0 -->
### 9. Double

Not used

<!-- @since:5.1.0 -->
### 10. Double

Not used

<!-- @since:5.1.0 -->
### 11. Double

Thickness

<!-- @since:5.1.0 -->
### 12. Double

Bending stiffness

<!-- @since:5.1.0 -->
### 13. Double

Thickness ratio

<!-- @since:5.1.0 -->
### 14. Double

Nonstructural mass

<!-- @since:5.1.0 -->
### 15. Double

Fiber dist 1

<!-- @since:5.1.0 -->
### 16. Double

Fiber dist 2

<!-- @since:5.1.0 -->
### 17. Double

Plate offset

<!-- @since:5.1.0 -->
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

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Create2DCompositeMaterialShellProperty(
    "ComMatShell1", 12901750, 0, 1.79769e+308, 0, 22:50000000, 1.79769e+308, 
    2, 1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 
    [6:22], 0:0, 0:0, 0, [1.7976931e+308, 1.7976931e+308, 1.7976931e+308])
```
