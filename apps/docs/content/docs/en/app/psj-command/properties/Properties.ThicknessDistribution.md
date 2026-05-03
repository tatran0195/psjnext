---
title: "Properties.ThicknessDistribution()"
description: "Properties view Thickness Distribution"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > ThicknessDistribution"
---

## Description

Properties view Thickness Distribution

## Syntax

```psj
Properties.ThicknessDistribution(dMax=1, dMin=0, iByEach=0, dlThicknessValueSet=[])
```

## Inputs

### `dMax` @type(Double) @default(1)

- The maximum.

### `dMin` @type(Double) @default(0)

- The minimum.

### `iByEach` @type(Integer) @default(0)

- The by each.

### `dlThicknessValueSet` @type(Double List) @default(\[])

- The thickness value set.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.ThicknessDistribution(dMax=1, dMin=0, iByEach=0, dlThicknessValueSet=[])
```
