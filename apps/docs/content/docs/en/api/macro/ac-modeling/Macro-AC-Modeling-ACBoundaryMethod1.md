---
title: "ACBoundaryMethod1()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create Acoustic Boundary.

## Syntax

```psj
ACBoundaryMethod1(cursor[] crlParts, bool bIsMergePart, bool bIsRenumber)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. cursor\[]

A list of body entities (such as parts or shapes) that you want to process using the boundary method.

<!-- @since:5.1.0 -->
### 2. bool

Whether to merge the body entities into one. If True, the selected parts will be merged together.

<!-- @since:5.1.0 -->
### 3. bool

Whether to renumber the nodes and elements. If True, the macro will assign new numbers to nodes/elements to avoid duplicates or conflicts.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ACBoundaryMethod1([3:1, 3:2], 1, 1)
```
