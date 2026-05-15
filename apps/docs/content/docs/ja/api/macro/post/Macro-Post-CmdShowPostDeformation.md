---
title: "CmdShowPostDeformation()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show deformation.

## Syntax

```psj
CmdShowPostDeformation(Cursor crPostJob,
    int analysisType, int resultSet, int timeStep, int opComplex, float phaseAngle, int scaleMethod, float dispRatio, bool eachDispComp, 
    float dispRatioEachX,  float dispRatioEachY, float dispRatioEachZ, bool bApplyAll)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

Cursor of post job.

<!-- @since:5.0.1 -->
### 2. int

Analysis type.

<!-- @since:5.1.0 -->
### 3. PostResultKey::int

Analysis ID.

<!-- @since:5.0.1 -->
### 4. int

Result set

<!-- @since:5.0.1 -->
### 5. int

Time step

<!-- @since:5.1.0 -->
### 6. string

Name of result

<!-- @since:5.1.0 -->
### 7. string

Name of component

<!-- @since:5.1.0 -->
### 8. int

opComplex

<!-- @since:5.1.0 -->
### 9. float

phaseAngle

<!-- @since:5.1.0 -->
### 10. int

scaling method

<!-- @since:5.0.1 -->
### 11. float

Display ratio

<!-- @since:5.1.0 -->
### 12. bool

Each direction ratio flag

<!-- @since:5.1.0 -->
### 13. float

Deformation X

<!-- @since:5.1.0 -->
### 14. float

Deformation Y

<!-- @since:5.1.0 -->
### 15. float

Deformation Z

<!-- @since:5.1.0 -->
### 16. bool

Apply all flag

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 3. int

Result set

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 6. float

phaseAngle

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 7. int

scaling method

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 8. float

Display ratio

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 9. bool

Each direction ratio flag

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 10. float

Deformation X

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 12. float

Deformation Z

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 13. bool

Apply all flag

## Return Code

Nothing.

## Sample Code

```psj
CmdShowPostDeformation(183:1, 2, 0, 1, 1, Displacement, Translational, 0, 0.000000, 0, 0.070000, 0, 0.070000, 0.070000, 0.070000, 0)
```
