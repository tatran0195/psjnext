---
id: ImprintCloseLineS
title: ImprintCloseLineS()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create imprint Closed line

## Syntax

```psj
ImprintCloseLineS(double[] entitiesCoord, cursor[] crFace, bool bBrFace)
```

## Inputs

### `1. Double[]`

Point coordinate

### `2. Cursor[]`

Target face cursor([6:Face ID])

### `3. Bool`

Break face bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImprintCloseLineS([[0, 0, 0], [0, 0.002222222222222222, 0.001111111111111111],
    [0, 0.001111111111111111, 0.002222222222222222]], [6:23], 1)
```
