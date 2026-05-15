---
title: "SetHidingElementFactor()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set Optimized Shape value and result that is threshold for being a hidden element.

## Syntax

```psj
SetHiddingElementFactor(float OptimizedShape, string ResultName)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. float

Specify Optimized Shape value to hide element.

<!-- @since:5.1.0 -->
### 2. string

Specify result to use as hiding elemet source. "NodalDensityRatio" or "DensityRatio".

## Return Code

Nothing.

## Sample Code

```psj
SetHidingElementFactor(0.28, "NodalDensityRatio")
```
