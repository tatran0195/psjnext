---
title: "ContactADVC()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create contact for advc

## Syntax

```psj
ContactADVC(String m _strName,int m _iType,int slidingType,int InitialState,
    double initialStateTol,double kineticFrictionCoef,double exponentialCoef,
    int Behavior,double Clearance,int adjust2Clearance,double interference,
    int adjust2Interference,int autoShrink,int badvAdjust,double adjustValue,
    double FrictionCoef,double MaxShear,double elastic _slip,double slip _tolerance,
    double searchWidth,double SearchGap,double searchDepth,double critialPenetration,
    int estimation _impact _time,int formula,int constraintType,int iDataType,
    int m _TypeId,bool m _btemperatureDependency,int m _idependencies,TSheetd m _table,
    int stabilized,int type,double residual _factor,double effective _dist,double cn,
    double ct,Cursor[] m _taCClearance,Cursor[] m _taTarget,Cursor m _crEdit,
    double searchAngle,int constraintType _explicit,double penaltyFact,
    double penaltyFactExplicit,int m _Color,int m _iAlg,int m _iMethod,
    int iTypeId _pressure, bool bPressureTemperatureDependency, int iPressureDependencies, 
    double[] tshPressureData, int iTyingType)
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

Sliding Type \[0: blank; 1: Finite sliding; 2: Small sliding; 3: Not sliding]

<!-- @since:5.0.1 -->
### 4. Int

initial state\[0:blank; 1:Auto; 2:Open; 3:Close]

<!-- @since:5.0.1 -->
### 5. Double

initial state tol

<!-- @since:5.0.1 -->
### 6. Double

kinetic friction coef

<!-- @since:5.0.1 -->
### 7. Double

exponential coef

<!-- @since:5.0.1 -->
### 8. Int

behavior\[0:blank; 1:Separation; 2:No Separation]

<!-- @since:5.0.1 -->
### 9. Double

clearance

<!-- @since:5.0.1 -->
### 10. Int

adjust to clearance\[0:blank; 1:Yes; 2:No]

<!-- @since:5.0.1 -->
### 11. Double

interference

<!-- @since:5.0.1 -->
### 12. Int

adjust to Interference\[0:blank; 1:Yes; 2:No]

<!-- @since:5.0.1 -->
### 13. Int

auto shrink\[0:blank; 1:Yes; 2:No]

<!-- @since:5.0.1 -->
### 14. Int

adjust\[0:blank; 1:Yes; 2:Value]

<!-- @since:5.0.1 -->
### 15. Double

adjust value

<!-- @since:5.0.1 -->
### 16. Double

friction coef

<!-- @since:5.0.1 -->
### 17. Double

max shear stress

<!-- @since:5.0.1 -->
### 18. Double

elastic slip

<!-- @since:5.0.1 -->
### 19. Double

slip tolerance

<!-- @since:5.0.1 -->
### 20. Double

search width

<!-- @since:5.0.1 -->
### 21. Double

search gap

<!-- @since:5.0.1 -->
### 22. Double

search depth

<!-- @since:5.0.1 -->
### 23. Double

critial penetration

<!-- @since:5.0.1 -->
### 24. Int

impact time estimation\[0:blank; 1:Yes; 2:No]

<!-- @since:5.0.1 -->
### 25. Int

formulation\[0:blank; 1:node to segment; 2:segment to segment]

<!-- @since:5.0.1 -->
### 26. Int

constraint type\[0:blank; 1:Lagrange; 2:Penalty]

<!-- @since:5.0.1 -->
### 27. Int

thermal conductance type\[0:blank; 1:Clearance Dependence]

<!-- @since:5.0.1 -->
### 28. Int

type\[0:CLEARANCE\_DEPENDENCY; 1:PRESSURE\_DEPENDENCY]

<!-- @since:5.0.1 -->
### 29. Bool

if use temperature dependent data

<!-- @since:5.0.1 -->
### 30. Int

number of field variables

<!-- @since:5.0.1 -->
### 31. TSheetd

table of clearance dependency

<!-- @since:5.0.1 -->
### 32. Int

if stabilization parameter defined\[0:not defined; 1:defined]

<!-- @since:5.0.1 -->
### 33. Int

type\[0:blank; 1:stiffness; 2:Area]

<!-- @since:5.0.1 -->
### 34. Double

residual factor

<!-- @since:5.0.1 -->
### 35. Double

effective distance

<!-- @since:5.0.1 -->
### 36. Double

normal factor cn

<!-- @since:5.0.1 -->
### 37. Double

normal factor ct

<!-- @since:5.0.1 -->
### 38. Cursor\[]

clearance list

<!-- @since:5.0.1 -->
### 39. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 40. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 41. Double

Search Angle Value

<!-- @since:5.0.1 -->
### 42. Int

Constraint for Explicit type \[0:blank; 1:kinematic; 2:penalty]

<!-- @since:5.0.1 -->
### 43. Double

Penalty Scale Factor

<!-- @since:5.0.1 -->
### 44. Double

Penalty Scale Factor for Explicit

<!-- @since:5.0.1 -->
### 45. Int

contact maker color

<!-- @since:5.0.1 -->
### 46. Int

algorithm\[0:face to face]

<!-- @since:5.0.1 -->
### 47. Int

method type (specify 1)

<!-- @since:5.1.0 -->
### 48. Int

pressure type ID

<!-- @since:5.1.0 -->
### 49. Bool

Flag whether to use temperature dependent data for pressure dependency.

<!-- @since:5.1.0 -->
### 50. Int

The number of pressure dependency

<!-- @since:5.1.0 -->
### 51. double\[]

table of pressure dependency.

<!-- @since:5.1.0 -->
### 52. int

tying type \[0:blank, 1:Rigid, 2:Shear Tying]

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ContactADVC("ContactADVC _1", 1, 0, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 0, 0, 1.79769e+308, 0, 0, 1, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 0, 0, 1, 1, 0, 0, [1, 2, 0, 0], 0, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, [], [79:5-79:6], 108:8, 1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 65280, 0, 1, 2, 0, 0, [1, 2, 0, 0], 0)
```
