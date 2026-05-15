---
title: "MeshEditMorphingRibThickness()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Change rib thickness by moveing nodes.

## Syntax

```psj
MeshEditMorphingRibThickness(Cursor[] taFaceMove, Cursor[] taFaceFixed, double move, double distStrong, double distWeak)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

A Cursor List specifying the face move.

<!-- @since:5.0.1 -->
### 2. Cursor\[]

A Cursor List specifying the face fixed.

<!-- @since:5.0.1 -->
### 3. Double

A Double specifying the move.

<!-- @since:5.0.1 -->
### 4. Double

A Double specifying the dist strong.

<!-- @since:5.0.1 -->
### 5. Double

A Double specifying the dist weak.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeshEditMorphingRibThickness([6:26, 6:25], [], 0.003, 0.01, 0.02)
```
