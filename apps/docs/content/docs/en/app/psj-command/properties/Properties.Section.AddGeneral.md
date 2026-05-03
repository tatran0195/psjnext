---
title: "Properties.Section.AddGeneral()"
description: "Unknown Description"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Section > AddGeneral"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

The general properties of a one-dimensional section are generated.

## Syntax

```psj
Properties.Section.AddGeneral(...)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `iSecType` @type(Integer) @default(0)

- The section type.

### `iSecGenType` @type(Integer) @default(0)

- The section general type.

### `dDsecGensizeA` @type(Double) @default(0)

- The section general size a.

### `dDsecGensizeB` @type(Double) @default(0)

- The section general size b.

### `dDsecGensizeH` @type(Double) @default(0)

- The section general size h.

### `dDsecGensizeT1` @type(Double) @default(0)

- The section general size t1.

### `dDsecGensizeT2` @type(Double) @default(0)

- The section general size t2.

### `dDsecGensizeT3` @type(Double) @default(0)

- The section general size t3.

### `bBsecTapered` @type(Boolean) @default(False)

- The bsec tapered.

### `dDsecGensizeATap` @type(Double) @default(0)

- The section general size a tapered.

### `dDsecGensizeBTap` @type(Double) @default(0)

- The section general size b tapered.

### `dDsecGensizeHTap` @type(Double) @default(0)

- The section general size h tapered.

### `dDsecGensizeT1Tap` @type(Double) @default(0)

- The section general size t1 tapered.

### `dDsecGensizeT2Tap` @type(Double) @default(0)

- The section general size t2 tapered.

### `dDsecGensizeT3Tap` @type(Double) @default(0)

- The section general size t3 tapered.

### `iDirType` @type(Integer) @default(0) @since(5.1.0)

- The y direction type.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Section.AddGeneral(strName="t1", 
                            iSecGenType=2, 
                            dDsecGensizeT1=0.001, 
                            iDirType=1)
```
