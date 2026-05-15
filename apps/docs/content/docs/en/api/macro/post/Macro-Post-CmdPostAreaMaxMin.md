---
title: "CmdPostAreaMaxMin()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Detect the maximum and minimum values of nodes within a specified range.

## Syntax

```psj
CmdPostAreaMaxMin(cursor[] crlTargets, bool bCheckMax, bool bCheckMin, bool bSave)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor\[]

A List of Cursor specifying the selected nodes to detect max/min value.

<!-- @since:5.1.0 -->
### 2. bool

A Boolean specifying whether to enable/disable detecting and displaying the maximum value.

<!-- @since:5.1.0 -->
### 3. bool

A Boolean specifying whether to enable/disable detecting and displaying the minimum value.

<!-- @since:5.1.0 -->
### 4. bool

A Boolean specifying whether to save the detected max/min result into AreaMax/Min tab of the Watch Data Window.

## Return Code

Nothing.

## Sample Code

```psj
CmdPostAreaMaxMin([10:7, 10:10, 10:3, 10:4, 10:11, 10:67, 10:72, 10:92], 1, 1)
```
