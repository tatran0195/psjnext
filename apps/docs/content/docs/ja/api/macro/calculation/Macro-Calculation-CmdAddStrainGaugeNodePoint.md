---
title: "CmdAddStrainGaugeNodePoint()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Display stress and strain in the direction connecting two points.

## Syntax

```psj
CmdAddStrainGauge2Nodes(int iNode1, double[] dlPosition, double dWidth, double dHeight, double dAmendFactor, str strGaugeName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

- An Integer specifying the ID of the 1st selected node. This argument can be used for both 2Nodes or Node-Point selection methods.

<!-- @since:5.1.0 -->
### 2. double\[]

- A Double List specifying the coordinate of the selected Point. This argument was used incase of the selection method is Node-Point.

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the width of the selection when the node is picked.

<!-- @since:5.1.0 -->
### 4. double

- A Double specifying the length of the selection when the node is picked.

<!-- @since:5.1.0 -->
### 5. double

- A Double specifying the coefficient for correction that is used for strain analysis results.

<!-- @since:5.1.0 -->
### 6. str

- A String specifying the gauge name.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdAddStrainGaugeNodePoint(0, [0.0,0.0,0.0], 0.0, 0.0, 1.0, "strGaugeName")
```
