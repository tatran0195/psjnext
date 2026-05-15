---
title: "TranslateBody()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Translate Body

## Syntax

```psj
TranslateBody(cursor[] taBody, double[] tavdTranslate, cursor crCoord, bool bCreateNewBody,
    bool bcopyLBC, int iCopyCount)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target part cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 2. Double\[]

Translation vector list

<!-- @since:5.0.1 -->
### 3. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

<!-- @since:5.0.1 -->
### 4. Bool

Create New Part bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Bool

LBC Copy bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Int

Copy count

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
TranslateBody([3:1], [[0.01, 0, 0]], 0:0, 1, 0, 1)
```
