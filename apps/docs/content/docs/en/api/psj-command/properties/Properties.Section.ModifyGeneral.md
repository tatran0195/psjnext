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

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The section name.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crSection`

- The existing section to modify.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSecType`

- The section type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iGeneralType`

- The general type.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dA`

- A.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dB`

- The b.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dH`

- The h.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dT1`

- The t1.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dT2`

- The t2.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dT3`

- The t3.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
<!-- @since:5.1.0 @removed:5.1.0 -->
### `bTapered`

-A _Boolean_ specifying whether or not tapered.



<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDaTap`

- A tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDbTap`

- The b tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDhTap`

- The h tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDt1Tap`

- The t1 tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDt2Tap`

- The t2 tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDt3Tap`

- The t3 tapered.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iDirType`

- The direction type.

<!-- @since:5.0.1 @type:Boolean @removed:5.1.0 @optional @deprecated @default:False -->
### `bTapered`

- The tapered.

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
