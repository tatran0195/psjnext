---
title: "SplitElement()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Split Element

## Syntax

```psj
SplitElement(cursor[] taElems, cursor datum0, cursor datum1, int iMethod, bool bAutoExecute,
    bool AutoTransition, bool bCADProject, bool bMergeNodes)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target element cursor(\[11:Element ID])

<!-- @since:5.0.1 -->
### 2. Cursor

datum0 = 0:0

<!-- @since:5.0.1 -->
### 3. Cursor

datum1 = 0:0

<!-- @since:5.0.1 -->
### 4. Int

Method = 0

<!-- @since:5.0.1 -->
### 5. Bool

Auto execution bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

Auto transition bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Bool

CAD Projection bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 8. Bool

Merge Nodes bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SplitElement([11:1090], 0:0, 0:0, 0, 1, 0, 0, 1)
```
