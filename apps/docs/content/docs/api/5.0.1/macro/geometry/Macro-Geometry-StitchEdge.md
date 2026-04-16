---
id: StitchEdge
title: StitchEdge()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Stitch Edge

## Syntax

```psj
StitchEdge(double dTolerance, bool keepSlave, cursor[] taMaster, cursor[] taSlave)
```

## Inputs

### `1. Double`

Tolerance for stitch (m)

### `2. Bool`

Whether keep slave or not True = 1, False = 0

### `3. Cursor[]`

Master edge for stitch -> edge cursor([5:Edge ID])

### `4. Cursor[]`

Slave edge for stitch -> edge cursor([5:Edge ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
StitchEdge(0.0003, 1, [5:18], [5:57])
```
