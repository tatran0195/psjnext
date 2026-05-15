---
title: "CmdGeneralReportModal()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create report of modal analysis.

## Syntax

```psj
CmdGeneralReportModal(string file, bool ExportPPT, bool ExportImgFile, double startFreq, double endFreq)
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

<!-- @since:5.0.1 -->
### 4. double

Start Frequency.

<!-- @since:5.0.1 -->
### 5.double

End Frequency.

## Return Code

Nothing.

## Sample Code

```psj
CmdGeneralReportModal("C:/temp/gen _post.csv", 1, 1, 0, 10000)
```
