---
title: "DYNAMIC _FREQ _ANALYSIS _LOAD()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set the frequency response steady-state excitation input for the Gururi.

## Syntax

```psj
DYNAMIC _FREQ _ANALYSIS _LOAD(int AnalysisType, cursor ParentAnalysis, cursor Coordinate, string Name, int LoadDirection, double[] Force, double Amplitude, double Delay, double Phase, bool Bf, double Bf, cursor BfTable, bool Ff, double Ff, cursor FfTable, bool UnitLoad, bool CentrifugalForce, cursor[] TargetNode, cursor Edit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Int

Choose type of analysis.

<!-- @since:5.1.0 -->
### 2. Cursor

A Cursor specifying the parent analysis.

<!-- @since:5.1.0 -->
### 3. Cursor

A Cursor specifying the coordinate.

<!-- @since:5.1.0 -->
### 4. String

Name of the load case.

<!-- @since:5.1.0 -->
### 5. Int

Choose the direction of load.

<!-- @since:5.1.0 -->
### 6. Double\[]

A Double List specifying the force.

<!-- @since:5.1.0 -->
### 7. Double

A Double specifying amplitude of the force.

<!-- @since:5.1.0 -->
### 8. Double

A Double specifying delay of the force.

<!-- @since:5.1.0 -->
### 9. Double

A Double specifying phase of the force.

<!-- @since:5.1.0 -->
### 10. Bool

Specify whether to input value of B(f) with double format or table format.

### 11. `Double`

A Double specifying value of B(f) with double format.

<!-- @since:5.1.0 -->
### 12. Cursor

A Cursor specifying value of B(f) with table format.

<!-- @since:5.1.0 -->
### 13. Bool

Specify whether to input value of F(f) with double format or table format.

<!-- @since:5.1.0 -->
### 14. Double

A Double specifying value of F(f) with double format.

<!-- @since:5.1.0 -->
### 15. Cursor

A Cursor specifying value of F(f) with table format.

<!-- @since:5.1.0 -->
### 16. Bool

A Boolean specifying whether to use the unit load.

<!-- @since:5.1.0 -->
### 17. Bool

A Boolean specifying whether to use the centrifugal force.

<!-- @since:5.1.0 -->
### 18. Cursor\[]

A Cursor List specifying the target node.

<!-- @since:5.1.0 -->
### 19. Cursor

A Cursor specifying an existing load condition.

## Return Code

A Cursor specifying the created gururi load condition.

## Sample Code

```psj
DYNAMIC _FREQ _ANALYSIS _LOAD(0, 3:1, 2:1, "FRQLOAD _1", 0, [1.0,0.0,0.0], 1.0, 0.0, 0.0, False, 1.0, 2:1, False, 0.0, 2:1, False, False, [], 2:1)
```
