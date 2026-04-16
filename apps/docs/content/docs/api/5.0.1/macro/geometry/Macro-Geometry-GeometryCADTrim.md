---
id: GeometryCADTrim
title: GeometryCADTrim()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

CAD Trim

## Syntax

```psj
GeometryCADTrim(cursor[] listFace, cursor[] listPart, double trimSize, double trimAngle)
```

## Inputs

### `1. Cursor[]`

Target faces for CAD Trim -> Face cursor([6:Face ID])

### `2. Cursor[]`

Target parts for CAD Trim -> Part cursor([3:Part ID])

### `3. Double`

Trim size (m)

### `4. Double`

Trim angle (radian)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
GeometryGeometryCADTrim([6:26], [3:1], 0.005, 0.261799)
```
