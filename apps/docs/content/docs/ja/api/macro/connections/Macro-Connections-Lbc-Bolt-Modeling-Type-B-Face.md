---
title: "Lbc _Bolt _Modeling _Type _B_Face()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Lbc TypeB Bolt Face method

## Syntax

```psj
Lbc _Bolt _Modeling _Type _B_Face(Cursor taFaceCur1,Cursor taFaceCur2,string strRbeName,
    string strBarName,int nShaftType,Cursor curBarProperty,double dPlaneTol,
    double dMaxBoltHeight,double dMaxDiameter,double dMinDiameter,bool bPretensionLoad,
    int nSolverType,double dForceValue,int nPreTenDof,Cursor curCoord,
    int nBoltFixLength,int nTopSlot,double dRBE1,double dRBE2,double dBotDtDia,
    double dPitch,int nBotRbeConnType,double dScale1, bool IsCreate2ADVCStaticProcessForFixLength)
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
### 4. String

name of BarBody

<!-- @since:5.0.1 -->
### 5. Int

Connection type, 0: cbar, 1: rbe2

<!-- @since:5.0.1 -->
### 6. Cursor

bar property cursor

<!-- @since:5.0.1 -->
### 7. Double

Plane tolerance angle around the selected edge.Used in finding slave nodes around the selected edge

<!-- @since:5.0.1 -->
### 8. Double

Maximum distance between top and bottom rbe

<!-- @since:5.0.1 -->
### 9. Double

Maximum diameter range of bolt hole

<!-- @since:5.0.1 -->
### 10. Double

Minimum diameter range of bolt hole

<!-- @since:5.0.1 -->
### 11. Bool

PretensionLoad flag,0=false,1=true

<!-- @since:5.0.1 -->
### 12. Int

Type of pretension Solver,0=All option pretension,1=Abaqus pretension

<!-- @since:5.0.1 -->
### 13. Double

force value.Used in pretension connection

<!-- @since:5.0.1 -->
### 14. Int

Pretension DoF at target

<!-- @since:5.0.1 -->
### 15. Cursor

referred coordinate system, NULL is global

<!-- @since:5.0.1 -->
### 16. Int

BoltFixLength used in Pretension

<!-- @since:5.0.1 -->
### 17. Int

top side slot bolt flag,0=false,1=true

<!-- @since:5.0.1 -->
### 18. Double

top rbe slave node diameter range

<!-- @since:5.0.1 -->
### 19. Double

Always zero.No need to consider here

<!-- @since:5.0.1 -->
### 20. Double

bottom bolt hole diameter.works with zero as default.User can specify value.

<!-- @since:5.0.1 -->
### 21. Double

bottom Rbe Pitch distance

<!-- @since:5.0.1 -->
### 22. Int

bottom Rbe connection type,0=down,1=up,2=center

<!-- @since:5.0.1 -->
### 23. Double

scale value for showing range,used in preview

<!-- @since:5.0.1 -->
### 24. Bool

Option ADVC Static process, 0: No, 1:Yes

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Lbc _Bolt _Modeling _Type _B_Face([6:60], [6:49], "RBE", "Bar _1", 0, 0:0, 20.0002, 0.1, 0.1,
    0.001, 0, 0, 0, 0, 0:0, 0, 1, 0.06, 0, 0, 0.01, 0, 3, 0)
```
