---
title: "DYNAMIC _FREQ _INTERACTIVE _LOAD _AND _RESPONSE()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Execute Frequency Analysis (Interactive) command.

## Syntax

```psj
DYNAMIC _FREQ _INTERACTIVE _LOAD _AND _RESPONSE(curl arTarget, string strName, double Amplitude, double Delay, double Phase, double dBf, double dFf, double dDampingFactor, double StyleParamTop, double StyleParamMid, double StyleParamBot, int iLoadPtn, double[] vecForce, bool bBf, bool bFf, bool bUnitLoad, bool bCentripetalForce, bool bAllModesUsed, bool bIncludeEigenValue, bool bDampingFactor, cursor crBfCurve, cursor crFfCurve, cursor crCoord, string[] vecstrModesSelect, cursor crParentAnalysis, int CurStyle, int ResultType, int ResultPos, string[] vecstrSelectedResultName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor

A Cursor specifying a target node to set load and calculate response.

<!-- @since:5.1.0 -->
### 2. string

Name of the load case.

<!-- @since:5.1.0 -->
### 3. double

A Double specifying amplitude.

<!-- @since:5.1.0 -->
### 4. double

A Double specifying delay of the force.

<!-- @since:5.1.0 -->
### 5. double

A Double specifying Phase.

<!-- @since:5.1.0 -->
### 6. double

A Double specifying value of B(f) with double format.

<!-- @since:5.1.0 -->
### 7. double

A Double specifying value of F(f) with double format.

<!-- @since:5.1.0 -->
### 8. double

A Double specifying value of the damping factor with double format.

<!-- @since:5.1.0 -->
### 9. double

A Double specifying the analysis Start

<!-- @since:5.1.0 -->
### 10. double

A Double specifying the Step Size or the Step Number (defined by 27th argument.)

<!-- @since:5.1.0 -->
### 11. double

A Double specifying the End or the Step Size (defined by 27th argument.)

<!-- @since:5.1.0 -->
### 12. int

An Integer specifying load pattern.

- 0: X
- 1: Y
- 2: Z
- 3: RX
- 4: RY
- 5: RZ
- 6: Normal

<!-- @since:5.1.0 -->
### 13. double\[]

load value. It automatically calculated by the other parameters.

<!-- @since:5.1.0 -->
### 14. bool

A boolean specifying whether to input value of B(f) with double format or table format.

- 0: double
- 1: table

<!-- @since:5.1.0 -->
### 15. bool

A boolean specifying whether to input value of F(f) with double format or table format.

- 0: double
- 1: table

<!-- @since:5.1.0 -->
### 16. bool

A Boolean specifying whether to use the unit load.

- 0: no
- 1: yes

<!-- @since:5.1.0 -->
### 17. bool

The flag specifying whether includes centripetalForce

- 0: no
- 1: yes

<!-- @since:5.1.0 -->
### 18. bool

A Boolean specifying whether to use the all modes used.

- 0: no
- 1: yes
-

<!-- @since:5.1.0 -->
### 19. bool

A Boolean specifying whether to include eigenvalue.

- 0: no
- 1: yes

<!-- @since:5.1.0 -->
### 20. bool

Specify whether to input value of damping factor with double format or table format.

- 0: table format
- 1: double format

<!-- @since:5.1.0 -->
### 21. Cursor

A Cursor specifying value of B(f) with table format.

<!-- @since:5.1.0 -->
### 22. Cursor

A Cursor specifying value of F(f) with table format.

<!-- @since:5.1.0 -->
### 23. Cursor

A Cursor specifying value of the damping factor with table format.

<!-- @since:5.1.0 -->
### 24. Cursor

A Cursor specifying a reference coordinate.
It always set global (0:0)

<!-- @since:5.1.0 -->
### 25. string\[]

String vector of selected modes if 19th argument is set 0.

<!-- @since:5.1.0 -->
### 26. Cursor

A Cursor specifying existing dynamic freq interactive analysis.

<!-- @since:5.1.0 -->
### 27. int

Input Style. Change values of argument 9 to 12.

- 0: Start, StepNumber, StepSize
- 1: Start, StepSize, End
- 2: Start, StepNumber, End

<!-- @since:5.1.0 -->
### 28. int

Result type.

- 0: Displacement
- 1: Velocity
- 2: Acceleration

<!-- @since:5.1.0 -->
### 29. int

Result position.
It is always set to 0 (on node).

<!-- @since:5.1.0 -->
### 30. string\[]

Directions in string representation.

## Return Code

Data for draw curve (string)

## Sample Code

```psj
DYNAMIC _FREQ _INTERACTIVE _LOAD _AND _RESPONSE([10:788], "Freq _Response _1", 1, 0, 0, 1, 0, 0.01, 0, 1, 200, 6, [0, -0.7071067811865476, 0.7071067811865476], 0, 0, 0, 0, 1, 0, 1, 0:0, 0:0, 0:0, 0:0, [], 0:0, 1, 0, 0, ["Normal"])
```
