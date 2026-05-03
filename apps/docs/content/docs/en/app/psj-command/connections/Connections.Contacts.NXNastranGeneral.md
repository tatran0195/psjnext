---
title: "Connections.Contacts.NXNastranGeneral()"
description: "Define contact settings for the NX solver."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > NXNastranGeneral"
macro_link: "[ContactNXNastran](../../macro/connections/ContactNXNastran)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Define contact settings for the NX solver."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Define contact settings for the NX solver.

## Syntax

```psj
Connections.Contacts.NXNastranGeneral(strName="", iPiType=0, iPiAlg=0, dPdNorPenFactor=0, dPdTanPenFactor=0, dPdForceConTol=0, dPdMaxForceIter=0, dPdMaxStaIter=0, dPdChangeNum=0, dPdMinContactPer=0, iPiShellThickness=0, iPiContactStatus=0, iPiInitGapPenetra=0, iPiRegionRefine=0, iPiEvaluPts=0, dPdMinSearDist=0, dPdMaxSearDist=0, dPdFricCoef=0, dPdSearchDist=0, dPdPenatlyFactor=0, iPiShellOffset=0, crlTargets=[], crEdit=None, iColor=0, iMethod=0)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `iPiType` @type(Integer) @default(0)

- The pi type.

### `iPiAlg` @type(Integer) @default(0)

- The pi algorithm.

### `dPdNorPenFactor` @type(Double) @default(0)

- The pd nor pen factor.

### `dPdTanPenFactor` @type(Double) @default(0)

- The pd tan pen factor.

### `dPdForceConTol` @type(Double) @default(0)

- The pd force con tolerance.

### `dPdMaxForceIter` @type(Double) @default(0)

- The pd maximum force iterator.

### `dPdMaxStaIter` @type(Double) @default(0)

- The pd maximum sta iterator.

### `dPdChangeNum` @type(Double) @default(0)

- The pd change number.

### `dPdMinContactPer` @type(Double) @default(0)

- The pd minimum contact per.

### `iPiShellThickness` @type(Integer) @default(0)

- The pi shell thickness.

### `iPiContactStatus` @type(Integer) @default(0)

- The pi contact status.

### `iPiInitGapPenetra` @type(Integer) @default(0)

- The pi initial gap penetra.

### `iPiRegionRefine` @type(Integer) @default(0)

- The pi region refine.

### `iPiEvaluPts` @type(Integer) @default(0)

- The pi evalu pts.

### `dPdMinSearDist` @type(Double) @default(0)

- The pd minimum sear dist.

### `dPdMaxSearDist` @type(Double) @default(0)

- The pd maximum sear dist.

### `dPdFricCoef` @type(Double) @default(0)

- The pd fric coefficient .

### `dPdSearchDist` @type(Double) @default(0)

- The pd search dist.

### `dPdPenatlyFactor` @type(Double) @default(0)

- The pd penatly factor.

### `iPiShellOffset` @type(Integer) @default(0)

- The pi shell offset.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iColor` @type(Integer) @default(0)

- The color.

### `iMethod` @type(Integer) @default(0)

- The method.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.NXNastranGeneral(strName="", iPiType=0, iPiAlg=0, dPdNorPenFactor=0, dPdTanPenFactor=0, dPdForceConTol=0, dPdMaxForceIter=0, dPdMaxStaIter=0, dPdChangeNum=0, dPdMinContactPer=0, iPiShellThickness=0, iPiContactStatus=0, iPiInitGapPenetra=0, iPiRegionRefine=0, iPiEvaluPts=0, dPdMinSearDist=0, dPdMaxSearDist=0, dPdFricCoef=0, dPdSearchDist=0, dPdPenatlyFactor=0, iPiShellOffset=0, crlTargets=[], crEdit=None, iColor=0, iMethod=0)
```
