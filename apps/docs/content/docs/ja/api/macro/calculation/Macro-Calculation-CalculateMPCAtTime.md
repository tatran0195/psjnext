---
title: "CalculateMPCAtTime()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Display MPC result of specific time in Model Participation Factor dialog.

## Syntax

```psj
CalculateMPCAtTime(cursor crResponse, double dTime)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor

- A Cursor specifying the response to calculate MPC.

<!-- @since:5.1.0 -->
### 2. double

- A Double specifying the time to calculate MPC.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CalculateMPCAtTime(0:0, 0.0)
```
