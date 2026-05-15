---
title: "DYNAMIC _TRANS _ANALYSIS _LOAD()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set the transient response arbitrary excitation input.

## Syntax

```psj
DYNAMIC _TRANS _ANALYSIS _LOAD(cursor crParentAnalysis, cursor crCoordinate, str strName, int iLoadType, iLoadDirection, double[] dlForce, double dAmplitude, double dDelay, double dPhase, bool bFt, double dFt, cursor crFtTable, double dT1, double dT2, double dFrequency, double dExponent, double dPower, cursor[] crlTargetNodes, cursor crEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor

- A Cursor specifying the target analysis. A new analysis is created if this parameter is set as None.

<!-- @since:5.1.0 -->
### 2. cursor

- A Cursor specifying the coordinate system.

<!-- @since:5.1.0 -->
### 3. str

- A String specifying the name of load condition to be created.

<!-- @since:5.1.0 -->
### 4. int

- An Integer specifying the load type.

<!-- @since:5.1.0 -->
### 5. int

- An Integer specifying the direction of vibration.

<!-- @since:5.1.0 -->
### 6. double\[]

- A List of Double specifying the vector of vibration force.

<!-- @since:5.1.0 -->
### 7. double

- A Double specifying the amplitude of vibration load.

<!-- @since:5.1.0 -->
### 8. double

- A Double specifying the value of time delay (seconds).

<!-- @since:5.1.0 -->
### 9. double

- A Double specifying the value of phase delay (angle) in load type Cosine(TLOAD2).

<!-- @since:5.1.0 -->
### 10. bool

- A Boolean specifying whether to use the time history load as inputted value or table.

<!-- @since:5.1.0 -->
### 11. double

- A Double specifying the value of the time history load.

<!-- @since:5.1.0 -->
### 12. cursor

- A Cursor specifying the field data of the time history load.

<!-- @since:5.1.0 -->
### 13. double

- A Double specifying the vibration start time of load type Cosine(TLOAD2).

<!-- @since:5.1.0 -->
### 14. double

- A Double specifying the vibration end time of load type Cosine(TLOAD2).

<!-- @since:5.1.0 -->
### 15. double

- A Double specifying the value of frequency in load type Cosine(TLOAD2).

<!-- @since:5.1.0 -->
### 16. double

- A Double specifying the value of exponential function in load type Cosine (TLOAD2).

<!-- @since:5.1.0 -->
### 17. double

- A Double specifying the value of growth factor in load type Cosine (TLOAD2).

<!-- @since:5.1.0 -->
### 18. cursor\[]

- A List of Cursor specifying the selected nodes which can be assigned the load condition.

<!-- @since:5.1.0 -->
### 19. cursor

- A Cursor specifying an existing Load condition

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
DYNAMIC _TRANS _ANALYSIS _LOAD(0:0, 0:0, "TRNLoad1", 0, 0, [1, 0, 0], 1.0, 0.0, 0.0, 1, 1.0, 0:0, 0.0, 1.0, 0.0, 0.0, 0.0, [0:0], 0:0)
```
