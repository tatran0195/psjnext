---
title: "CmdAddStrainGaugeAxisAngle()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Display stress/strain data for an input rotation angle from the first defined axis on a plane consisting of two axes.

## Syntax

```psj
CmdAddStrainGaugeAxisAngle(int[] ilNodeIDs, int nAxis1, int nAxis2, double dAngle, double dWidth, double dHeight, double dAmendFactor, str strGaugeName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int\[]

- A List of Integer specifying the IDs of the selected nodes.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying the first axis from maximum principal stress, minimum principal stress, and middle principal stress.

<!-- @since:5.1.0 -->
### 3. int

- An Integer specifying the second axis from the minimum principal stress and the middle principal stress.

<!-- @since:5.1.0 -->
### 4. double

- A Double specifying the value of rotation angle.

<!-- @since:5.1.0 -->
### 5. double

- A Double specifying the width of the selection when the node is picked.

<!-- @since:5.1.0 -->
### 6. double

- A Double specifying the length of the selection when the node is picked.

<!-- @since:5.1.0 -->
### 7. double

- A Double specifying the coefficient for correction that is used for strain analysis results.

<!-- @since:5.1.0 -->
### 8. str

- A String specifying the gauge name.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdAddStrainGaugeAxisAngle([], 0, 1, 0.0, 0.0, 0.0, 1.0, "strGaugeName")
```
