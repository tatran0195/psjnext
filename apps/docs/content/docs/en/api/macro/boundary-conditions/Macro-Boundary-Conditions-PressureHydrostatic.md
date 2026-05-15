---
title: "PressureHydrostatic()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Pressure hydrostatic

## Syntax

```psj
PressureHydrostatic(String name, double staticPressure, double density, int densityUnit,
    double gravity, int gravityUnit, int gravityDir, double waterSurface, int surfaceUnit,
    int distributionMethod, Cursor[] targets, Cursor crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name

<!-- @since:5.0.1 -->
### 2. Double

static pressure

<!-- @since:5.0.1 -->
### 3. Double

density

<!-- @since:5.0.1 -->
### 4. Int

density unit

<!-- @since:5.0.1 -->
### 5. Double

gravity

<!-- @since:5.0.1 -->
### 6. Int

gravity unit

<!-- @since:5.0.1 -->
### 7. Int

gravity direction

<!-- @since:5.0.1 -->
### 8. Double

water surface

<!-- @since:5.0.1 -->
### 9. Int

water surface unit

<!-- @since:5.0.1 -->
### 10. Int

distributionMethod (0: Per selected entity, 1: Per node, 2: Total of select)

<!-- @since:5.0.1 -->
### 11. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 12. Cursor

edit target

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PressureHydrostatic("PressureHydrostatic1", 0, 1000, 0, 0, 0, 0, 0, 0, 0, [6:23], 0:0)
```
