---
id: MergeFace
title: MergeFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Merge Face

## Syntax

```psj
MergeFace(Cursor[] face,bool merge_edge)
```

## Inputs

### `1. Cursor[]`

Face List

### `2. Bool`

Auto Merge Edge 1=Yes,0=No

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MergeFace([6:24, 6:26], 0)
```
