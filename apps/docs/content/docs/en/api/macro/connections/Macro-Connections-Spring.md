---
title: "Spring()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create spring connection

## Syntax

```psj
Spring(int method, String name, Cursor[] master, Cursor[] slave,Cursor coord, int springType,
    int ground, double tol, int dir, int distMode, int dof1, int dof2, double dampCoef,
    double stressCoef, double[3] transStiffness, double[3] rotStiffness, Cursor editObj )
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

method to create spring, 17: any entities(1:1)

<!-- @since:5.0.1 -->
### 2. String

name of spring

<!-- @since:5.0.1 -->
### 3. Cursor\[]

master entities of spring

<!-- @since:5.0.1 -->
### 4. Cursor\[]

master entities of spring

<!-- @since:5.0.1 -->
### 5. Cursor

referred coordinate system, NULL is global

<!-- @since:5.0.1 -->
### 6. Int

type of spring, 0: general, 1: DoF, 2: uniform DoF

<!-- @since:5.0.1 -->
### 7. Int

ground or not, 0: no, 1: yes

<!-- @since:5.0.1 -->
### 8. Double

tolerance to find node pair

<!-- @since:5.0.1 -->
### 9. Int

direction of spring, 0: isotropic, 1: anisotropic

<!-- @since:5.0.1 -->
### 10. Int

distribute mode, not used

<!-- @since:5.0.1 -->
### 11. Int

DoF at reference

<!-- @since:5.0.1 -->
### 12. Int

DoF at target

<!-- @since:5.0.1 -->
### 13. Double

Damping coef.

<!-- @since:5.0.1 -->
### 14. Double

Stress coef.

<!-- @since:5.0.1 -->
### 15. Double\[3]

stiffness

<!-- @since:5.0.1 -->
### 16. Double\[3]

Rotate stiffness

<!-- @since:5.0.1 -->
### 17. Cursor

used for edit mode

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Spring(17, "Spring _1", [5:66316], [5:66299], 0:0, 2, 0, 0, 0, 0, 0, 0, 1.2, 1.5,
    [1000, 2000, 1000], [1.7976931e+308, 1.7976931e+308, 1.7976931e+308], 1, 0:0)
```
