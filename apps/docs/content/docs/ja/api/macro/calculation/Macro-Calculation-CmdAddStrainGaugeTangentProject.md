---
title: "CmdAddStrainGaugeTangentProject()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Display the tangential strain at each node.

## Syntax

```psj
CmdAddStrainGaugeTangentProject(int[] ilNodeIDs, double dWidth, double dHeight, int nDirection, double dAngle, double dVectorSize, double dAmendFactor, str strGaugeName)
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
### 4. int

- An Integer specifying the original direction which is selected from maximum principal stress, minimum principal stress, X-axis, Y-axis, and Z-axis.

<!-- @since:5.1.0 -->
### 5. double

- A Double specifying the value of rotation angle.

<!-- @since:5.1.0 -->
### 6. double

- A Double specifying the vector size.

<!-- @since:5.1.0 -->
### 7. double

- A Double specifying the coefficient for correction that is used for strain analysis results.

<!-- @since:5.1.0 -->
### 8. str

- A String specifying gauge name.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdAddStrainGaugeTangentProject([], 0.0, 0.0, 0, 0.0, 1.0, 1.0, "strGaugeName")
```
