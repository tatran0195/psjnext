---
title: "Properties.Section1D()"
description: "Create 1D Property Sketcher Section"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Section1D"
macro_link: "[Property1DSection](../../macro/properties/Property1DSection)"
---

## Description

Create 1D Property Sketcher Section

## Syntax

```psj
Properties.Section1D(strName="", iSecType=0, iSecGenType=2, dSecGensizeA=0, dSecGensizeB=0, dSecGensizeH=0, dSecGensizeT1=0, dSecGensizeT2=0, dSecGensizeT3=0, bSecTapered=False, dSecGensizeATap=0, dSecGensizeBTap=0, dSecGensizeHTap=0, dSecGensizeT1Tap=0, dSecGensizeT2Tap=0, dSecGensizeT3Tap=0)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `iSecType` @type(Integer) @default(0)

- The section type.

### `iSecGenType` @type(Integer) @default(2)

- The section general type.

### `dSecGensizeA` @type(Double) @default(0)

- The section general size a.

### `dSecGensizeB` @type(Double) @default(0)

- The section general size b.

### `dSecGensizeH` @type(Double) @default(0)

- The section general size h.

### `dSecGensizeT1` @type(Double) @default(0)

- The section general size t1.

### `dSecGensizeT2` @type(Double) @default(0)

- The section general size t2.

### `dSecGensizeT3` @type(Double) @default(0)

- The section general size t3.

### `bSecTapered` @type(Boolean) @default(False)

- The section tapered.

### `dSecGensizeATap` @type(Double) @default(0)

- The section general size a tapered.

### `dSecGensizeBTap` @type(Double) @default(0)

- The section general size tapered.

### `dSecGensizeHTap` @type(Double) @default(0)

- The section general size h tapered.

### `dSecGensizeT1Tap` @type(Double) @default(0)

- The section general size t1 tapered.

### `dSecGensizeT2Tap` @type(Double) @default(0)

- The section general size t2 tapered.

### `dSecGensizeT3Tap` @type(Double) @default(0)

- The section general size t3 tapered.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Section1D(strName="", iSecType=0, iSecGenType=2, dSecGensizeA=0, dSecGensizeB=0, dSecGensizeH=0, dSecGensizeT1=0, dSecGensizeT2=0, dSecGensizeT3=0, bSecTapered=False, dSecGensizeATap=0, dSecGensizeBTap=0, dSecGensizeHTap=0, dSecGensizeT1Tap=0, dSecGensizeT2Tap=0, dSecGensizeT3Tap=0)
```
