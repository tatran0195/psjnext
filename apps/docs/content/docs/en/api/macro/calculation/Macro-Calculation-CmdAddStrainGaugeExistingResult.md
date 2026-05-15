---
title: "CmdAddStrainGaugeExistingResult()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Obtain the strain in the vector direction of the existing result.

## Syntax

```psj
CmdAddStrainGaugeExistingResult(int[] ilNodeIDs, int iAnalysisType, int iResultSet, int iTimeStep, int iResultType, double dWidth, double dHeight, double dAmendFactor, str strGaugeName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int\[]

- A List of Integer specifying the IDs of the selected nodes.

<!-- @since:5.1.0 -->
### 2. int

- An Integer specifying the analysis type.

<!-- @since:5.1.0 -->
### 3. int

- An Integer specifying the result set.

<!-- @since:5.1.0 -->
### 4. int

- An Integer specifying the time step.

<!-- @since:5.1.0 -->
### 5. int

- An Integer specifying the result type.

<!-- @since:5.1.0 -->
### 6. double

- A Double specifying the width of the selection when the node is picked.

<!-- @since:5.1.0 -->
### 7. double

- A Double specifying the length of the selection when the node is picked.

<!-- @since:5.1.0 -->
### 8. double

- A Double specifying the coefficient for correction that is used for strain analysis results.

<!-- @since:5.1.0 -->
### 9. str

- A String specifying the gauge name.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdAddStrainGaugeExistingResult([], 0, 1, 1, 1, 0.0, 0.0, 1.0, "strGaugeName")
```
