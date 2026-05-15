---
title: "ConnectionNewMass()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

## Syntax

```psj
ConnectionNewMass(String m _strName, Cursor[] m _taTarget, double value, int dof, bool designer, Cursor coordinate, double offset0, double offset1, double offset2, double inertia0, double inertia1, double inertia2, double inertia3, double inertia4, double inertia5,Cursor m _crEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

Name

<!-- @since:5.1.0 -->
### 2. Cursor\[]

Target Entity

<!-- @since:5.1.0 -->
### 3. Double

Mass value

<!-- @since:5.1.0 -->
### 4. int

DOF

<!-- @since:5.1.0 -->
### 5. Bool

License switcher: Designer or Base

<!-- @since:5.1.0 -->
### 6. Cursor\[]

Coordinate

<!-- @since:5.1.0 -->
### 7. Double

Offset0

<!-- @since:5.1.0 -->
### 8. Double

Offset1

<!-- @since:5.1.0 -->
### 9. Double

Offset2

<!-- @since:5.1.0 -->
### 10. Double

Inertia0

<!-- @since:5.1.0 -->
### 11. Double

Inertia1

<!-- @since:5.1.0 -->
### 12. Double

Inertia2

<!-- @since:5.1.0 -->
### 13. Double

Inertia3

<!-- @since:5.1.0 -->
### 14. Double

Inertia4

<!-- @since:5.1.0 -->
### 15. Double

Inertia5

<!-- @since:5.1.0 -->
### 16. Cursor

Edit Cursor

<!-- @since:5.1.0 -->
### 17. Bool

Update displacement CS or not.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

ConnectionNewMass("Mass\_1", \[10:471], 1000, 6, 0, 0:0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0:0, 1)
