---
title: "SNOnePush.DropTest.CalcTimestep()"
description: "Used to calculate time step for drop test function"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "SNOnePush > DropTest > CalcTimestep"
---

## Description

Used to calculate time step for drop test function

## Syntax

```psj
SNOnePush.DropTest.CalcTimestep(dRelevantElemRate, dChangeMassRage)
```

## Inputs

<!-- @since:5.0.1 @type:Double @required -->
### `dRelevantElemRate`

- The relevant element rate.

<!-- @since:5.0.1 @type:Double @required -->
### `dChangeMassRage`

- The change mass rage.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SNOnePush.DropTest.CalcTimestep(dRelevantElemRate, dChangeMassRage)
```
