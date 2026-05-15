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

<!-- @since:5.0.1 @optional -->
### dMax

- Specify the maximum.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dMin

- Specify the minimum.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iByEach

- Specify the by each.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dlThicknessValueSet

- Specify the thickness value set.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.ThicknessDistribution(dMax=1, dMin=0, iByEach=0, dlThicknessValueSet=[])
```
