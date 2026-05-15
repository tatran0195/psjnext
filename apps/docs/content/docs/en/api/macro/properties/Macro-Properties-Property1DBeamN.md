---
title: "Property1DBeamN()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

1D Beam property

## Syntax

```psj
Property1DBeam(string Name, int Id, color propertyColor, Cursor Section, int ShapeDataType,
    Cursor Material, double Area, double[3] Orient, double[3] Inertia,
    double TorConst, double NSM, double NSM _A, double NSM _B, double NSM _NodeAy,
    double NSM _NodeAz, double NSM _NodeBy, double NSM _NodeBz, double ShearStiffnessK1,
    double ShearStiffnessK2, double AreaReliefS1, double AreaReliefS2,
    double WrapCoefficientA, double WrapCoefficientB, double Y _NA _NodeA,
    double Z _NA _NodeA, double Y _NA _NodeB, double Z _NA _NodeB, double StressRevoceryCoeff _Cy,
    double StressRevoceryCoeff _Cz, double StressRevoceryCoeff _Dy,
    double StressRevoceryCoeff _Dz, double StressRevoceryCoeff _Ey,
    double StressRevoceryCoeff _Ez, double StressRevoceryCoeff _Fy,
    double StressRevoceryCoeff _Fz, bool PinA0, bool PinA1, bool PinA2, bool PinA3,
    bool PinA4, bool PinA5, bool PinB0, bool PinB1, bool PinB2, bool PinB3, bool PinB4,
    bool PinB5, double[3] OffsetPointA, double[3] OffsetPointB, int LocalLengthUnit,
    int LocalMassUnit, Cursor[] Target, Cursor credit, bool Tapped, int IntePtNum)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

Name

<!-- @since:5.1.0 -->
### 2. Int

ID

<!-- @since:5.1.0 -->
### 3. Color

Color of the property.

<!-- @since:5.1.0 -->
### 4. Cursor

Section

<!-- @since:5.1.0 -->
### 5. int

Shape data type \[SHAPE\_TYPE\_UNKNOWN = 0, SHAPE\_TYPE\_M3 = 1, SHAPE\_TYPE\_M4 =2, SHAPE\_TYPE\_M6 = 3, SHAPE\_TYPE\_M8 = 4, SHAPE\_TYPE\_M10 = 5, SHAPE\_TYPE\_M12 = 6, SHAPE\_TYPE\_M14 = 7, SHAPE\_TYPE\_M16 = 8, SHAPE\_TYPE\_M18 = 9, SHAPE\_TYPE\_M20 = 10, SHAPE\_TYPE\_M22 = 11, SHAPE\_TYPE\_M24 = 12, SHAPE\_TYPE\_M26 = 13, SHAPE\_TYPE\_M28 = 14, SHAPE\_TYPE\_M30 = 15, SHAPE\_TYPE\_M32 = 16, SHAPE\_TYPE\_M34 = 17, SHAPE\_TYPE\_M36 = 18, SHAPE\_TYPE\_CIRC = 19]

<!-- @since:5.1.0 -->
### 6. cursor

Material

<!-- @since:5.1.0 -->
### 7. double

Area

<!-- @since:5.1.0 -->
### 8. double\[3]

Orient Vector double list \[x,y,z]

<!-- @since:5.1.0 -->
### 9. Double\[3]

Inertia double list \[Izz,Iyy,Izy]

<!-- @since:5.1.0 -->
### 10. double

Tor const

<!-- @since:5.1.0 -->
### 11. double

NSM

<!-- @since:5.1.0 -->
### 12. double

NSM\_A

<!-- @since:5.1.0 -->
### 13. double

NSM\_B

<!-- @since:5.1.0 -->
### 14. Double

NSM\_NodeAy

<!-- @since:5.1.0 -->
### 15. Double

NSM\_NodeAz

<!-- @since:5.1.0 -->
### 16. Double

NSM\_NodeBy

<!-- @since:5.1.0 -->
### 17. Double

NSM\_NodeBz

<!-- @since:5.1.0 -->
### 18. Double

Shear stiffness K1

<!-- @since:5.1.0 -->
### 19. Double

Shear stiffness K2

<!-- @since:5.1.0 -->
### 20. Double

Shear area relief S1

<!-- @since:5.1.0 -->
### 21. Double

Shear area relief S2

<!-- @since:5.1.0 -->
### 22. Double

Wrap Coefficient A

<!-- @since:5.1.0 -->
### 23. Double

Wrap Coefficient B

<!-- @since:5.1.0 -->
### 24. double

Y/NA@NodeA

<!-- @since:5.1.0 -->
### 25. double

Y/NA@NodeA

<!-- @since:5.1.0 -->
### 26. double

Z/NA@NodeB

<!-- @since:5.1.0 -->
### 27. double

Z/NA@NodeB

<!-- @since:5.1.0 -->
### 28. double

Stress recovery coefficient Cy

<!-- @since:5.1.0 -->
### 29. Double

Stress recovery coefficient Cz

<!-- @since:5.1.0 -->
### 30. Double

Stress recovery coefficient Dy

<!-- @since:5.1.0 -->
### 31. Double

Stress recovery coefficient Dz

<!-- @since:5.1.0 -->
### 32. Double

Stress recovery coefficient Ey

<!-- @since:5.1.0 -->
### 33. Double

Stress recovery coefficient Ez

<!-- @since:5.1.0 -->
### 34. Double

Stress recovery coefficient Fy

<!-- @since:5.1.0 -->
### 35. Double

Stress recovery coefficient Fz

<!-- @since:5.1.0 -->
### 36. Bool

Pin flag at A1 true = 1, false = 0

<!-- @since:5.1.0 -->
### 37. Bool

Pin flag at A2 true = 1, false = 0

<!-- @since:5.1.0 -->
### 38. Bool

Pin flag at A3 true = 1, false = 0

<!-- @since:5.1.0 -->
### 39. Bool

Pin flag at A4 true = 1, false = 0

<!-- @since:5.1.0 -->
### 40. Bool

Pin flag at A5 true = 1, false = 0

<!-- @since:5.1.0 -->
### 41. Bool

Pin flag at A6 true = 1, false = 0

<!-- @since:5.1.0 -->
### 42. Bool

Pin flag at B1 true = 1, false = 0

<!-- @since:5.1.0 -->
### 43. Bool

Pin flag at B2 true = 1, false = 0

<!-- @since:5.1.0 -->
### 44. Bool

Pin flag at B3 true = 1, false = 0

<!-- @since:5.1.0 -->
### 45. Bool

Pin flag at B4 true = 1, false = 0

<!-- @since:5.1.0 -->
### 46. Bool

Pin flag at B5 true = 1, false = 0

<!-- @since:5.1.0 -->
### 47. Bool

Pin flag at B6 true = 1, false = 0

<!-- @since:5.1.0 -->
### 48. Double\[3]

Offset PointA double list

<!-- @since:5.1.0 -->
### 49. Double\[3]

Offset PointB double list

<!-- @since:5.1.0 -->
### 50. Int

Local Unit Length

<!-- @since:5.1.0 -->
### 51. Int

Local Unit mass

<!-- @since:5.1.0 -->
### 52. Cursor\[]

Target list

<!-- @since:5.1.0 -->
### 53. Cursor

Edit 1D Beam

<!-- @since:5.1.0 -->
### 54. Bool

Tapered flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 55. double

Taper Area

<!-- @since:5.1.0 -->
### 56. double\[3]

Taper Inertia \[Inertia I1/Izz, Inertia I2/Iyy, Inertia I1,2]

<!-- @since:5.1.0 -->
### 57. double

Taper Torsional Const

<!-- @since:5.1.0 -->
### 58. double

Taper Non Struct MassL

<!-- @since:5.1.0 -->
### 59. double

Taper Stress Recovery Coeff Cy

<!-- @since:5.1.0 -->
### 60. double

Taper Stress Recovery Coeff Cz

<!-- @since:5.1.0 -->
### 61. double

Taper Stress Recovery Coeff Dy

<!-- @since:5.1.0 -->
### 62. double

Taper Stress Recovery Coeff Dz

<!-- @since:5.1.0 -->
### 63. double

Taper Stress Recovery Coeff Ey

<!-- @since:5.1.0 -->
### 64. double

Taper Stress Recovery Coeff Ez

<!-- @since:5.1.0 -->
### 65. double

Taper Stress Recovery Coeff Fy

<!-- @since:5.1.0 -->
### 66. double

Taper Stress Recovery Coeff Fz

<!-- @since:5.1.0 -->
### 67. int

Integration Points Num

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Property1DBeamN("BEAM1", 5, 13478620, 0:0, 0, 22:1, 1e-06, [0, 1, 0], [1.7976931e+308, 1.7976931e+308, 1.7976931e+308], 
    1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308,
    1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308,
    1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [1.7976931e+308, 1.7976931e+308, 1.7976931e+308], 
    [1.7976931e+308, 1.7976931e+308, 1.7976931e+308], 0, 0, [5:19], 0:0, 0, 1.79769e+308, 
    [1.7976931e+308, 1.7976931e+308, 1.7976931e+308], 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 
    1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 2147483647)
```
