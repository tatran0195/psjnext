---
title: "CmdMarkupSearchMultiPoints()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Search position and put note at the positions.

## Syntax

```psj
CmdMarkupSearchMultiPoints(vector[] positions, float dTolerance, bool bVisible )
```

## Inputs

<!-- @since:5.0.1 -->
### 1. vector\[]

List of search position \[x,y,z].

<!-- @since:5.0.1 -->
### 2. double

A Double specifying the tolerance to search the satisfying element. This argument will help to find the first nearest element with the input position.

<!-- @since:5.0.1 -->
### 3. bool

A _Boolean_ specifying the search mode.

- _True_: Only search element which is displayed on the screen
- _False_: Enable to search the hidden element

## Return Code

<!-- @since:5.0.1 -->
### 1. bool\[]

List of succeed(1) or failed(0).

## Sample Code

```psj
CmdMarkupSearchMultiPoints([[15.459201, 15.559538, 7.877257],[101.999998, 30.057640, 10.221649],[-0.827893, 23.017937, 9.930871],[66.764768, 24.950984, 7.866127]], 0.010000, 0)
>> [1,1,0,1]
```
