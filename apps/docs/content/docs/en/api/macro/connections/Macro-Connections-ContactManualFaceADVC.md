---
title: "ContactManualFaceADVC()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create contact for advc

## Syntax

```psj
ContactManualFaceADVC(cursor[] m _crlMasterFaces, cursor[] crlSlaveFaces, 
    string m _strName,int m _iType,int slidingType,int InitialState,
    double initialStateTol,double kineticFrictionCoef,double exponentialCoef,
    int Behavior,double Clearance,int adjust2Clearance,double interference,
    int adjust2Interference,int autoShrink,int badvAdjust,double adjustValue,
    double FrictionCoef,double MaxShear,double elastic _slip,double slip _tolerance,
    double searchWidth,double SearchGap,double searchDepth,double critialPenetration,
    int estimation _impact _time,int formula,int constraintType,int iDataType,
    int m _TypeId,bool m _btemperatureDependency,int m _idependencies,TSheetd m _table,
    int stabilized,int type,double residual _factor,double effective _dist,double cn,
    double ct,Cursor[] m _taCClearance, Cursor m _crEdit,
    double searchAngle,int constraintType _explicit,double penaltyFact,
    double penaltyFactExplicit,int m _Color,int m _iAlg,int m _iMethod,
    int iTypeId _pressure, bool bPressureTemperatureDependency, int iPressureDependencies, 
    double[] tshPressureData, int iTyingType)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

Mastar faces

<!-- @since:5.1.0 -->
### 2. Cursor\[]

Slave faces

<!-- @since:5.1.0 -->
### 3. String

name of contact

<!-- @since:5.1.0 -->
### 4. Int

contact type\[0:General; 1:Tied]

<!-- @since:5.1.0 -->
### 5. Int

Sliding Type \[0: blank; 1: Finite sliding; 2: Small sliding; 3: Not sliding]

<!-- @since:5.1.0 -->
### 6. Int

initial state\[0:blank; 1:Auto; 2:Open; 3:Close]

<!-- @since:5.1.0 -->
### 7. Double

initial state tol

<!-- @since:5.1.0 -->
### 8. Double

kinetic friction coef

<!-- @since:5.1.0 -->
### 9. Double

exponential coef

<!-- @since:5.1.0 -->
### 10. Int

behavior\[0:blank; 1:Separation; 2:No Separation]

<!-- @since:5.1.0 -->
### 11. Double

clearance

<!-- @since:5.1.0 -->
### 12. Int

adjust to clearance\[0:blank; 1:Yes; 2:No]

<!-- @since:5.1.0 -->
### 13. Double

interference

<!-- @since:5.1.0 -->
### 14. Int

adjust to Interference\[0:blank; 1:Yes; 2:No]

<!-- @since:5.1.0 -->
### 15. Int

auto shrink\[0:blank; 1:Yes; 2:No]

<!-- @since:5.1.0 -->
### 16. Int

adjust\[0:blank; 1:Yes; 2:Value]

<!-- @since:5.1.0 -->
### 17. Double

adjust value

<!-- @since:5.1.0 -->
### 18. Double

friction coef

<!-- @since:5.1.0 -->
### 19. Double

max shear stress

<!-- @since:5.1.0 -->
### 20. Double

elastic slip

<!-- @since:5.1.0 -->
### 21. Double

slip tolerance

<!-- @since:5.1.0 -->
### 22. Double

search width

<!-- @since:5.1.0 -->
### 23. Double

search gap

<!-- @since:5.1.0 -->
### 24. Double

search depth

<!-- @since:5.1.0 -->
### 25. Double

critial penetration

<!-- @since:5.1.0 -->
### 26. Int

impact time estimation\[0:blank; 1:Yes; 2:No]

<!-- @since:5.1.0 -->
### 27. Int

formulation\[0:blank; 1:node to segment; 2:segment to segment]

<!-- @since:5.1.0 -->
### 28. Int

constraint type\[0:blank; 1:Lagrange; 2:Penalty]

<!-- @since:5.1.0 -->
### 29. Int

thermal conductance type\[0:blank; 1:Clearance Dependence]

<!-- @since:5.1.0 -->
### 30. Int

type\[0:CLEARANCE\_DEPENDENCY; 1:PRESSURE\_DEPENDENCY]

<!-- @since:5.1.0 -->
### 31. Bool

if use temperature dependent data

<!-- @since:5.1.0 -->
### 32. Int

number of field variables

<!-- @since:5.1.0 -->
### 33. TSheetd

table of clearance dependency

<!-- @since:5.1.0 -->
### 34. Int

if stabilization parameter defined\[0:not defined; 1:defined]

<!-- @since:5.1.0 -->
### 35. Int

type\[0:blank; 1:stiffness; 2:Area]

<!-- @since:5.1.0 -->
### 36. Double

residual factor

<!-- @since:5.1.0 -->
### 37. Double

effective distance

<!-- @since:5.1.0 -->
### 38. Double

normal factor cn

<!-- @since:5.1.0 -->
### 39. Double

normal factor ct

<!-- @since:5.1.0 -->
### 40. Cursor\[]

clearance list

<!-- @since:5.1.0 -->
### 41. Cursor

edit cursor

<!-- @since:5.1.0 -->
### 42. Double

Search Angle Value

<!-- @since:5.1.0 -->
### 43. Int

Constraint for Explicit type \[0:blank; 1:kinematic; 2:penalty]

<!-- @since:5.1.0 -->
### 44. Double

Penalty Scale Factor

<!-- @since:5.1.0 -->
### 45. Double

Penalty Scale Factor for Explicit

<!-- @since:5.1.0 -->
### 46. Int

contact maker color

<!-- @since:5.1.0 -->
### 47. Int

algorithm\[0:face to face]

<!-- @since:5.1.0 -->
### 48. Int

method type (specify 0)

<!-- @since:5.1.0 -->
### 49. Int

pressure type ID

<!-- @since:5.1.0 -->
### 50. Bool

Flag whether to use temperature dependent data for pressure dependency.

<!-- @since:5.1.0 -->
### 51. Int

The number of pressure dependency

<!-- @since:5.1.0 -->
### 52. double\[]

table of pressure dependency.

<!-- @since:5.1.0 -->
### 53. int

tying type \[0:blank, 1:Rigid, 2:Shear Tying]

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ContactManualFaceADVC([6:24], [6:49], "ContactADVC _1", 1, 0, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 0, 0, 1.79769e+308, 0, 0, 1, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 0, 0, 1, 1, 0, 0, [1, 2, 0, 0], 0, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, [], 0:0, 1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 65280, 0, 0, 2, 0, 0, [1, 2, 0, 0], 0)
```
