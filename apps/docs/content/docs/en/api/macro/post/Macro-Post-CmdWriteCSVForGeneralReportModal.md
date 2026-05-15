---
title: "CmdWriteCSVForGeneralReportModal()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export Modal report into CSV file.

## Syntax

```psj
CmdWriteCSVForGeneralReportModal(string strPathFile, int ResultsInOnePage, bool bCheckusecurrentview, double dStartFrequency, double dEndFrequency)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

The name of export CSV file.

<!-- @since:5.1.0 -->
### 2. int

The number of images in one slide.

<!-- @since:5.1.0 -->
### 3. bool

Whether use current view point or not.

<!-- @since:5.1.0 -->
### 4. double

Start frequency.

<!-- @since:5.1.0 -->
### 5. double

End frequency.

## Return Code

Nothing.

## Sample Code

```psj
CmdWriteCSVForGeneralReportModal("C:/Users/TECHNO~1/AppData/Local/Temp/TechnoStar/00/gen _post.csv", 1, 0, 30000, 60000)
```
