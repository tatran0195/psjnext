---
title: "Connections.Contacts.NXNastran.ContactShareFace()"
description: "Create Contact NXNastran Contact Share Face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > NXNastran > ContactShareFace"
---

## Description

Create Contact NXNastran Contact Share Face

## Syntax

```psj
Connections.Contacts.NXNastran.ContactShareFace(crlShareFace=[], strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=3, crEdit=None)
```

## Inputs

### `crlShareFace` @type(List\[Cursor]) @default(\[])

- The share face.

### `strName` @type(String) @default("ContactNXNastran\_1")

- The name.

### `iContactType` @type(Integer) @default(0)

- The contact type.

### `iContactAlg` @type(Integer) @default(0)

- The contact algorithm.

### `dNorPenFactor` @type(Double) @default(10)

- The nor pen factor.

### `dTanPenFactor` @type(Double) @default(1)

- The tan pen factor.

### `dForceConTol` @type(Double) @default(0.01)

- The force con tolerance.

### `dMaxForceIter` @type(Double) @default(10)

- The maximum force iterator.

### `dMaxStaIter` @type(Double) @default(20)

- The maximum sta iterator.

### `dChangeNum` @type(Double) @default(0.02)

- The change number.

### `dMinContactPer` @type(Double) @default(100)

- The minimum contact per.

### `iShellThickness` @type(Integer) @default(0)

- The shell thickness.

### `iContactStatus` @type(Integer) @default(0)

- The contact status.

### `iInitGapPenetra` @type(Integer) @default(0)

- The initial gap penetra.

### `iRegionRefine` @type(Integer) @default(0)

- The region refine.

### `iEvaluPts` @type(Integer) @default(1)

- The evalu pts.

### `dMinSearDist` @type(Double) @default(0)

- The minimum sear dist.

### `dMaxSearDist` @type(Double) @default(0.01)

- The maximum sear dist.

### `dFricCoef` @type(Double) @default(0)

- The fric coefficient .

### `dSearchDist` @type(Double) @default(0)

- The search dist.

### `dPenatlyFactor` @type(Double) @default(0)

- The penatly factor.

### `iShellOffset` @type(Integer) @default(0)

- The shell offset.

### `iColor` @type(Integer) @default(0)

- The color.

### `iMethod` @type(Integer) @default(3)

- The method.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.NXNastran.ContactShareFace(crlShareFace=[], strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=3, crEdit=None)
```
