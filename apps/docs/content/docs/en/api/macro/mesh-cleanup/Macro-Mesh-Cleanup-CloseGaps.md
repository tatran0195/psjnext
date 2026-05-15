---
title: "CloseGaps()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Close small Gaps

## Syntax

```psj
CloseGaps(cursor[] taBodyCur, double dDistanceTol)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target part cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 2. Double

Close gap distance tolerance

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CloseGaps([3:1], 0.0001)
```
