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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iType

- Specify the type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAlg

- Specify the algorithm.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dNorPenFactor

- Specify the nor pen factor.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTanPenFactor

- Specify the tan pen factor.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dForceConTol

- Specify the force con tolerance.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMaxForceIter

- Specify the maximum force iterator.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMaxStaIter

- Specify the maximum sta iterator.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dChangeNum

- Specify the change number.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMinContactPer

- Specify the minimum contact per.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iShellThickness

- Specify the shell thickness.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactStatus

- Specify the contact status.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iInitGapPenetra

- Specify the initial gap penetra.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iRegionRefine

- Specify the region refine.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEvaluPts

- Specify the evalu pts.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMinSearDist

- Specify the minimum sear dist.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMaxSearDist

- Specify the maximum sear dist.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dFricCoef

- Specify the fric coefficient .
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSearchDist

- Specify the search dist.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPenatlyFactor

- Specify the penatly factor.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iShellOffset

- Specify the shell offset.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crplTargetPair

- Specify the target pair.
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
- The default value is 1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.NXNastran.ContactTable(strName="", iType=0, iAlg=0, dNorPenFactor=0, dTanPenFactor=0, dForceConTol=0, dMaxForceIter=0, dMaxStaIter=0, dChangeNum=0, dMinContactPer=0, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=0, dMinSearDist=0, dMaxSearDist=0, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, crplTargetPair=[], crEdit=None, iColor=0, iMethod=1)
```
