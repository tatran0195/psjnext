---
title: "Properties.Section.ModifyGeneral()"
description: "Modify the existing general section for 1D Property."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Section > ModifyGeneral"
macro _link: "Property1DSectionModify _General"
---

## Description

Modify the existing general section for 1D Property.

## Syntax

```psj
Properties.Section.ModifyGeneral(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the section name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### crSection

- Specify the existing section to modify.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iSecType

- Specify the section type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iGeneralType

- Specify the general type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dA

- Specify the a.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dB

- Specify the b.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dH

- Specify the h.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dT1

- Specify the t1.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dT2

- Specify the t2.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dT3

- Specify the t3.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 @removed:5.1.0 -->
### bTapered

-A _Boolean_ specifying whether or not tapered.

- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dDaTap

- Specify the a tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDbTap

- Specify the b tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDhTap

- Specify the h tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDt1Tap

- Specify the t1 tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDt2Tap

- Specify the t2 tapered.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDt3Tap

- Specify the t3 tapered.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iDirType

- Specify direction type.
- The default value is 0.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### bTapered

- Specify the tapered.
- The default value is False.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {5-9}
Properties.Section.AddGeneral(  strName="t1", 
                                iSecGenType=2, 
                                dDsecGensizeT1=0.001, 
                                iDirType=1)
Properties.Section.ModifyGeneral(strName="t1", 
                                crSection=SectionGeneral(1), 
                                iGeneralType=2, 
                                dT1=0.001, 
                                iDirType=3)
```
