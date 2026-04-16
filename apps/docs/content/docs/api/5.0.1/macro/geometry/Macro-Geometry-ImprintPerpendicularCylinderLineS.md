---
id: ImprintPerpendicularCylinderLineS
title: ImprintPerpendicularCylinderLineS()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Create imprint PerpendicularCylinder line

## Syntax

```psj
ImprintPerpendicularCylinderLineS(cursor[] crNode, cursor[] crFace, int iMethod, double dLength, bool bOpSide, bool bBrFace)
```

## Inputs

### `1. Cursor[]`

Target node cursor([10:Node ID])

### `2. Cursor[]`

Target face cursor([6:Face ID])

### `3. Int`

Imprint method

- 0: Center Angle
- 1: ArcLength

### `4. Double`

Length/ Angle offset

### `5. Bool`

Opposite side bool flag True = 1, False = 0

### `6. Bool`

Break face bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ImprintPerpendicularCylinderLineS([10:283, 10:281], [6:5], 0, 3, 0, 1)
```
