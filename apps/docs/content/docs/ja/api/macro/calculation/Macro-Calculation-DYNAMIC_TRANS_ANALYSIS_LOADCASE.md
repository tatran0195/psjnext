---
title: "DYNAMIC _TRANS _ANALYSIS _LOADCASE()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create a load case for transient response analysis.

## Syntax

```psj
DYNAMIC _TRANS _ANALYSIS _LOADCASE(cursor crParentAnalysis, str strName, double dFactor, int iNewID, cursor[] crlSelectionLoad, double[] dlTargetFactor, cursor crEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor

- A Cursor specifying the target analysis to be create a load case. A new analysis is created if this parameter is set as None.

<!-- @since:5.1.0 -->
### 2. str

- A String specifying the name of load case to be created.

<!-- @since:5.1.0 -->
### 3. double

- A Double specifying the load coefficient for the entire load cases to be created.

<!-- @since:5.1.0 -->
### 4. int

- An Integer specifying the ID of the load case to be created.

<!-- @since:5.1.0 -->
### 5. cursor\[]

- A List of Cursor specifying the selected loads will be used in the load case to be created.

<!-- @since:5.1.0 -->
### 6. double\[]

- A Double List specifying the coefficient for each selected load in the corresponding order.

<!-- @since:5.1.0 -->
### 7. cursor

- A Cursor specifying an existing load case condition

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
DYNAMIC _TRANS _ANALYSIS _LOADCASE(0:0, "LoadCase1", 1.0, 1, [0:0], [], 0:0)
```
