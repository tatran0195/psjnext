---
title: "Property1DSectionAdd _General()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create the general properties of 1D section.

## Syntax

```psj
Property1DSectionAdd _General(string strName, int iSecType, int iSecGenType, double dDsecGensizeA, double dDsecGensizeB, double dDsecGensizeH, double dDsecGensizeT1, double dDsecGensizeT2, double dDsecGensizeT3, bool bBsecTapered, double dDsecGensizeATap, double dDsecGensizeBTap, double dDsecGensizeHTap, double dDsecGensizeT1Tap, double dDsecGensizeT2Tap, double dDsecGensizeT3Tap, int iDirType)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

Property name

<!-- @since:5.1.0 -->
### 2. Int

Section type.

<!-- @since:5.1.0 -->
### 3. Int

Section general type.

<!-- @since:5.1.0 -->
### 4.Double

Section general size a.

<!-- @since:5.1.0 -->
### 5.Double

Section general size b.

<!-- @since:5.1.0 -->
### 6.Double

Section general size h.

<!-- @since:5.1.0 -->
### 7.Double

Section general size t1.

<!-- @since:5.1.0 -->
### 8.Double

Section general size t2.

<!-- @since:5.1.0 -->
### 9.Double

Section general size t3.

<!-- @since:5.1.0 -->
### 10.Bool

The bsec tapered.

<!-- @since:5.1.0 -->
### 11.Double

Section general size a tapered.

<!-- @since:5.1.0 -->
### 12.Double

Section general size b tapered.

<!-- @since:5.1.0 -->
### 13.Double

Section general size h tapered.

<!-- @since:5.1.0 -->
### 14.Double

Section general size t1 tapered.

<!-- @since:5.1.0 -->
### 15.Double

Section general size t2 tapered.

<!-- @since:5.1.0 -->
### 16.Double

Section general size t3 tapered.

<!-- @since:5.1.0 -->
### 17.Int

Y direction type.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Property1DSectionAdd _General("NewSection", 0, 2, 0, 0, 0, 0.001, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
```
