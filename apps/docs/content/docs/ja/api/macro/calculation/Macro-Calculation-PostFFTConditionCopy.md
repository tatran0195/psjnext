---
title: "PostFFTConditionCopy()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Copy a FFT analysis.

## Syntax

```psj
PostFFTConditionCopy(cursor crTarget)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor

- A Cursor specifying the copy source.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PostFFTConditionCopy(220:1)
```
