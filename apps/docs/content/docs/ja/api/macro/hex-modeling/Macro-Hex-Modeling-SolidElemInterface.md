---
title: "SolidElemInterface"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Pyramid elements as interface elements.

## Syntax

```psj
SolidElemInterface(cursor[] taFaces, bool Flip, cursor[] taElements)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Face Cursor (\[6:Face ID])

<!-- @since:5.0.1 -->
### 2. Bool

Flip Normal false : 0, true : 1

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Elements Cursor (\[11:Elements ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SolidElemInterface([6:22], 0, [11:324])
```
