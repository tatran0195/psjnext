---
title: "Connections.Contacts.NXNastran.ContactTable()"
description: "Create Contact NXNastran Contact Table"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > NXNastran > ContactTable"
---

## Description

Create Contact NXNastran Contact Table

## Syntax

```psj
Connections.Contacts.NXNastran.ContactTable(strName="", iType=0, iAlg=0, dNorPenFactor=0, dTanPenFactor=0, dForceConTol=0, dMaxForceIter=0, dMaxStaIter=0, dChangeNum=0, dMinContactPer=0, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=0, dMinSearDist=0, dMaxSearDist=0, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, crplTargetPair=[], crEdit=None, iColor=0, iMethod=1)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `iType` @type(Integer) @default(0)

- The type.

### `iAlg` @type(Integer) @default(0)

- The algorithm.

### `dNorPenFactor` @type(Double) @default(0)

- The nor pen factor.

### `dTanPenFactor` @type(Double) @default(0)

- The tan pen factor.

### `dForceConTol` @type(Double) @default(0)

- The force con tolerance.

### `dMaxForceIter` @type(Double) @default(0)

- The maximum force iterator.

### `dMaxStaIter` @type(Double) @default(0)

- The maximum sta iterator.

### `dChangeNum` @type(Double) @default(0)

- The change number.

### `dMinContactPer` @type(Double) @default(0)

- The minimum contact per.

### `iShellThickness` @type(Integer) @default(0)

- The shell thickness.

### `iContactStatus` @type(Integer) @default(0)

- The contact status.

### `iInitGapPenetra` @type(Integer) @default(0)

- The initial gap penetra.

### `iRegionRefine` @type(Integer) @default(0)

- The region refine.

### `iEvaluPts` @type(Integer) @default(0)

- The evalu pts.

### `dMinSearDist` @type(Double) @default(0)

- The minimum sear dist.

### `dMaxSearDist` @type(Double) @default(0)

- The maximum sear dist.

### `dFricCoef` @type(Double) @default(0)

- The fric coefficient .

### `dSearchDist` @type(Double) @default(0)

- The search dist.

### `dPenatlyFactor` @type(Double) @default(0)

- The penatly factor.

### `iShellOffset` @type(Integer) @default(0)

- The shell offset.

### `crplTargetPair` @type(Cursor Pair List) @default(\[])

- The target pair.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iColor` @type(Integer) @default(0)

- The color.

### `iMethod` @type(Integer) @default(1)

- The method.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.NXNastran.ContactTable(strName="", iType=0, iAlg=0, dNorPenFactor=0, dTanPenFactor=0, dForceConTol=0, dMaxForceIter=0, dMaxStaIter=0, dChangeNum=0, dMinContactPer=0, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=0, dMinSearDist=0, dMaxSearDist=0, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, crplTargetPair=[], crEdit=None, iColor=0, iMethod=1)
```
