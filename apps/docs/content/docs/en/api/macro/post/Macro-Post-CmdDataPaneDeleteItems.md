---
title: "CmdDataPaneDeleteItems()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Delete all the data in specified tab of Watch Data Window.

## Syntax

```psj
CmdDataPaneDeleteItems(int Tab, int[] items)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Tab ID.

<!-- @since:5.0.1 -->
### 2. int \[]

ID list of delete line.

## Return Code

Nothing.

## Sample Code

```psj
CmdDataPaneDeleteItems(1, [1,2,3,4])
```
