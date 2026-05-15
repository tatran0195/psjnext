---
title: "ContactAbaqus()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Contact for ABAQUS

## Syntax

```psj
ContactAbaqus(String m _strName,int m _iMethod,int m _iType,int m _iAlg,double AdjustVal,
    double ExtensionZone,double MaxPenetration,int SmallSliding,double Smooth,
    int FrictionType,double FrictionCoef1,double FrictionCoef2,double ShearLimit,
    double SlipTol,double StaticFrictionCoef,double KineticFrictionCoef,double DecayCoef,
    int bAdjust,double PositonTol,int formula,int tie,int m _type,int m _bAllowSeparation,
    double m _slope,TSheetd m _table,int m _clearanceType,int m _TypeId,
    bool m _btemperatureDependency,int m _idependencies,TSheetd m _table,int m _TypeId,
    bool m _btemperatureDependency,int m _idependencies,TSheetd m _table,Cursor[] m _taTarget,
    Cursor m _crEditCursor,int m _Color)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of contact

<!-- @since:5.0.1 -->
### 2. Int

method type\[0:MANUAL\_FACE; 1:MANUAL\_GROUP; 2:BY\_GROUP\_MATRIX; 3:SHARE\_FACE; 4:AUTO\_SETTING; 5:METHOD\_UNKNOWN]

<!-- @since:5.0.1 -->
### 3. Int

contact type\[0:CONTACT\_GENERAL; 1:CONTACT\_TIED; 2:CONTACT\_ALL\_SELF]

<!-- @since:5.0.1 -->
### 4. Int

algorithm\[0:face to face; 1:node to face]

<!-- @since:5.0.1 -->
### 5. Double

adjust value

<!-- @since:5.0.1 -->
### 6. Double

extension Zone

<!-- @since:5.0.1 -->
### 7. Double

max pretension

<!-- @since:5.0.1 -->
### 8. Int

small sliding\[0:Off; 1:On]

<!-- @since:5.0.1 -->
### 9. Double

smooth

<!-- @since:5.0.1 -->
### 10. Int

friction type\[0:None; 1:General; 2:Lagrange; 3:Rough; 4:Static and Kinematic]

<!-- @since:5.0.1 -->
### 11. Double

friction coef1

<!-- @since:5.0.1 -->
### 12. Double

friction coef2

<!-- @since:5.0.1 -->
### 13. Double

shear limit

<!-- @since:5.0.1 -->
### 14. Double

slip tolerance

<!-- @since:5.0.1 -->
### 15. Double

static friction coef

<!-- @since:5.0.1 -->
### 16. Double

kinetic friction coef

<!-- @since:5.0.1 -->
### 17. Double

decay coef

<!-- @since:5.0.1 -->
### 18. Int

adjust\[0:No; 1:Yes]

<!-- @since:5.0.1 -->
### 19. Double

position tol

<!-- @since:5.0.1 -->
### 20. Int

formulation\[0:Node to Surface; 1:Surface to Surface]

<!-- @since:5.0.1 -->
### 21. Int

TIE\[0:No]

<!-- @since:5.0.1 -->
### 22. Int

pressure-Overclosure type\[0:Hard Contact; 1:Exponential; 2:Linear; 3:Tabular]

<!-- @since:5.0.1 -->
### 23. Int

allow separation

<!-- @since:5.0.1 -->
### 24. Double

contact stiffness

<!-- @since:5.0.1 -->
### 25. TSheetd

table of pressure-Overclosure

<!-- @since:5.0.1 -->
### 26. Int

thermal conductance type\[0:Clearance Dependence; 1:Pressure Dependence; 2:Clearance and Pressure Dependence]

<!-- @since:5.0.1 -->
### 27. Int

type\[0:CLEARANCE\_DEPENDENCY; 1:PRESSURE\_DEPENDENCY]

<!-- @since:5.0.1 -->
### 28. Bool

if use temperature dependent data

<!-- @since:5.0.1 -->
### 29. Int

number of field variables

<!-- @since:5.0.1 -->
### 30. TSheetd

table of clearance dependency

<!-- @since:5.0.1 -->
### 31. Int

type\[0:CLEARANCE\_DEPENDENCY; 1:PRESSURE\_DEPENDENCY]

<!-- @since:5.0.1 -->
### 32. Bool

if use temperature dependent data

<!-- @since:5.0.1 -->
### 33. Int

number of field variables

<!-- @since:5.0.1 -->
### 34. TSheetd

table of pressure dependency

<!-- @since:5.0.1 -->
### 35. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 36. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 37. Int

contact maker color

## Return Code

**1** - The function is executed correctly.

**0** - Cannot execute.

## Sample Code

```psj
ContactAbaqus("Test",1,1,1,0.001,0.001,0.001,1,0.001,1,0.001,0.001,0.001,0.001,
    0.001,0.001,0.001,1,0.001,1,1,1,1,0.001,,1,1,1,1,,1,1,1,,[1:11,2:12],1:11,1)
```
