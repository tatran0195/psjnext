---
title: "DYNAMIC _FREQ _ANALYSIS _RESPONSE _SOLVER()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create a response solver for Gururi analysis.

## Syntax

```psj
DYNAMIC _FREQ _ANALYSIS _RESPONSE _SOLVER(cursor ParentAnalysis, cursor Coordinate, bool AllModesUsed, string[] ModesSelect, bool DampingFactor, double DampingFactor, cursor DampingFactor, int CurveStyle, double StyleParamTop, double StyleParamMid, double StyleParamBot, bool IncludeEigenValue, bool CreateNewResult, int ResultType, string[] SelectedResultName, int ResultPos, string DBFileName, string DBVersion, string MethodId, string SPCID, int RESVEC, string JobName, cursor[] Targets, cursor Edit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor

A Cursor specifying the parent analysis.

<!-- @since:5.1.0 -->
### 2. Cursor

A Cursor specifying the coordinate.

<!-- @since:5.1.0 -->
### 3. Bool

A Boolean specifying whether to use the all modes used.

<!-- @since:5.1.0 -->
### 4. String\[]

A String List specifying names of the selected modes.

<!-- @since:5.1.0 -->
### 5. Bool

Specify whether to input value of damping factor with double format or table format.

<!-- @since:5.1.0 -->
### 6. Double

A Double specifying value of the damping factor with doule format.

<!-- @since:5.1.0 -->
### 7. Cursor

A Cursor specifying value of the damping factor with table format.

<!-- @since:5.1.0 -->
### 8. Int

An Integer specifying the curve style.

<!-- @since:5.1.0 -->
### 9. Double

A Double specifying the style of ParamTop.

<!-- @since:5.1.0 -->
### 10. Double

A Double specifying the style of ParamMid.

<!-- @since:5.1.0 -->
### 11. Double

A Double specifying the style of ParamBot.

<!-- @since:5.1.0 -->
### 12. Bool

A Boolean specifying whether to include eigenvalue.

<!-- @since:5.1.0 -->
### 13. Bool

A Boolean specifying whether to create the new all result.

<!-- @since:5.1.0 -->
### 14. Int

An Integer specifying type of result.

<!-- @since:5.1.0 -->
### 15. String\[]

A String List specifying the name of selected result.

<!-- @since:5.1.0 -->
### 16. Int

An Integer specifying the position of result.

<!-- @since:5.1.0 -->
### 17. String

A String specifying name of DB file.

<!-- @since:5.1.0 -->
### 18. String

A String specifying DB version.

<!-- @since:5.1.0 -->
### 19. String

A String specifying ID of method.

<!-- @since:5.1.0 -->
### 20. String

A String specifying ID of SPC.

<!-- @since:5.1.0 -->
### 21. Int

An Integer specifying RESVEC.

<!-- @since:5.1.0 -->
### 22. String

Name of the job.

<!-- @since:5.1.0 -->
### 23. Cursor\[]

A Cursor List specifying existing targets.

<!-- @since:5.1.0 -->
### 24. Cursor

A Cursor specifying an existing response condition.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
DYNAMIC _FREQ _ANALYSIS _RESPONSE _SOLVER(0:0, 0:0, True, [""], True, 1.0, 0:0, 0, 0.0,0.0,0.0, True,True, 0, [""],0,"","","","",0,"",[0:0], 0:0)
```
