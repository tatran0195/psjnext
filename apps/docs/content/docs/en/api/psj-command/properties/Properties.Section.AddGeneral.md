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

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSecType`

- The section type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSecGenType`

- The section general type.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeA`

- The section general size a.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeB`

- The section general size b.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeH`

- The section general size h.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeT1`

- The section general size t1.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeT2`

- The section general size t2.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeT3`

- The section general size t3.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bBsecTapered`

- The bsec tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeATap`

- The section general size a tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeBTap`

- The section general size b tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeHTap`

- The section general size h tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeT1Tap`

- The section general size t1 tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeT2Tap`

- The section general size t2 tapered.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dDsecGensizeT3Tap`

- The section general size t3 tapered.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iDirType`

- The y direction type.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Section.AddGeneral(strName="t1", 
                            iSecGenType=2, 
                            dDsecGensizeT1=0.001, 
                            iDirType=1)
```
