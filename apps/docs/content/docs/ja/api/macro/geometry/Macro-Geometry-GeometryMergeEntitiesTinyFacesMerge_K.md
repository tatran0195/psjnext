---
title: "GeometryMergeEntitiesTinyFacesMerge _K()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Merge tiny faces either by extending the user selection or using only the selected faces.

## Syntax

```psj
GeometryMergeEntitiesTinyFacesMerge _K(string method, cursor[] targets, double minFace [3:1], 0, 0.001, 30, 0, 1, [], [])
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

The method use to merge. Possible values are _AUTO_, _SELECT_, _MERGE_, _RESTORE_.

<!-- @since:5.1.0 -->
### 2. Cursor\[]

The parts or faces to be merged.

<!-- @since:5.1.0 -->
### 3. Double

The minimum face width in meter. This argument is used when _strMethod_ has the value _AUTO_ or _SELECT_.

<!-- @since:5.1.0 -->
### 4. Double

The maximum face width in meter. This argument is used when _strMethod_ has the value _AUTO_ or _SELECT_.

<!-- @since:5.1.0 -->
### 5. Double

The angle between faces in degree. This argument is used when _strMethod_ has the value _AUTO_ or _MERGE_.

<!-- @since:5.1.0 -->
### 6. Bool

Whether to refer to the local setting or not.

<!-- @since:5.1.0 -->
### 7. Bool

Whether or not create a reference part.

<!-- @since:5.1.0 -->
### 8. cursor\[]

The reference parts.

<!-- @since:5.1.0 -->
### 9. cursor\[]

The reference edge.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
GeometryMergeEntitiesTinyFacesMerge _K("AUTO", [3:1], 0, 0.001, 30, 0, 1, [], [])
```
