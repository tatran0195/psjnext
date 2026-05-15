---
title: "Imprint _PerpendicularCylinderLine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Perpendicular Cylinder line

## Syntax

```psj
Imprint _PerpendicularCylinderLine(double[] Point _xyz, int FaceID, int type,double value,
    bool oppositeFlag, bool BreakFace,Cursor[] BodyCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double\[]

Point xyz \[\[x1,y1,z1],\[x2,y2,z2],\[x3,y3,z3]]

<!-- @since:5.0.1 -->
### 2. Int

Face ID

<!-- @since:5.0.1 -->
### 3. Int

Method Type 0=Arclength,1=CenterAngle

<!-- @since:5.0.1 -->
### 4. Double

Length/Angle Value

<!-- @since:5.0.1 -->
### 5. Bool

Opposite Flag true=1,false=0

<!-- @since:5.0.1 -->
### 6. Bool

Flag Break Face true = 1,false=0

<!-- @since:5.0.1 -->
### 7. Cursor\[]

Body Cursor(\[3:\*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint _PerpendicularCylinderLine([[0.005, 0.00666667, 0.00866025], [0.005, 0.02, 0.00866025]], 5, 1, 0, 0, 1, [3:1])
```
