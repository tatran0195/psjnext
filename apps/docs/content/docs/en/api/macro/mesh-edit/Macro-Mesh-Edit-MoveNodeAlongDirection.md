---
title: "MoveNodeAlongDirection()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move node(s) in a specified direction

## Syntax

```psj
MoveNodeAlongDirection(double dX, double dY, double dZ, double planept[0][0],
    double planept[0][1], double planept[0][2], double planept[1][0], double planept[1][1],
    double planept[1][2], double planept[2][0], double planept[2][1], double planept[2][2],
    Cursor face, double magnitude, bool facepicked, bool elempicked, int[] node)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double

Displacement in X Direction

<!-- @since:5.0.1 -->
### 2. Double

Displacement in Y Direction

<!-- @since:5.0.1 -->
### 3. Double

Displacement in Z Direction

<!-- @since:5.0.1 -->
### 4. Double

1st coordinate of plane point1

<!-- @since:5.0.1 -->
### 5. Double

2nd coordinate of plane point1

<!-- @since:5.0.1 -->
### 6. Double

3rd coordinate of plane point1

<!-- @since:5.0.1 -->
### 7. Double

1st coordinate of plane point2

<!-- @since:5.0.1 -->
### 8. Double

2nd coordinate of plane point2

<!-- @since:5.0.1 -->
### 9. Double

3rd coordinate of plane point2

<!-- @since:5.0.1 -->
### 10. Double

1st coordinate of plane point3

<!-- @since:5.0.1 -->
### 11. Double

2nd coordinate of plane point3

<!-- @since:5.0.1 -->
### 12. Double

3rd coordinate of plane point3

<!-- @since:5.0.1 -->
### 13. Cursor

selected face cursor

<!-- @since:5.0.1 -->
### 14. Double

Magnitude

<!-- @since:5.0.1 -->
### 15. Bool

is face picked 0=no,1=yes

<!-- @since:5.0.1 -->
### 16. Bool

is element picked 0=no,1=yes

<!-- @since:5.0.1 -->
### 17. Int\[]

Node List

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeAlongDirection(0.00333333, 0, -0.00111111, 0.01, 0, 0, 0.01, 0.00111111, 0,
    0.01, 0.00111111, 0.00111111, 6:24, 0.00351364, 1, 0, [443, 437])
```
