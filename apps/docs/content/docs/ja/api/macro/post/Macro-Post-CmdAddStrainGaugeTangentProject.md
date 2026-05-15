---
title: "CmdAddStrainGaugeTangentProject()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute Strain Gauge - Tangent Project.

## Syntax

```psj
CmdAddStrainGaugeTangentProject(int node, double Width, double Height, double AmendFactor, int Dir, double Angle, float VecSize, string GaugeName)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Target node.

<!-- @since:5.0.1 -->
### 2. double

Gauge Width.

<!-- @since:5.0.1 -->
### 3. double

Gauge Height.

<!-- @since:5.0.1 -->

#### 4. double

Amend Factor.

<!-- @since:5.0.1 -->

#### 5. int

Original Dir

<!-- @since:5.0.1 -->

#### 6. double

Angle

<!-- @since:5.0.1 -->

#### 7. double

Vector Size

<!-- @since:5.0.1 -->

#### 8. string

Gauge name.

## Return Code

Nothing.

## Sample Code

```psj
CmdAddStrainGaugeTangentProject(9461, 0.006, 0.006, 2, 0, 0, 1, "")
```
