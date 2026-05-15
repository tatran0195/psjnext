---
title: "SetDefaultAutoSaveOption()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set auto save options.

## Syntax

```psj
SetDefaultAutoSaveOption(int Flag, int Interval, int NumberOfSaveFiles)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

Enable auto save.

- 0: OFF
- 1: ON

<!-- @since:5.1.0 -->
### 2. int

Interval of auto save (minutes).

<!-- @since:5.1.0 -->
### 3. int

Number of save files.

## Return Code

No return code.

## Sample Code

```psj
SetDefaultAutoSaveOption(1, 15, 2)
```
