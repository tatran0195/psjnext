---
title: "Connections.Contacts.NXNastran.ContactShareFace()"
description: "Create Contact NXNastran Contact Share Face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > NXNastran > ContactShareFace"
---

## Description

Create Contact NXNastran Contact Share Face

## Syntax

```psj
Connections.Contacts.NXNastran.ContactShareFace(crlShareFace=[], strName="ContactNXNastran _1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=3, crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlShareFace`

- The share face.

<!-- @since:5.0.1 @type:String @optional @default:"ContactNXNastran _1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactType`

- The contact type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactAlg`

- The contact algorithm.

<!-- @since:5.0.1 @type:Double @optional @default:10 -->
### `dNorPenFactor`

- The nor pen factor.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dTanPenFactor`

- The tan pen factor.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dForceConTol`

- The force con tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:10 -->
### `dMaxForceIter`

- The maximum force iterator.

<!-- @since:5.0.1 @type:Double @optional @default:20 -->
### `dMaxStaIter`

- The maximum sta iterator.

<!-- @since:5.0.1 @type:Double @optional @default:0.02 -->
### `dChangeNum`

- The change number.

<!-- @since:5.0.1 @type:Double @optional @default:100 -->
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

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iEvaluPts`

- The evalu pts.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMinSearDist`

- The minimum sear dist.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
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

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iColor`

- The color.

<!-- @since:5.0.1 @type:Integer @optional @default:3 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.NXNastran.ContactShareFace(crlShareFace=[], strName="ContactNXNastran _1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=3, crEdit=None)
```
