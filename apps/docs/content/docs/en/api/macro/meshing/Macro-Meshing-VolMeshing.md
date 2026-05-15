---
title: "VolMeshing()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Solid Meshing

## Syntax

```psj
VolMeshing(cursor[] body, volMeshParam param, bool use _mesh _color, color color)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Body List

<!-- @since:5.0.1 -->
### 2. VolMeshParam::bool

Tet10 0=No,1=Yes

<!-- @since:5.0.1 -->
### 3. VolMeshParam::double

Grading Factor

<!-- @since:5.0.1 -->
### 4. VolMeshParam::bool

Gravity Centre 0=No,1=Yes

<!-- @since:5.0.1 -->
### 5. VolMeshParam::double

Stretch Limit

<!-- @since:5.0.1 -->
### 6. VolMeshParam::int

Quality 0=Fastest,1=Standard,2=Optimize

<!-- @since:5.0.1 -->
### 7. VolMeshParam::int

Memory 0=Standard,1=LowMemory

<!-- @since:5.0.1 -->
### 8. VolMeshParam::int

Region 0=AllRegion,1=MainRegion

<!-- @since:5.0.1 -->
### 9. VolMeshParam::bool

Internal Nodes 0=No,1=Yes

<!-- @since:5.0.1 -->
### 10. VolMeshParam::bool

Safe Mode 0=No,1=Yes

<!-- @since:5.0.1 -->
### 11. VolMeshParam::int

Parallel Number

<!-- @since:5.0.1 -->
### 12. VolMeshParam::bool

Surface Nodes 0=No,1=Yes

<!-- @since:5.0.1 -->
### 13. VolMeshParam::bool

Edge Nodes 0=No,1=Yes

<!-- @since:5.0.1 -->
### 14. VolMeshParam::bool

Preservation 0=No,1=Yes

<!-- @since:5.0.1 -->
### 15. VolMeshParam::bool

Internal Mesh Only 0=No,1=Yes

<!-- @since:5.0.1 -->
### 16. Bool

Use Mesh Color 0=No,1=Yes

<!-- @since:5.0.1 -->
### 17. Color

Mesh Color

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
VolMeshing([3:1], {1, 1.05, 0, 0.1, 1, 0, 1, 1, 0, 4, 1, 1, 1, 0}, 0, 65280)
```
