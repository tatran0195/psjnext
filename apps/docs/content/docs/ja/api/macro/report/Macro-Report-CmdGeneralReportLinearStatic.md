---
title: "CmdGeneralReportLinearStatic()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Search for parts (components) whose displayed static analysis results are outside the result thresholds set for parts and materials, captures images and automatically pastes them into Microsoft Office PowerPoint.

## Syntax

```psj
CmdGeneralReportLinearStatic(int CalculateValue, int EvaluationValue, int[] listPartInformation, bool UseCurrentView, bool ExportPPT, bool ExportImage, string ImgFilePath)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Int

An Integer specifying the evaluation value.

<!-- @since:5.1.0 -->
### 2. Int

An Integer specifying the evaluation expression.

<!-- @since:5.1.0 -->
### 3. Int\[]

A List of _[GENERAL\_REPORT\_LINEAR\_STATIC\_DATA](../../data-type/psj-command/parameter-types/GENERAL _REPORT _LINEAR _STATIC _DATA)_ specifying the attribute of components.

<!-- @since:5.1.0 -->
### 4. Bool

A Boolean specifying whether to use the current view as perspective.

<!-- @since:5.1.0 -->
### 5. Bool

A Boolean specifying whether to export the result image to PowerPoint.

<!-- @since:5.1.0 -->
### 6. Bool

A Boolean specifying whether to save the result image to file.

<!-- @since:5.1.0 -->
### 7. String

A String specifying the path of image file to be saved in the specified format.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
CmdGeneralReportLinearStatic(0, 0, [], False, True, False, "")
```
