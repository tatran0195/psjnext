---
title: "GeometryDeform()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Deform face

## Syntax

```psj
GeometryDeform(cursor[] taFaceSrcObverse, cursor[] taFaceDstReverse, cursor[] taFaceSrcReverse, cursor[] crlFaceDstObverse, cursor[] crlFaceFixed, double dDistEffect)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

A List of Cursor specifying the face source obverse.

<!-- @since:5.0.1 -->
### 2. Cursor\[]

A List of Cursor specifying the face dst reverse.

<!-- @since:5.0.1 -->
### 3. Cursor\[]

A List of Cursor specifying the face source reverse.

<!-- @since:5.0.1 -->
### 4. Cursor\[]

A List of Cursor specifying the face dst obverse.

<!-- @since:5.0.1 -->
### 5. Cursor\[]

A List of Cursor specifying the face fixed.

<!-- @since:5.0.1 -->
### 6. double

A Double specifying the dist effect.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
GeometryDeform([6:26], [6:21], [6:22], [6:24], [], 0.02)
```
