---
title: "MoveNodeAlongCylinder()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move Nodes Along desired Cylinder.

## Syntax

```psj
MoveNodeAlongCylinder(cursor[] taFace, cursor[] taNode, double dirX, double dirY,
    double dirZ, double circleX, double circleY, double circleZ, double radius, double height)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target face cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target node cursor(\[10:Node ID])

<!-- @since:5.0.1 -->
### 3. Double

X direction vector of imaginary cylinder

<!-- @since:5.0.1 -->
### 4. Double

Y direction vector of imaginary cylinder

<!-- @since:5.0.1 -->
### 5. Double

Z direction vector of imaginary cylinder

<!-- @since:5.0.1 -->
### 6. Double

X direction center of imaginary cylinder

<!-- @since:5.0.1 -->
### 7. Double

Y direction center of imaginary cylinder

<!-- @since:5.0.1 -->
### 8. Double

Z direction center of imaginary cylinder

<!-- @since:5.0.1 -->
### 9. Double

Radius of imaginary cylinder

<!-- @since:5.0.1 -->
### 10. Double

Height of imaginary cylinder

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeAlongCylinder([], [10:333, 10:341, 10:342, 10:334], 0, 1, 0, 0, 0, 0, 0.01, 0.02)
```
