---
title: "ContactNXNastran()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create contact for Nastran

## Syntax

```psj
ContactNXNastran(String m _strName,int iType,int iAlg,double dNorPenFactor,
    double dTanPenFactor,double dForceConTol,double dMaxForceIter,double dMaxStaIter,
    double dChangeNum,double dMinContactPer,int iShellThickness,int iContactStatus,
    int iInitGapPenetra,int iRegionRefine,int iEvaluPts,double dMinSearDist,
    double dMaxSearDist,double dFricCoef,double dSearchDist,double dPenatlyFactor,
    int iShellOffset,Cursor[] m _taTarget,Cursor m _crEdit,int m _Color,int m _iMethod)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of contact

<!-- @since:5.0.1 -->
### 2. Int

contact type\[0:General; 1:Tied]

<!-- @since:5.0.1 -->
### 3. Int

algorithm\[0:face to face]

<!-- @since:5.0.1 -->
### 4. Double

normal penalty factor

<!-- @since:5.0.1 -->
### 5. Double

tangential penalty factor

<!-- @since:5.0.1 -->
### 6. Double

force convergence tol

<!-- @since:5.0.1 -->
### 7. Double

max force iterations

<!-- @since:5.0.1 -->
### 8. Double

max status iterations

<!-- @since:5.0.1 -->
### 9. Double

change number

<!-- @since:5.0.1 -->
### 10. Double

min contact percentage

<!-- @since:5.0.1 -->
### 11. Int

shell thickness\[0:Include; 1:Not Include]

<!-- @since:5.0.1 -->
### 12. Int

contact status\[0:Previous; 1:Initial]

<!-- @since:5.0.1 -->
### 13. Int

initial gap or penetration\[0:No Correction; 1:Reset Penetration; 2:Reset Both]

<!-- @since:5.0.1 -->
### 14. Int

region refine\[0:Refine; 1:Not Refine]

<!-- @since:5.0.1 -->
### 15. Int

evaluation points\[0:Low; 1:Mid; 2:High]

<!-- @since:5.0.1 -->
### 16. Double

min search dist

<!-- @since:5.0.1 -->
### 17. Double

max search dist

<!-- @since:5.0.1 -->
### 18. Double

friction coef

<!-- @since:5.0.1 -->
### 19. Double

search dist

<!-- @since:5.0.1 -->
### 20. Double

penalty factor

<!-- @since:5.0.1 -->
### 21. Int

shell thickness\[0:Include; 1:Not Include]

<!-- @since:5.0.1 -->
### 22. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 23. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 24. Int

contact maker color

<!-- @since:5.0.1 -->
### 25. Int

method type\[0:MANUAL\_FACE; 1:MANUAL\_GROUP; 2:BY\_GROUP\_MATRIX; 3:SHARE\_FACE; 4:AUTO\_SETTING; 5:METHOD\_UNKNOWN]

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ContactNXNastran("ContactNXNastran _1", 0, 0, 10, 1, 0.01, 10, 20, 0.02, 100, 0, 0, 0,
    0, 1, 0, 0.01, 0, 10, 1, 0, [79:1-79:2], 0:0, 16711680, 1)
```
