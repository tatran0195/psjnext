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

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSecType`

- The section type.

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iSecGenType`

- The section general type.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeA`

- The section general size a.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeB`

- The section general size b.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeH`

- The section general size h.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeT1`

- The section general size t1.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeT2`

- The section general size t2.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeT3`

- The section general size t3.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSecTapered`

- The section tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeATap`

- The section general size a tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeBTap`

- The section general size tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeHTap`

- The section general size h tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeT1Tap`

- The section general size t1 tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeT2Tap`

- The section general size t2 tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSecGensizeT3Tap`

- The section general size t3 tapered.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Section1D(strName="", iSecType=0, iSecGenType=2, dSecGensizeA=0, dSecGensizeB=0, dSecGensizeH=0, dSecGensizeT1=0, dSecGensizeT2=0, dSecGensizeT3=0, bSecTapered=False, dSecGensizeATap=0, dSecGensizeBTap=0, dSecGensizeHTap=0, dSecGensizeT1Tap=0, dSecGensizeT2Tap=0, dSecGensizeT3Tap=0)
```
