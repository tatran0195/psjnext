---
title: "Properties.ThicknessDistribution()"
description: "Properties view Thickness Distribution"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > ThicknessDistribution"
---

## Description

Properties view Thickness Distribution

## Syntax

```psj
Properties.ThicknessDistribution(dMax=1, dMin=0, iByEach=0, dlThicknessValueSet=[])
```

## Inputs

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dMax`

- The maximum.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMin`

- The minimum.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iByEach`

- The by each.

<!-- @since:5.0.1 @type:Double List @optional @default:[] -->
### `dlThicknessValueSet`

- The thickness value set.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.ThicknessDistribution(dMax=1, dMin=0, iByEach=0, dlThicknessValueSet=[])
```
