---
title: "MoveNodeDeform()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move nodes based on solver result.

## Syntax

```psj
MoveNodeDeform(int solerType, string SolverResult, int step, double scale)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

Solver type. 0: Nastran, 1: ADVC, 2: Abaqus, 3: Abaqus610.

<!-- @since:5.0.1 -->
### 2. String

Path for solver result.

<!-- @since:5.0.1 -->
### 3. int

Indicate the number of step(subcase).

<!-- @since:5.0.1 -->
### 4. Double

Scale the magnitude of the result.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeDeform(0, "C:/Temp/NastranData.op2", 0, 1)
```
