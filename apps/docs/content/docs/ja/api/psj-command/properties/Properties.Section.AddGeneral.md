---
title: "Properties.Section.AddGeneral()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Section > AddGeneral"
---

## Description

The general properties of a one-dimensional section are generated.

## Syntax

```psj
Properties.Section.AddGeneral(...)
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
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeA

- Specify the section general size a.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeB

- Specify the section general size b.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeH

- Specify the section general size h.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeT1

- Specify the section general size t1.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeT2

- Specify the section general size t2.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeT3

- Specify the section general size t3.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bBsecTapered

- Specify the bsec tapered.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeATap

- Specify the section general size a tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeBTap

- Specify the section general size b tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeHTap

- Specify the section general size h tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeT1Tap

- Specify the section general size t1 tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeT2Tap

- Specify the section general size t2 tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDsecGensizeT3Tap

- Specify the section general size t3 tapered.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iDirType

- Specify the y direction type.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Section.AddGeneral(strName="t1", 
                            iSecGenType=2, 
                            dDsecGensizeT1=0.001, 
                            iDirType=1)
```
