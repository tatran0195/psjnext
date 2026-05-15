---
title: "ResponseCondition()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Output the result of the response point for transient response.

## Syntax

```psj
DYNAMIC _FREQ _ANALYSIS _RESPONSE(cursor crParentAnalysis, cursor crCoordinate, bool bAllModesUsed, str[] strlModesSelect, bool bDampingFactor, double dDampingFactor, cursor crDampingFactor, int iCurveStyle, double dStyleParamTop, double dStyleParamMid, double dStyleParamBot, bool bIncludeEigenValue, bool bCreateNewResult, int iResultType, str[]strlSelectedResultName, int iResultPos, bool bAllCase, cursor crSelectedLoadCase, bool bSeparateLoad, cursor[] crlTargets, cursor crEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor

- A Cursor specifying the target job to be processed.

<!-- @since:5.1.0 -->
### 2. cursor

- A Cursor specifying the output coordinate system.

<!-- @since:5.1.0 -->
### 3. bool

- A Boolean specifying whether to use all modes.

<!-- @since:5.1.0 -->
### 4. str\[]

- A List of String specifying the selected modes using for response calculation. This option was used if bAllModesUsed is False.

<!-- @since:5.1.0 -->
### 5. bool

- A Boolean specifying whether to use damping factor for calculation.

<!-- @since:5.1.0 -->
### 6. double

- A Double specifying the value of damping factor.

<!-- @since:5.1.0 -->
### 7. cursor

- A Cursor specifying the field data of damping factor.

<!-- @since:5.1.0 -->
### 8. int

- An Integer specifying the style of time range for the calculation.

<!-- @since:5.1.0 -->
### 9. double

- A Double specifying the analysis start value of the selected curve style.

<!-- @since:5.1.0 -->
### 10. double

- A Double specifying the step size value of the selected curve style.

<!-- @since:5.1.0 -->
### 11. double

- A Double specifying the analysis end value of the selected curve style.

<!-- @since:5.1.0 -->
### 12. bool

- A Double specifying the analysis end value of the selected curve style.

<!-- @since:5.1.0 -->
### 13. bool

- A Boolean specifying whether to create new results (displacement and stress) for the entire model.

<!-- @since:5.1.0 -->
### 14. int

- An Integer specifying the result type to be calculated.

<!-- @since:5.1.0 -->
### 15. str\[]

- A List of String specifying the component results according to the selected result type.

<!-- @since:5.1.0 -->
### 16. int

- An Integer specifying the output position of the result.

<!-- @since:5.1.0 -->
### 17. bool

- A Boolean specifying whether to use all current load cases.

<!-- @since:5.1.0 -->
### 18. cursor

- A Cursor specifying the selected load case to analyze. This option was used if bAllLoadCases is False.

<!-- @since:5.1.0 -->
### 19. bool

- A Boolean specifying whether to calculate the response to each set load.

<!-- @since:5.1.0 -->
### 20. cursor\[]

- A List of Cursor specifying the target to calculate the response. The target is node or solid element.

<!-- @since:5.1.0 -->
### 21. cursor

- A Cursor specifying an existing response condition

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
DYNAMIC _FREQ _ANALYSIS _RESPONSE(0:0, 0:0, 1, [], 1, 0.01, 0:0, 1, 0.0, 1.0, 1.0, 0, 0, 0, ["TX"], 0, 1, 0:0, 1, [0:0], 0:0)
```
