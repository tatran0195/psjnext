---
title: "FindHoles()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

FindHoles

## Syntax

```psj
FindHoles(Cursor[] part _list, Cursor[] edge _list, int min _length, double max _length, double findMethod)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Part List

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Edge List

<!-- @since:5.0.1 -->
### 3. Double

Edge Min Length

<!-- @since:5.0.1 -->
### 4. Double

Edge Max Length

<!-- @since:5.0.1 -->
### 5. Int

Find Method. All=0, Edges=1, Parts=2

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
FindHoles([3:1], [], 0, 12.345, 2)
```
