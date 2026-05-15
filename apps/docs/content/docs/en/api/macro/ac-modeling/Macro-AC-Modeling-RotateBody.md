---
title: "RotateBody()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Rotate Body

## Syntax

```psj
RotateBody(cursor[] body, double[3] rotate _centre, double[3] rotate _axis, double rotate _angle,
    bool create _new, bool copy _lbc, int copy _count, bool merge _node, double tolerance)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Body List

<!-- @since:5.0.1 -->
### 2. Double\[3]

Rotate Centre

<!-- @since:5.0.1 -->
### 3. Double\[3]

Rotate Axis

<!-- @since:5.0.1 -->
### 4. Double

Rotate Angle(Radian)

<!-- @since:5.0.1 -->
### 5. Bool

Create New Body 1=Yes, 0=No

<!-- @since:5.0.1 -->
### 6. Bool

Copy LBC 1=Yes, 0=No

<!-- @since:5.0.1 -->
### 7. Int

Copy Count

<!-- @since:5.0.1 -->
### 8. Bool

Merge Node 1=Yes, 0=No

<!-- @since:5.0.1 -->
### 9. Double

Merge Node Tolerance

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
RotateBody([3:1], [0.005, 0, 0.01], [0.001, 0, 0], 0.785398, 0, 0, 0, 0, 0)
```
