---
title: "EnforcedAcceleration()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create enforced acceleration

## Syntax

```psj
EnforcedAcceleration(String m _strName,int dwDof,double fVel[0],double fVel[1],double fVel[2],
    double fVel[3],double fVel[4],double fVel[5],Cursor curCoord,int enArrowDir,Cursor crTable,
    Cursor crNodeSet,double m _fPhase,double m _fDelay,Cursor crPhaseTable,BOOL bExport,
    Cursor crMEExport[0],Cursor crMEExport[1],Cursor crMEExport[2],Cursor crMEExport[3],
    Cursor crMEExport[4],Cursor crMEExport[5],int iAcUnit,int iRotUnit,Cursor[] m _taTarget,Cursor m _crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of enforced acceleration

<!-- @since:5.0.1 -->
### 2. Int

dof

<!-- @since:5.0.1 -->
### 3. Double

translation x

<!-- @since:5.0.1 -->
### 4. Double

translation y

<!-- @since:5.0.1 -->
### 5. Double

translation z

<!-- @since:5.0.1 -->
### 6. Double

rotate x

<!-- @since:5.0.1 -->
### 7. Double

rotate y

<!-- @since:5.0.1 -->
### 8. Double

rotate z

<!-- @since:5.0.1 -->
### 9. Cursor

coordinate system

<!-- @since:5.0.1 -->
### 10. Int

arrow direction\[0:Start at Node; 1:End at Node]

<!-- @since:5.0.1 -->
### 11. Cursor

select table

<!-- @since:5.0.1 -->
### 12. Cursor

node set table

<!-- @since:5.0.1 -->
### 13. Double

phase

<!-- @since:5.0.1 -->
### 14. Double

delay

<!-- @since:5.0.1 -->
### 15. Cursor

phase table

<!-- @since:5.0.1 -->
### 16. Bool

if export defined

<!-- @since:5.0.1 -->
### 17. Cursor

translation x

<!-- @since:5.0.1 -->
### 18. Cursor

translation y

<!-- @since:5.0.1 -->
### 19. Cursor

translation z

<!-- @since:5.0.1 -->
### 20. Cursor

rotation x

<!-- @since:5.0.1 -->
### 21. Cursor

rotation y

<!-- @since:5.0.1 -->
### 22. Cursor

rotation z

<!-- @since:5.0.1 -->
### 23. Int

unit of acceleration

<!-- @since:5.0.1 -->
### 24. Int

unit of rotate

<!-- @since:5.0.1 -->
### 25. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 26. Cursor

edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
EnforcedAcceleration("EnforcedAcceleration1", 63, 0.001, 0.002, 0.003, 3, 2, 1,0:0, 0, 0:0,
    0:0, 1.79769e+308, 1.79769e+308, 0:0, 0, 0:0, 0:0, 0:0, 0:0, 0:0, 0:0, 0, 0, [6:26], 0:0)
```
