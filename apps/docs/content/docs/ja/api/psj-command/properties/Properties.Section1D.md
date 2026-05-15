---
title: "Properties.Section1D()"
description: "Create 1D Property Sketcher Section"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Section1D"
macro _link: "[Property1DSection](../../macro/properties/Property1DSection)"
---

## Description

Create 1D Property Sketcher Section

## Syntax

```psj
Properties.Section1D(strName="", iSecType=0, iSecGenType=2, dSecGensizeA=0, dSecGensizeB=0, dSecGensizeH=0, dSecGensizeT1=0, dSecGensizeT2=0, dSecGensizeT3=0, bSecTapered=False, dSecGensizeATap=0, dSecGensizeBTap=0, dSecGensizeHTap=0, dSecGensizeT1Tap=0, dSecGensizeT2Tap=0, dSecGensizeT3Tap=0)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iSecType

- Specify the section type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSecGenType

- Specify the section general type.
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### dSecGensizeA

- Specify the section general size a.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSecGensizeB

- Specify the section general size b.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSecGensizeH

- Specify the section general size h.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSecGensizeT1

- Specify the section general size t1.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSecGensizeT2

- Specify the section general size t2.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSecGensizeT3

- Specify the section general size t3.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bSecTapered

- Specify the section tapered.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dSecGensizeATap

- Specify the section general size a tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSecGensizeBTap

- Specify the section general size tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSecGensizeHTap

- Specify the section general size h tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSecGensizeT1Tap

- Specify the section general size t1 tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSecGensizeT2Tap

- Specify the section general size t2 tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSecGensizeT3Tap

- Specify the section general size t3 tapered.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Section1D(strName="", iSecType=0, iSecGenType=2, dSecGensizeA=0, dSecGensizeB=0, dSecGensizeH=0, dSecGensizeT1=0, dSecGensizeT2=0, dSecGensizeT3=0, bSecTapered=False, dSecGensizeATap=0, dSecGensizeBTap=0, dSecGensizeHTap=0, dSecGensizeT1Tap=0, dSecGensizeT2Tap=0, dSecGensizeT3Tap=0)
```
