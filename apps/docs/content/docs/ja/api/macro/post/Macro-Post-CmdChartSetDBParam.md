---
title: "CmdChartSetDBParam()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set dB Param.

## Syntax

```psj
CmdChartSetDBParam(int type, double refValue, double frontParam)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

dB Type. 1:dB, 2:SPL.

<!-- @since:5.0.1 -->
### 2. double

Reference Value

<!-- @since:5.0.1 -->
### 3. double

Front Parameter

## Return Code

Nothing.

## Sample Code

```psj
CmdChartSetDBParam(1, 1, 20)
```
