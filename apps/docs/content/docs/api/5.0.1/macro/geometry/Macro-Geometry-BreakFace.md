---
id: BreakFace
title: BreakFace()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Break selected face

## Syntax

```psj
BreakFace(Cursor[] FACE Cursor)
```

## Inputs

### `1. Cursor[]`

Target face cursor([6:Face ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
BreakFace([6:64, 6:537, 6:531, 6:534])
```
