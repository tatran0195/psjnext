---
title: "Connections.Contacts.NXNastranGeneral()"
description: "Define contact settings for the NX solver."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > NXNastranGeneral"
macro _link: "[ContactNXNastran](../../macro/connections/ContactNXNastran)"
---

## Description

Define contact settings for the NX solver.

## Syntax

```psj
Connections.Contacts.NXNastranGeneral(strName="", iPiType=0, iPiAlg=0, dPdNorPenFactor=0, dPdTanPenFactor=0, dPdForceConTol=0, dPdMaxForceIter=0, dPdMaxStaIter=0, dPdChangeNum=0, dPdMinContactPer=0, iPiShellThickness=0, iPiContactStatus=0, iPiInitGapPenetra=0, iPiRegionRefine=0, iPiEvaluPts=0, dPdMinSearDist=0, dPdMaxSearDist=0, dPdFricCoef=0, dPdSearchDist=0, dPdPenatlyFactor=0, iPiShellOffset=0, crlTargets=[], crEdit=None, iColor=0, iMethod=0)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPiType`

- The pi type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPiAlg`

- The pi algorithm.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdNorPenFactor`

- The pd nor pen factor.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdTanPenFactor`

- The pd tan pen factor.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdForceConTol`

- The pd force con tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdMaxForceIter`

- The pd maximum force iterator.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdMaxStaIter`

- The pd maximum sta iterator.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdChangeNum`

- The pd change number.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdMinContactPer`

- The pd minimum contact per.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPiShellThickness`

- The pi shell thickness.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPiContactStatus`

- The pi contact status.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPiInitGapPenetra`

- The pi initial gap penetra.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPiRegionRefine`

- The pi region refine.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPiEvaluPts`

- The pi evalu pts.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdMinSearDist`

- The pd minimum sear dist.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdMaxSearDist`

- The pd maximum sear dist.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdFricCoef`

- The pd fric coefficient .

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdSearchDist`

- The pd search dist.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPdPenatlyFactor`

- The pd penatly factor.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPiShellOffset`

- The pi shell offset.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iColor`

- The color.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.NXNastranGeneral(strName="", iPiType=0, iPiAlg=0, dPdNorPenFactor=0, dPdTanPenFactor=0, dPdForceConTol=0, dPdMaxForceIter=0, dPdMaxStaIter=0, dPdChangeNum=0, dPdMinContactPer=0, iPiShellThickness=0, iPiContactStatus=0, iPiInitGapPenetra=0, iPiRegionRefine=0, iPiEvaluPts=0, dPdMinSearDist=0, dPdMaxSearDist=0, dPdFricCoef=0, dPdSearchDist=0, dPdPenatlyFactor=0, iPiShellOffset=0, crlTargets=[], crEdit=None, iColor=0, iMethod=0)
```
