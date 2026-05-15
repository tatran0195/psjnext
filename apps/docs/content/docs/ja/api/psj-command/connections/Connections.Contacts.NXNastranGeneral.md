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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iPiType

- Specify the pi type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPiAlg

- Specify the pi algorithm.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdNorPenFactor

- Specify the pd nor pen factor.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdTanPenFactor

- Specify the pd tan pen factor.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdForceConTol

- Specify the pd force con tolerance.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdMaxForceIter

- Specify the pd maximum force iterator.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdMaxStaIter

- Specify the pd maximum sta iterator.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdChangeNum

- Specify the pd change number.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdMinContactPer

- Specify the pd minimum contact per.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPiShellThickness

- Specify the pi shell thickness.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPiContactStatus

- Specify the pi contact status.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPiInitGapPenetra

- Specify the pi initial gap penetra.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPiRegionRefine

- Specify the pi region refine.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPiEvaluPts

- Specify the pi evalu pts.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdMinSearDist

- Specify the pd minimum sear dist.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdMaxSearDist

- Specify the pd maximum sear dist.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdFricCoef

- Specify the pd fric coefficient .
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdSearchDist

- Specify the pd search dist.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPdPenatlyFactor

- Specify the pd penatly factor.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPiShellOffset

- Specify the pi shell offset.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iColor

- Specify the color.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.NXNastranGeneral(strName="", iPiType=0, iPiAlg=0, dPdNorPenFactor=0, dPdTanPenFactor=0, dPdForceConTol=0, dPdMaxForceIter=0, dPdMaxStaIter=0, dPdChangeNum=0, dPdMinContactPer=0, iPiShellThickness=0, iPiContactStatus=0, iPiInitGapPenetra=0, iPiRegionRefine=0, iPiEvaluPts=0, dPdMinSearDist=0, dPdMaxSearDist=0, dPdFricCoef=0, dPdSearchDist=0, dPdPenatlyFactor=0, iPiShellOffset=0, crlTargets=[], crEdit=None, iColor=0, iMethod=0)
```
