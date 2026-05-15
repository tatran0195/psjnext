---
title: "DeleteElement()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Delete Element

## Syntax

```psj
DeleteElement(cursor[] elemList, bool bKeepShareElem)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target element cursor(\[11:Element ID])

<!-- @since:5.0.1 -->
### 2. Bool

Keep Share Element bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
DeleteElement([11:1112], 0)
```
