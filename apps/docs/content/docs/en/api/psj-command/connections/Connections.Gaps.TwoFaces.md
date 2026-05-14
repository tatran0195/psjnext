---
title: "Connections.Gaps.TwoFaces()"
description: "create gap connection"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Gaps > TwoFaces"
---

## Description

Create gap connection

## Syntax

```psj
Connections.Gaps.TwoFaces(crlMaster=[], crlSlave=[], iMethod=3, iOriMode=0, crCoord=None, strName="", dU0=DFLT _DBL, dF0=DFLT _DBL, dKa=DFLT _DBL, dKb=DFLT _DBL, dKt=DFLT _DBL, dMar=DFLT _DBL, dMu1=DFLT _DBL, dMu2=DFLT _DBL, dlOriVec=[], dTmax=DFLT _DBL, dTol=DFLT _DBL, dTrmin=DFLT _DBL, crEditCur=None)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMaster`

- The master.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlave`

- The slave.

<!-- @since:5.0.1 @type:Integer @optional @default:3 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOriMode`

- The ori mode.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dU0`

- The u0.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dF0`

- The f0.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dKa`

- The ka.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dKb`

- The kb.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dKt`

- The kt.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMar`

- The mar.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMu1`

- The mu1.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMu2`

- The mu2.

<!-- @since:5.0.1 @type:Double List @optional @default:[] -->
### `dlOriVec`

- The ori vector.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTmax`

- The tmax.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTrmin`

- The trmin.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEditCur`

- The edit cur.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Gaps.TwoFaces(crlMaster=[], crlSlave=[], iMethod=3, iOriMode=0, crCoord=None, strName="", dU0=DFLT _DBL, dF0=DFLT _DBL, dKa=DFLT _DBL, dKb=DFLT _DBL, dKt=DFLT _DBL, dMar=DFLT _DBL, dMu1=DFLT _DBL, dMu2=DFLT _DBL, dlOriVec=[], dTmax=DFLT _DBL, dTol=DFLT _DBL, dTrmin=DFLT _DBL, crEditCur=None)
```
