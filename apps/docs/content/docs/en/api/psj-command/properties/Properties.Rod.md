---
title: "Properties.Rod()"
description: "create 1D rod property"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Rod"
macro _link: "[Property1DRod](../../macro/properties/Property1DRod)"
---

## Description

Create 1D rod property

## Syntax

```psj
Properties.Rod(strName="", iPID=1, crSection=None, crMat=None, dArea=DFLT _DBL, dTorConst=DFLT _DBL, dTorStressCoeff=DFLT _DBL, dNSM=DFLT _DBL, iLocalLengthUnit=0, iLocalMassUnit=0, crlTargets=[], crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iPID`

- The ID.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crSection`

- The section.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMat`

- The material.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dArea`

- The area.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTorConst`

- The tor const.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTorStressCoeff`

- The tor stress coeff.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNSM`

- The n s m.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLocalLengthUnit`

- The local length unit.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLocalMassUnit`

- The local mass unit.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Rod(strName="", iPID=1, crSection=None, crMat=None, dArea=DFLT _DBL, dTorConst=DFLT _DBL, dTorStressCoeff=DFLT _DBL, dNSM=DFLT _DBL, iLocalLengthUnit=0, iLocalMassUnit=0, crlTargets=[], crEdit=None)
```
