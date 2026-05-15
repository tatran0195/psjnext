---
title: "ACCombinedAnimation()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Animate deformations, contour colors, and vectors with separately selected physical quantities.

## Syntax

```psj
ACCombinedAnimation(int iTimeStep, int iAnalysisType, str strTargetAnalysisName, bool bDeform, bool bContour, bool bVector,  int iContourSetting, int iVectorSetting)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

- The time step for the animation

<!-- @since:5.1.0 -->
### 2. int

- The type of analysis

<!-- @since:5.1.0 -->
### 3. str

- The name of the target analysis for the animation

<!-- @since:5.1.0 -->
### 4. bool

- Deformmation  (True = 1, False = 0)

<!-- @since:5.1.0 -->
### 5. bool

- Contour  (True = 1, False = 0)

<!-- @since:5.1.0 -->
### 6. Bool

- Vector  (True = 1, False = 0)

<!-- @since:5.1.0 -->
### 7. int

- Contour option

<!-- @since:5.1.0 -->
### 8. int

- Vector option

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ACCombinedAnimation(1, 1, "Fluid Pressure", 1, 1, 1, 0, 0)
```
