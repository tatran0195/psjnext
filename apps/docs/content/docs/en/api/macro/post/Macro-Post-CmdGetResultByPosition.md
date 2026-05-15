---
title: "CmdGetResultByPosition()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get result of specific position

## Syntax

```psj
CmdGetResultByPosition(Real x, Real y, Real z, Real Tolerance, bool DisplayPartOnly, bool UseMidNode)
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
### 5 bool

Restrict search target only displayed parts. true = 1,false = 0

<!-- @since:5.0.1 -->
### 6. bool

Use mid node data. true = 1,false = 0

## Return Code

- Result value of the searched point. The precision is set by Watch Data of Numeric settings in Preferences.
- "FAILED": If no position searched.

## Sample Code

```psj
CmdGetResultByPosition(10.001400, 8.884620, 1.818100, 0.010000, 0, 1)')
```
