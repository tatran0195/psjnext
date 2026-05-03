---
title: "Properties.Section.ModifyGeneral()"
description: "Modify the existing general section for 1D Property."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Section > ModifyGeneral"
macro_link: "Property1DSectionModify_General"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Modify the existing general section for 1D Property."]}
   [param_removed_unexpectedly] Param 'bTapered' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Modify the existing general section for 1D Property.

## Syntax

```psj
Properties.Section.ModifyGeneral(...)
```

## Inputs

### `strName` @type(String) @default("")

- The section name.

### `crSection` @type(Cursor) @default(None)

- The existing section to modify.

### `iSecType` @type(Integer) @default(0)

- The section type.

### `iGeneralType` @type(Integer) @default(0)

- The general type.

### `dA` @type(Double) @default(0)

- The a.

### `dB` @type(Double) @default(0)

- The b.

### `dH` @type(Double) @default(0)

- The h.

### `dT1` @type(Double) @default(0)

- The t1.

### `dT2` @type(Double) @default(0)

- The t2.

### `dT3` @type(Double) @default(0)

- The t3.

### `bTapered` @type(Boolean) @default(False) @deprecated @until(5.1.0)

-A _Boolean_ specifying whether or not tapered.



### `dDaTap` @type(Double) @default(0)

- The a tapered.

### `dDbTap` @type(Double) @default(0)

- The b tapered.

### `dDhTap` @type(Double) @default(0)

- The h tapered.

### `dDt1Tap` @type(Double) @default(0)

- The t1 tapered.

### `dDt2Tap` @type(Double) @default(0)

- The t2 tapered.

### `dDt3Tap` @type(Double) @default(0)

- The t3 tapered.

### `iDirType` @type(Integer) @default(0) @since(5.1.0)

- Direction type.

### `bTapered` @type(Boolean) @default(False) @deprecated @until(5.1.0)

- The tapered.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {5-9}
Properties.Section.AddGeneral(  strName="t1", 
                                iSecGenType=2, 
                                dDsecGensizeT1=0.001, 
                                iDirType=1)
Properties.Section.ModifyGeneral(strName="t1", 
                                crSection=SectionGeneral(1), 
                                iGeneralType=2, 
                                dT1=0.001, 
                                iDirType=3)
```
