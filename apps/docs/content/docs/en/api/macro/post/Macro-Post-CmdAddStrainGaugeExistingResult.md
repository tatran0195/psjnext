---
title: "CmdAddStrainGaugeExistingResult()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute Strain Gauge - Existing result.

## Syntax

```psj
CmdAddStrainGaugeExistingResult(int node, int analysisType, int resultSet, int timeStep, int resultType, double Width, double Height, double AmendFactor, string GaugeName)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Target node.

<!-- @since:5.0.1 -->
### 2. int

Analysis Type.

<!-- @since:5.0.1 -->
### 3. int

Result Set.

<!-- @since:5.0.1 -->
### 4. int

Time step.

<!-- @since:5.0.1 -->
### 5. int

Result type.

<!-- @since:5.0.1 -->
### 6. double

Gauge Width.

<!-- @since:5.0.1 -->
### 7. double

Gauge Height.

<!-- @since:5.0.1 -->

#### 8. double

Amend Factor.

<!-- @since:5.0.1 -->

#### 9. string

Gauge name.

## Return Code

Nothing.

## Sample Code

```psj
CmdAddStrainGaugeExistingResult(23237, 1, 1, 1, 6, 0.003, 0.003, 1, "")
```
