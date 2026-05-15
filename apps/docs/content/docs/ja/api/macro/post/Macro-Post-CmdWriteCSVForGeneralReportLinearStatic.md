---
title: "CmdWriteCSVForGeneralReportLinearStatic()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export Linear Static report into CSV file.

## Syntax

```psj
CmdWriteCSVForGeneralReportLinearStatic(string strCSVFile, string strCalculateValue, string strEvaluationValue, bool bCheckusecurrentview, 
string strfilePath, string strfileName, string strfileExt, string[] listGridData)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

The name of export CSV file.

<!-- @since:5.1.0 -->
### 2. string

Calculation value.

<!-- @since:5.1.0 -->
### 3. string

Evaluation value.

<!-- @since:5.1.0 -->
### 4. bool

Flag whether use current view.

<!-- @since:5.1.0 -->

#### 5. string

Folder path to export images.

<!-- @since:5.1.0 -->

#### 6. string

File name of export images.

<!-- @since:5.1.0 -->

#### 7. string

File extension of export images.

<!-- @since:5.1.0 -->

#### 8. string\[]

Grid information.

## Return Code

Nothing.

## Sample Code

```psj
JPT.Exec('CmdWriteCSVForGeneralReportLinearStatic("C:/Users/TECHNO~1/AppData/Local/Temp/TechnoStar/01/gen _pre.csv", "Mises", "A/B", 0, "", "", "", [["All", "-", "-", "0.000000"]])')
```
