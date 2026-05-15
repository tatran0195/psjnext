---
title: "Property1DBar()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

1D Bar property

## Syntax

```psj
Property1DBar(string Name, int Id, color propertyColor, Cursor Section, int ShapeDataType, Cursor Material,
    double Area, double[3] Orient, double[3] Inertia, double TorConst, double NSM,
    double ShearAreaFactor1, double ShearAreaFactor2, double StressRevoceryCoeff _Cy,
    double StressRevoceryCoeff _Cz, double StressRevoceryCoeff _Dy, double StressRevoceryCoeff _Dz,
    double StressRevoceryCoeff _Ey, double StressRevoceryCoeff _Ez, double StressRevoceryCoeff _Fy,
    double StressRevoceryCoeff _Fz, bool PinA0, bool PinA1, bool PinA2, bool PinA3,
    bool PinA4, bool PinA5, bool PinB0, bool PinB1, bool PinB2, bool PinB3, bool PinB4,
    bool PinB5, double[3] PointA, double[3] PointB, int LocalLengthUnit, int LocalMassUnit,
    Cursor[] Target, Cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Name

<!-- @since:5.0.1 -->
### 2. Int

ID

<!-- @since:5.1.0 -->
### 3. Color

Color of the property.

<!-- @since:5.1.0 -->
### 4. Int

Shape data type \[SHAPE\_TYPE\_UNKNOWN = 0, SHAPE\_TYPE\_M3 = 1, SHAPE\_TYPE\_M4 =2, SHAPE\_TYPE\_M6 = 3, SHAPE\_TYPE\_M8 = 4, SHAPE\_TYPE\_M10 = 5, SHAPE\_TYPE\_M12 = 6, SHAPE\_TYPE\_M14 = 7, SHAPE\_TYPE\_M16 = 8, SHAPE\_TYPE\_M18 = 9, SHAPE\_TYPE\_M20 = 10, SHAPE\_TYPE\_M22 = 11, SHAPE\_TYPE\_M24 = 12, SHAPE\_TYPE\_M26 = 13, SHAPE\_TYPE\_M28 = 14, SHAPE\_TYPE\_M30 = 15, SHAPE\_TYPE\_M32 = 16, SHAPE\_TYPE\_M34 = 17, SHAPE\_TYPE\_M36 = 18, SHAPE\_TYPE\_CIRC = 19]

<!-- @since:5.1.0 -->
### 5. Cursor

Material

<!-- @since:5.1.0 -->
### 6. Double

Area

<!-- @since:5.0.1 -->
### 7. Double\[3]

Orient Vector double list \[x,y,z]

<!-- @since:5.1.0 -->
### 8. Double\[3]

Inertia double list \[Izz,Iyy,Izy]

<!-- @since:5.0.1 -->
### 9. Double

Tor const

<!-- @since:5.1.0 -->
### 10 Double

NSM

<!-- @since:5.0.1 -->
### 11. Double

Shear area factor K1

<!-- @since:5.0.1 -->
### 12. Double

Shear area factor K2

<!-- @since:5.0.1 -->
### 13. Double

Stress recovery coefficient Cy

<!-- @since:5.0.1 -->
### 14. Double

Stress recovery coefficient Cz

<!-- @since:5.0.1 -->
### 15. Double

Stress recovery coefficient Dy

<!-- @since:5.0.1 -->
### 16. Double

Stress recovery coefficient Dz

<!-- @since:5.0.1 -->
### 17. Double

Stress recovery coefficient Ey

<!-- @since:5.0.1 -->
### 18. Double

Stress recovery coefficient Ez

<!-- @since:5.0.1 -->
### 19. Double

Stress recovery coefficient Fy

<!-- @since:5.1.0 -->
### 20. Double

Stress recovery coefficient Fz

<!-- @since:5.0.1 -->
### 21. Bool

Pin flag at A0 true = 1, false = 0

<!-- @since:5.0.1 -->
### 22. Bool

Pin flag at A1 true = 1, false = 0

<!-- @since:5.0.1 -->
### 23. Bool

Pin flag at A2 true = 1, false = 0

<!-- @since:5.0.1 -->
### 24. Bool

Pin flag at A3 true = 1, false = 0

<!-- @since:5.0.1 -->
### 25. Bool

Pin flag at A4 true = 1, false = 0

<!-- @since:5.0.1 -->
### 26. Bool

Pin flag at A5 true = 1, false = 0

<!-- @since:5.0.1 -->
### 27. Bool

Pin flag at B0 true = 1, false = 0

<!-- @since:5.0.1 -->
### 28. Bool

Pin flag at B1 true = 1, false = 0

<!-- @since:5.0.1 -->
### 29. Bool

Pin flag at B2 true = 1, false = 0

<!-- @since:5.0.1 -->
### 30. Bool

Pin flag at B3 true = 1, false = 0

<!-- @since:5.0.1 -->
### 31. Bool

Pin flag at B4 true = 1, false = 0

<!-- @since:5.1.0 -->
### 32. Bool

Pin flag at B5 true = 1, false = 0

<!-- @since:5.0.1 -->
### 33. Double\[3]

Offset PointA double list

<!-- @since:5.1.0 -->
### 34. Double\[3]

Offset PointB double list

<!-- @since:5.0.1 -->
### 35. Int

Local Unit Length

<!-- @since:5.1.0 -->
### 36. Int

Local Unit mass

<!-- @since:5.1.0 -->
### 37. Cursor\[]

Target list

<!-- @since:5.1.0 -->
### 38. Cursor

Edit 1D Bar

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 3. Int

Shape data type \[SHAPE\_TYPE\_UNKNOWN = 0, SHAPE\_TYPE\_M3 = 1, SHAPE\_TYPE\_M4 =2, SHAPE\_TYPE\_M6 = 3, SHAPE\_TYPE\_M8 = 4, SHAPE\_TYPE\_M10 = 5, SHAPE\_TYPE\_M12 = 6, SHAPE\_TYPE\_M14 = 7, SHAPE\_TYPE\_M16 = 8, SHAPE\_TYPE\_M18 = 9, SHAPE\_TYPE\_M20 = 10, SHAPE\_TYPE\_M22 = 11, SHAPE\_TYPE\_M24 = 12, SHAPE\_TYPE\_M26 = 13, SHAPE\_TYPE\_M28 = 14, SHAPE\_TYPE\_M30 = 15, SHAPE\_TYPE\_M32 = 16, SHAPE\_TYPE\_M34 = 17, SHAPE\_TYPE\_M36 = 18, SHAPE\_TYPE\_CIRC = 19]

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 4. Cursor

Material

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 5. Double

Area

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 6. Double\[3]

Orient Vector double list \[x,y,z]

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 8. Double

Tor const

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 10. Double

Shear area factor K1

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 20. Bool

Pin flag at A0 true = 1, false = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 32. Double\[3]

Offset PointA double list

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 34. Int

Local Unit Length

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 36. Cursor\[]

Target list

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 37. Cursor

Edit 1D Bar

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Property1DBar("BAR3", 1, 14572863, 93:1, 0, 22:2, 3.14159e-06, [0, 1, 0], [7.85398e-13, 7.85398e-13, 0],
    1.5708e-12, 1.79769e+308, 0.9, 0.9, 0.001, -0, 0, 0.001, -0.001, 0, -0, -0.001, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, [1.7976931e+308, 1.7976931e+308, 1.7976931e+308],
    [1.7976931e+308, 1.7976931e+308, 1.7976931e+308], 0, 0, [5:1], 0:0)
```
