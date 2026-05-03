---
title: "SNOnePush.DropTest.CalcTimestep()"
description: "Used to calculate time step for drop test function"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "SNOnePush > DropTest > CalcTimestep"
---

## Description

Used to calculate time step for drop test function

## Syntax

```psj
SNOnePush.DropTest.CalcTimestep(dRelevantElemRate, dChangeMassRage)
```

## Inputs

### `dRelevantElemRate` @type(Double) @required

- The relevant element rate.

### `dChangeMassRage` @type(Double) @required

- The change mass rage.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SNOnePush.DropTest.CalcTimestep(dRelevantElemRate, dChangeMassRage)
```
