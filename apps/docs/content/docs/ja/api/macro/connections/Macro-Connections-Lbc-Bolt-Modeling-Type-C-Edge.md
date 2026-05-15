---
title: "Lbc _Bolt _Modeling _Type _C_Edge()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Lbc TypeC Bolt Edge method

## Syntax

```psj
Lbc _Bolt _Modeling _Type _C_Edge(Cursor taEdgeCur1,Cursor taEdgeCur2,string strRbeName,
    double dPlaneTol,double dMaxBoltHeight,int nConnectionType, int nCoincidentNodes,
    double dTolerance, int nGround,double dStiffnessX,double dStiffnessY,double dStiffnessZ,
    int nLocalStiffUnit,double dRotateStiffX,double dRotateStiffY,double dRotateStiffZ,
    int nLocalRotateStiffUnit, double dDampCoef, double dStressCoef,Cursor curCoord,
    int nTopRbeType,double dTopPitch,double dTopRemoveDepth,int nBotRbeType,double dBotPitch,
    double dBotRemoveDepth)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

faces with circular edges in top side

<!-- @since:5.0.1 -->
### 2. Cursor\[]

faces with circular edges in bottom side

<!-- @since:5.0.1 -->
### 3. String

name of Rbe

<!-- @since:5.0.1 -->
### 4. Double

Plane tolerance angle around the selected edge.

<!-- @since:5.0.1 -->
### 5. Double

Maximum distance between top and bottom rbe

<!-- @since:5.0.1 -->
### 6. Int

connection type,0 = Spring,1 = Rbe2

<!-- @since:5.0.1 -->
### 7. Int

Coincident Nodes

<!-- @since:5.0.1 -->
### 8. Double

Tolerance

<!-- @since:5.0.1 -->
### 9. Int

Ground

<!-- @since:5.0.1 -->
### 10. Double

Stiffness X value

<!-- @since:5.0.1 -->
### 11. Double

Stiffness Y value

<!-- @since:5.0.1 -->
### 12. Double

Stiffness Z value

<!-- @since:5.0.1 -->
### 13. Int

Local Stiffness Unit

<!-- @since:5.0.1 -->
### 14. Double

Rotation Stiffness X value

<!-- @since:5.0.1 -->
### 15. Double

Rotation Stiffness Y value

<!-- @since:5.0.1 -->
### 16. Double

Rotation Stiffness Z value

<!-- @since:5.0.1 -->
### 17. Int

Local Rotate Stiffness Unit

<!-- @since:5.0.1 -->
### 18. Double

Damping Coefficient

<!-- @since:5.0.1 -->
### 19. Double

Stress Coefficient

<!-- @since:5.0.1 -->
### 20. Cursor

referred coordinate system, NULL is global

<!-- @since:5.0.1 -->
### 21. Int

top Rbe type,0=RBE3,1=Rbe2

<!-- @since:5.0.1 -->
### 22. Double

Top bolt hole rbe range

<!-- @since:5.0.1 -->
### 23. Double

top slave nodes in this range will not be considered

<!-- @since:5.0.1 -->
### 24. Int

bottom Rbe type,0=RBE3,1=Rbe2

<!-- @since:5.0.1 -->
### 25. Double

bottom bolt hole rbe range

<!-- @since:5.0.1 -->
### 26. Double

bottom slave nodes in this range will not be considered

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Lbc _Bolt _Modeling _Type _C_Edge([5:66319], [5:10000031], "RBE", 20, 0.1, 0, 1, 2.22507e-308,
    0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308,
    0, 1.79769e+308, 1.79769e+308, 0:0, 0, 0.01, 0, 0, 0.01, 0)
```
