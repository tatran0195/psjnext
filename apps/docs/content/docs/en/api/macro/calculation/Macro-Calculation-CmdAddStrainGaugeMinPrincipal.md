---
title: "CmdAddStrainGaugeMinPrincipal()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Display stress or strain in the direction of the minimum principle stress.

## Syntax

```psj
CmdAddStrainGaugeMinPrincipal(int[] ilNodeIDs, double dWidth, double dHeight, double dAmendFactor, str strGaugeName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int\[]

- A List of Integer specifying the IDs of the selected nodes.

<!-- @since:5.1.0 -->
### 2. double

- A Double specifying the width of the selection when the node is picked.

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the length of the selection when the node is picked.

<!-- @since:5.1.0 -->
### 4. double

- A Double specifying the coefficient for correction that is used for strain analysis results.

<!-- @since:5.1.0 -->
### 5. str

A String specifying the gauge name.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdAddStrainGaugeMinPrincipal([], 0.0, 0.0, 1.0, "strGaugeName")
```
