---
title: "DYNAMIC _GURURI _ANALYSIS _SWEEP()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Output specified element/frequency result output to external file.

## Syntax

```psj
DYNAMIC _GURURI _ANALYSIS _SWEEP(str strExportFilePath, cursor[] crlTargetElem, cursor crParentAnalysis, cursor crCoordinate, bool bAllModesUsed, str[] strlSelectedModesName, bool bUseDampingFactor, double dDampingFactor, cursor crDampingFactorTable, double[] dlInputFrequency, double dStartPhase, int iStepNumber, bool bOutputMaximumGururiResult, int iPrincipleType, bool bAllCase, cursor crSelectedLoadCase, cursor crEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

A String specifying the path of result file to be exported.

<!-- @since:5.1.0 -->
### 2. cursor\[]

A List of Cursor specifying the target solid elements.

<!-- @since:5.1.0 -->
### 3. cursor

A Cursor specifying the target job to be processed.

<!-- @since:5.1.0 -->
### 4. cursor

A Cursor specifying the response points coordinate system.

<!-- @since:5.1.0 -->
### 5. bool

A Boolean specifying whether to use all modes.

<!-- @since:5.1.0 -->
### 6. str\[]

- A List of String specifying the selected modes using for response calculation. This option was used if bAllModesUsed is False.

<!-- @since:5.1.0 -->
### 7. bool

- A Boolean specifying whether to use damping factor for calculation.

<!-- @since:5.1.0 -->
### 8. double

- A Double specifying the value of damping factor.

<!-- @since:5.1.0 -->
### 9. cursor

- A Cursor specifying the field data of damping factor.

<!-- @since:5.1.0 -->
### 10. double\[]

- A Double List specifying the frequency value for analysis.

<!-- @since:5.1.0 -->
### 11. double

- A Double specifying the starting phase to analyze.

<!-- @since:5.1.0 -->
### 12. int

- An Integer specifying the number division of one cycle.

<!-- @since:5.1.0 -->
### 13. bool

- A Boolean specifying whether to output the maximum result of the selected Principal type and store it in a separated tree of assembly window.

<!-- @since:5.1.0 -->
### 14. int

- An Integer specifying the principal result type that will be analyzed.

<!-- @since:5.1.0 -->
### 15. bool

- A Boolean specifying whether to use all current load cases.

<!-- @since:5.1.0 -->
### 16. cursor

- A Cursor specifying the selected load case to analyze. This option was used if bAllLoadCases is False.

<!-- @since:5.1.0 -->
### 17. cursor

- A Cursor specifying an existing Load condition.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
DYNAMIC _GURURI _ANALYSIS _SWEEP("path/to/the/file", [0:0], 0:0, 0:0, 1, [], 1, 1.0, 0:0, [], 0.0, 10, 1, 3, 1, 0:0, 0:0)
```
