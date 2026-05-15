---
title: "CmdMarkupSearchElementsFromMultiPoints()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Search nearest elements from indicated positions and put notes at the elementss.

## Syntax

```psj
CmdMarkupSearchElementsFromMultiPoints(vector[] positions)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. vector\[]

List of search position \[x,y,z].

## Return Code

<!-- @since:5.1.0 -->
### 1. bool \[]

List of succeed(1) or failed(0).

## Sample Code

```psj
CmdMarkupSearchElementsFromMultiPoints([0.000000, 0.000000, 0.000000],[0.000000, 5.000000, 0.000000],[10.000000, 5.000000, 0.000000],[10.000000, 10.000000, 5.000000])
>> [1,1,1,1]
```
