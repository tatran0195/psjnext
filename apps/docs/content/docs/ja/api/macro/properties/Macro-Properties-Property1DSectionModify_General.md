---
title: "Property1DSectionModify _General()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

## Syntax

```psj
Property1DSectionModify _General(string strName, cursor crSection,int iSecType, int iGeneralType, double dA, double dB, double dH, double dT1, double dT2, double dT3, bool bTapered, double dDaTap, double dDbTap, double dDhTap, double dDt1Tap, double dDt2Tap, double dDt3Tap, int iDirType)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

Property name

<!-- @since:5.1.0 -->
### 2.cursor

Existing section to modify.

<!-- @since:5.1.0 -->
### 3.Int

Section type.

<!-- @since:5.1.0 -->
### 4.Int

General type.

<!-- @since:5.1.0 -->
### 5.Double

a.

<!-- @since:5.1.0 -->
### 6.Double

b.

<!-- @since:5.1.0 -->
### 7.Double

h.

<!-- @since:5.1.0 -->
### 8.Double

t1.

<!-- @since:5.1.0 -->
### 9.Double

t2.

<!-- @since:5.1.0 -->
### 10.Double

t3.

<!-- @since:5.1.0 -->
### 11.Bool

Tapered or not.

<!-- @since:5.1.0 -->
### 12.Double

a tapered.

<!-- @since:5.1.0 -->
### 13.Double

b tapered.

<!-- @since:5.1.0 -->
### 14.Double

h tapered.

<!-- @since:5.1.0 -->
### 15.Double

t1 tapered.

<!-- @since:5.1.0 -->
### 16.Double

t2 tapered.

<!-- @since:5.1.0 -->
### 17.Double

t3 tapered.

<!-- @since:5.1.0 -->
### 18.Int

Direction type.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Property1DSectionModify _General("Modified", 93:1, 0, 0, 0, 0.002, 0.003, 0.001, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
```
