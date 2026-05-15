---
title: "CmdGeneralReportLinearStatic()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create report of linear static analysis.

## Syntax

```psj
CmdGeneralReportLinearStatic(string file, bool ExportPPT, bool ExportImgFile)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

CSV file path for setting file.

<!-- @since:5.0.1 -->
### 2.bool

Export PPT flag.

<!-- @since:5.0.1 -->
### 3.bool

Export Image File flag.

## Return Code

Nothing.

## Sample Code

```psj
CmdGeneralReportLinearStatic("C:/temp/gen _pre.csv", 1, 0)
```
