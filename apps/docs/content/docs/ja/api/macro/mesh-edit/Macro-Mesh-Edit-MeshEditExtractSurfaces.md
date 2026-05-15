---
title: "MeshEditExtractSurfaces()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Extract Surfaces

## Syntax

```psj
MeshEditExtractSurfaces(Cursor[] Face Cursor, double Angle, string New Body Name)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target Faces for Extraction

<!-- @since:5.0.1 -->
### 2. Double

Extracting Angle for Adjacent Faces

<!-- @since:5.0.1 -->
### 3. String

Extracted Body Name

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MeshEditExtractSurfaces([6:22, 6:23, 6:26], 1.0472, "New Body")
```
