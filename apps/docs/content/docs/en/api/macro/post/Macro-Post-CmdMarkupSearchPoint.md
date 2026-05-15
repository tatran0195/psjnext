---
title: "CmdMarkupSearchPoint()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Search element from position

## Syntax

```psj
CmdMarkupSearchPoint(Real x, Real y, Real z, Real Tolerance, bool DisplayPartOnly)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Real

X position

<!-- @since:5.0.1 -->
### 2. Real

Y position

<!-- @since:5.0.1 -->
### 3. Real

Z potision

<!-- @since:5.0.1 -->
### 4. Real

Tolerance of search surface.

<!-- @since:5.0.1 -->
### 5. bool

Restrict search target only displayed parts. true = 1,false = 0

## Return Code

- "1": If element found.
- "FALSE": If no element found.

## Sample Code

```psj
CmdMarkupSearchPoint(29.300000, 27.000000, 7.186000, 0.010000, 0)
```
