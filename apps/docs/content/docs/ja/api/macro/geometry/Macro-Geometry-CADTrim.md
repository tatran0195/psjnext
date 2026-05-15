---
title: "CADTrim()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

CAD Trim

## Syntax

```psj
CADTrim(Cursor[] Face Cursor, Cursor[] Body Cursor, double Trim Size, double Trim Angle)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target Faces for CAD Trim

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target Bodies for CAD Trim

<!-- @since:5.0.1 -->
### 3. Double

Trim Size

<!-- @since:5.0.1 -->
### 4. Double

Trim Angle

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
GeometryCADTrim([], [3:8], 0.001, 15)
```
