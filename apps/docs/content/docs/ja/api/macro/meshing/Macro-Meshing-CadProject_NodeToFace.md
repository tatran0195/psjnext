---
title: "CadProject _NodeToFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Project nodes in Meshed Face toward CAD Faces

## Syntax

```psj
CadProject _NodeToFace(cursor[] taCadFaces, cursor[] taNodes, int Direction, bool bImproveQuality,
    double tolerance, bool bNearest3Nodes)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target reference CAD Faces (15:RefFace ID)

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target nodes (\[10:Node IDs])

<!-- @since:5.0.1 -->
### 3. int

Direction Min=0, X=1, Y=2, Z=3, -X=4, -Y=5, -Z=6

<!-- @since:5.0.1 -->
### 4. Bool

Improve Quality check flag True = 1, False = 0

<!-- @since:5.1.0 -->
### 5. Double

Tolerance. If it set to -1, it means Auto setting (search based on mesh size).

<!-- @since:5.0.1 -->
### 7. Bool

Nearest Three Nodes check flag True = 1, False = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 5. Bool

Tolerance

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CadProject _NodeToFace([15:5], [10:377, 10:378, 10:390], 0, 0, 0.003, 1)
```
