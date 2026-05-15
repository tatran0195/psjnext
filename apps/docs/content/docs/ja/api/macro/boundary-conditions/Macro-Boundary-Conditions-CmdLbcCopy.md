---
title: "CmdLbcCopy()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Copy properties by translation

There are 3 cases:

- Copy translation

- Copy rotation

- Copy mirror

## Syntax

```psj
COPY TRANS: CmdLbcCopy(int Method, int MatchMethod, double[3] TransVec, double Magnitude,
    double Offset, double Tolerance, Cursor Coordinate, Cursor[] Target)
```

```psj
COPY ROTATE: CmdLbcCopy(int Method, int MatchMethod, double[3] AxisVec,
    double[3] CenterVec, double Angle, double Tolerance, Cursor Coordinate , Cursor[] Target)
```

```psj
COPY MIRROR: CmdLbcCopy(int Method, int MatchMethod, double[3] Points,
    double Offset, double Tolerance, Cursor[] Target)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

Method COPY TRANS = 0, COPY ROTATE = 1, COPY MIRROR = 2

<!-- @since:5.0.1 -->
### 2. Int

Match method MATCH NODE = 0, MATCH FEATURE = 1

<!-- @since:5.0.1 -->
### 3. Double\[3]

Trans vector

<!-- @since:5.0.1 -->
### 4. Double

Magnitude

<!-- @since:5.0.1 -->
### 5. Double

Offset

<!-- @since:5.0.1 -->
### 6. Double

Tolerance

<!-- @since:5.0.1 -->
### 7. Cursor

Coordinate

<!-- @since:5.0.1 -->
### 8. Double\[3]

Axis vector

<!-- @since:5.0.1 -->
### 9. Double\[3]

Center vector

<!-- @since:5.0.1 -->
### 10. Double

Angle

<!-- @since:5.0.1 -->
### 11. Cursor

Coordinate

<!-- @since:5.0.1 -->
### 12. Double\[3]

Points

<!-- @since:5.0.1 -->
### 13. Double

Offset

<!-- @since:5.0.1 -->
### 14. Double

Tolerance

<!-- @since:5.0.1 -->
### 15. Cursor\[]

Target (LBC/Property/Connection/Group)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdLbcCopy(0, 0, [0.001, 0, 0], 0.03, 0, 0.0001, 0:0, [40:1])
```
