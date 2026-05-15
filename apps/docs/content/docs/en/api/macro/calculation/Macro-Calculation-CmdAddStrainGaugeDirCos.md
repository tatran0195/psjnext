---
title: "CmdAddStrainGaugeDirCos()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Display a graph of the stress/strain in the direction cosine of the entered direction vector.

## Syntax

```psj
CmdAddStrainGaugeDirCos(int[] ilNodeIDs, double[] dlDirectionInput, double dWidth, double dHeight, double dAmendFactor, str strGaugeName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int\[]

- A List of Integer specifying the IDs of the selected nodes.

<!-- @since:5.1.0 -->
### 2. double\[]

- A Double List specifying the direction to get the result.

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the width of the selection when the node is picked.

<!-- @since:5.1.0 -->
### 4. double

- A Double specifying the length of the selection when the node is picked.

<!-- @since:5.1.0 -->
### 5. double

- A Double specifying the coefficient for correction that is used for strain analysis results

<!-- @since:5.1.0 -->
### 6. str

- A String specifying the gauge name.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdAddStrainGaugeDirCos([], [0.0, 0.0, 1.0], 0.0, 0.0, 1.0, "strGaugeName")
```
