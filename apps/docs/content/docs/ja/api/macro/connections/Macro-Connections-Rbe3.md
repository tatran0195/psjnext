---
title: "Rbe3()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create rbe3 connection

## Syntax

```psj
Rbe3(int Method, Cursor[] MasterTarget, Cursor[] SlaveTarget, RBE3TermAttribute[] termAtbs,
    int RBE3Type, string name, Cursor CoordSystem, double Tolerance, double[3] VisualNodePos,
    int SurfaceDef, Cursor edit, bool UpdateDispCS, bool CornerOnly )
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

Method RBE3 = 3

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Master Target

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Slave Target

<!-- @since:5.0.1 -->
### 4. RBE3TermAttribute\[]

Term attribute list

\*RBE3TermAttribute:(double Coefficient, int DOF, int Count)

<!-- @since:5.0.1 -->
### 5. Int

RBE3 Type

<!-- @since:5.0.1 -->
### 6. string

Name of RBE3

<!-- @since:5.0.1 -->
### 7. Cursor

Coordinate

<!-- @since:5.0.1 -->
### 8. Double

Tolerance

<!-- @since:5.0.1 -->
### 9. Double\[3]

Visual node position

<!-- @since:5.0.1 -->
### 10. Int

Surface definition ByNodeSet = 0, ByElementSet = 1

<!-- @since:5.0.1 -->
### 11. Cursor

Edit RBE3

<!-- @since:5.0.1 -->
### 12. Bool

Update disp Coordinate System flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 13. Bool

Corner only flag true = 1, false = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Rbe3(17, [10:157854], [10:224981], [(0, 63, 1), (1, 7, 1)], 3,
    "RBE3 _1", 0:0, 0, [0, 0, 0], 0, 0:0, 1, 0)
```
