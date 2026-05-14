---
title: "Connections.Contacts.NXNastran.ContactTable()"
description: "Create Contact NXNastran Contact Table"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > NXNastran > ContactTable"
---

## Description

Create Contact NXNastran Contact Table

## Syntax

```psj
Connections.Contacts.NXNastran.ContactTable(strName="", iType=0, iAlg=0, dNorPenFactor=0, dTanPenFactor=0, dForceConTol=0, dMaxForceIter=0, dMaxStaIter=0, dChangeNum=0, dMinContactPer=0, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=0, dMinSearDist=0, dMaxSearDist=0, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, crplTargetPair=[], crEdit=None, iColor=0, iMethod=1)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAlg`

- The algorithm.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dNorPenFactor`

- The nor pen factor.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dTanPenFactor`

- The tan pen factor.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dForceConTol`

- The force con tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMaxForceIter`

- The maximum force iterator.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMaxStaIter`

- The maximum sta iterator.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dChangeNum`

- The change number.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMinContactPer`

- The minimum contact per.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iShellThickness`

- The shell thickness.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactStatus`

- The contact status.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iInitGapPenetra`

- The initial gap penetra.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iRegionRefine`

- The region refine.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEvaluPts`

- The evalu pts.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMinSearDist`

- The minimum sear dist.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMaxSearDist`

- The maximum sear dist.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dFricCoef`

- The fric coefficient .

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSearchDist`

- The search dist.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPenatlyFactor`

- The penatly factor.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iShellOffset`

- The shell offset.

<!-- @since:5.0.1 @type:Cursor Pair List @optional @default:[] -->
### `crplTargetPair`

- The target pair.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iColor`

- The color.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iMethod`

- The method.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.NXNastran.ContactTable(strName="", iType=0, iAlg=0, dNorPenFactor=0, dTanPenFactor=0, dForceConTol=0, dMaxForceIter=0, dMaxStaIter=0, dChangeNum=0, dMinContactPer=0, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=0, dMinSearDist=0, dMaxSearDist=0, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, crplTargetPair=[], crEdit=None, iColor=0, iMethod=1)
```
