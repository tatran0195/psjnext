---
title: "Property1DBeam()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

1D Beam property

## Syntax

```psj
Property1DBeam(string Name, int Id, Cursor Section, int ShapeDataType,
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

<!-- @since:5.0.1 -->
### 1. string

Name

<!-- @since:5.0.1 -->
### 2. Int

ID

<!-- @since:5.0.1 -->
### 3. Int

Shape data type \[SHAPE\_TYPE\_UNKNOWN = 0, SHAPE\_TYPE\_M3 = 1, SHAPE\_TYPE\_M4 =2, SHAPE\_TYPE\_M6 = 3, SHAPE\_TYPE\_M8 = 4, SHAPE\_TYPE\_M10 = 5, SHAPE\_TYPE\_M12 = 6, SHAPE\_TYPE\_M14 = 7, SHAPE\_TYPE\_M16 = 8, SHAPE\_TYPE\_M18 = 9, SHAPE\_TYPE\_M20 = 10, SHAPE\_TYPE\_M22 = 11, SHAPE\_TYPE\_M24 = 12, SHAPE\_TYPE\_M26 = 13, SHAPE\_TYPE\_M28 = 14, SHAPE\_TYPE\_M30 = 15, SHAPE\_TYPE\_M32 = 16, SHAPE\_TYPE\_M34 = 17, SHAPE\_TYPE\_M36 = 18, SHAPE\_TYPE\_CIRC = 19]

<!-- @since:5.0.1 -->
### 4. Cursor

Material

<!-- @since:5.0.1 -->
### 5. Double

Area

<!-- @since:5.0.1 -->
### 6. Double\[3]

Orient Vector double list \[x,y,z]

<!-- @since:5.0.1 -->
### 7. Double\[3]

Inertia double list \[Izz,Iyy,Izy]

<!-- @since:5.0.1 -->
### 8. Double

Tor const

<!-- @since:5.0.1 -->
### 9. Double

NSM

<!-- @since:5.0.1 -->
### 10. Double

NSM\_A

<!-- @since:5.0.1 -->
### 11. Double

NSM\_B

<!-- @since:5.0.1 -->
### 12. Double

NSM\_NodeAy

<!-- @since:5.0.1 -->
### 13. Double

NSM\_NodeAz

<!-- @since:5.0.1 -->
### 14. Double

NSM\_NodeBy

<!-- @since:5.0.1 -->
### 15. Double

NSM\_NodeBz

<!-- @since:5.0.1 -->
### 16. Double

Shear stiffness K1

<!-- @since:5.0.1 -->
### 17. Double

Shear stiffness K2

<!-- @since:5.0.1 -->
### 18. Double

Shear area relief S1

<!-- @since:5.0.1 -->
### 19. Double

Shear area relief S2

<!-- @since:5.0.1 -->
### 20. Double

Wrap Coefficient A

<!-- @since:5.0.1 -->
### 21. Double

Wrap Coefficient B

<!-- @since:5.0.1 -->
### 22. Double

Stress recovery coefficient Cy

<!-- @since:5.0.1 -->
### 23. Double

Stress recovery coefficient Cz

<!-- @since:5.0.1 -->
### 24. Double

Stress recovery coefficient Dy

<!-- @since:5.0.1 -->
### 25. Double

Stress recovery coefficient Dz

<!-- @since:5.0.1 -->
### 26. Double

Stress recovery coefficient Ey

<!-- @since:5.0.1 -->
### 27. Double

Stress recovery coefficient Ez

<!-- @since:5.0.1 -->
### 28. Double

Stress recovery coefficient Fy

<!-- @since:5.0.1 -->
### 29. Double

Stress recovery coefficient Fz

<!-- @since:5.0.1 -->
### 30. Bool

Pin flag at A3 true = 1, false = 0

<!-- @since:5.0.1 -->
### 31. Bool

Pin flag at A4 true = 1, false = 0

<!-- @since:5.0.1 -->
### 32. Bool

Pin flag at A5 true = 1, false = 0

<!-- @since:5.0.1 -->
### 33. Bool

Pin flag at B0 true = 1, false = 0

<!-- @since:5.0.1 -->
### 34. Bool

Pin flag at B1 true = 1, false = 0

<!-- @since:5.0.1 -->
### 35. Bool

Pin flag at B2 true = 1, false = 0

<!-- @since:5.0.1 -->
### 36. Bool

Pin flag at B3 true = 1, false = 0

<!-- @since:5.0.1 -->
### 37. Bool

Pin flag at B4 true = 1, false = 0

<!-- @since:5.0.1 -->
### 38. Bool

Pin flag at B5 true = 1, false = 0

<!-- @since:5.0.1 -->
### 39. Double\[3]

Offset PointA double list

<!-- @since:5.0.1 -->
### 40. Double\[3]

Offset PointB double list

<!-- @since:5.0.1 -->
### 41. Int

Local Unit Length

<!-- @since:5.0.1 -->
### 42. Int

Local Unit mass

<!-- @since:5.0.1 -->
### 43. Cursor\[]

Target list

<!-- @since:5.0.1 -->
### 44. Cursor

Edit 1D Beam

<!-- @since:5.0.1 -->
### 45. Bool

Tapped flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 46. Int

Integration Points Num

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Property1DBeam("BEAM2", 2, 93:1, 0, 22:2, 1.25664e-07, [1, 3, 3], [1.257e-15, 1.257e-15, 0],
    2.513e-15, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308,
    1.79769e+308, 0.9, 0.9, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308,
    1.79769e+308, 1.79769e+308, 1.79769e+308, 0.0002, -0, 0, 0.0002, -0.0002, 0, -0, -0.0002,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [1.7976931e+308, 1.7976931e+308, 1.7976931e+308],
    [1.7976931e+308, 1.7976931e+308, 1.7976931e+308], 0, 0, [5:1], 0:0, 0, 2147483647)
```
