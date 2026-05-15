---
title: "Remove _Rib _Boss()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Remove Rib Boss

## Syntax

```psj
Remove _Rib _Boss(Curor[] Face, double Gradation, int iContinuity)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Face cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 2. Double

Gradation value

<!-- @since:5.0.1 -->
### 3. Int

Connection Continuity: 0,1,2

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Remove _Rib _Boss([624], 1, 1)
```
