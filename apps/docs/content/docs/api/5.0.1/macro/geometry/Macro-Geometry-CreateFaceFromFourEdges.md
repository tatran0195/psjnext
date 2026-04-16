---
id: CreateFaceFromFourEdges
title: CreateFaceFromFourEdges()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create Face From Four Edges

## Syntax

```psj
CreateFaceFromFourEdges(cursor[] vcrEdges)
```

## Inputs

### `1. Cursor[]`

Target edge cursor([5:Edge ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateFaceFromFourEdges([5:35, 5:38, 5:37, 5:32])
```
