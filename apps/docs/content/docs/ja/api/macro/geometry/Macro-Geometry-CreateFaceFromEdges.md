---
title: "CreateFaceFromEdges()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Face From Edges

## Syntax

```psj
CreateFaceFromEdges(cursor[] edgeList, cursor[] part, cursor[] nodeList, bool sharedFace,
    bool smoothFace, bool createPart, bool improved, bool barsOnly, bool onlyOnePart, bool useMidNodes)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target edge cursor(\[5:Edge ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target part cursor(\[3:Part ID])

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target node cursor(\[10:Node ID])

<!-- @since:5.0.1 -->
### 4. Bool

Share face bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Bool

Smooth face bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 6. Bool

New part bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 7. Bool

Improved bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 8. Bool

Bars bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 9. Bool

Only one part bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 10. Bool

use mid nodes bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateFaceFromEdges([5:57, 5:38], [3:3], [], 0, 0, 1, 0, 0, 0, 0)
```
