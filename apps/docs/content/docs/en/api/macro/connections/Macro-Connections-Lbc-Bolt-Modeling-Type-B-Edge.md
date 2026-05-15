---
title: "Lbc _Bolt _Modeling _Type _B_Edge()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Lbc TypeB Bolt Edge method

## Syntax

```psj
Lbc _Bolt _Modeling _Type _B_Edge(Cursor taEdgeCur1,TCursor taEdgeCur2,string strRbeName,
    string strBarName,int nShaftType,Cursor curBarProperty,double dPlaneTol,
    double dMaxBoltHeight,bool bPretensionLoad,int nSolverType,double dForceValue,
    int nPreTenDof,Cursor curCoord,int nBoltFixLength,int nTopSlot,double dRBE1,
    double dRBE2,double dBotDtDia,double dPitch,int nBotRbeConnType, bool IsCreate2ADVCStaticProcessForFixLength)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

circular edges in top side

<!-- @since:5.0.1 -->
### 2. Cursor\[]

circular edges in bottom side

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
### 9. Bool

PretensionLoad flag,0=false,1=true

<!-- @since:5.0.1 -->
### 10. Int

Type of pretension Solver,0=All option pretension,1=Abaqus pretension

<!-- @since:5.0.1 -->
### 11. Double

force value.Used in pretension connection

<!-- @since:5.0.1 -->
### 12. Int

Pretension DoF at target

<!-- @since:5.0.1 -->
### 13. Cursor

referred coordinate system, NULL is global

<!-- @since:5.0.1 -->
### 14. Int

BoltFixLength used in Pretension

<!-- @since:5.0.1 -->
### 15. Int

top side slot bolt flag,0=false,1=true

<!-- @since:5.0.1 -->
### 16. Double

top rbe slave node diameter range

<!-- @since:5.0.1 -->
### 17. Double

Always zero.No need to consider here

<!-- @since:5.0.1 -->
### 18. Double

bottom bolt hole diameter

<!-- @since:5.0.1 -->
### 19. Double

bottom Rbe Pitch distance

<!-- @since:5.0.1 -->
### 20. Int

bottom Rbe connection type,0=down,1=up,2=center

<!-- @since:5.0.1 -->
### 21. Bool

Option ADVC Static process, 0: No, 1:Yes

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Lbc _Bolt _Modeling _Type _B_Edge([5:66319], [5:10000031], "RBE", "Bar _2", 0, 0:0, 20,
    0.1, 0, 0, 0, 0, 0:0, 0, 0, 0.0081206, 0, 0.0027248, 0.01, 0, 0)
```
