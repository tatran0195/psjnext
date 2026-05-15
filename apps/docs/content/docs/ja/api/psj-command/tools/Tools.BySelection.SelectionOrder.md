---
title: "Tools.BySelection.SelectionOrder()"
description: "Renumber by selection order"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Tools > BySelection > SelectionOrder"
---

## Description

Renumber by selection order

## Syntax

```psj
Tools.BySelection.SelectionOrder(crlTargets=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iType

- Specify the type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iStartID

- Specify the start ID.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iIncrementStep

- Specify the increment step.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### bAscending

- Specify the ascending.
- The default value is True.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.BySelection.SelectionOrder(crlTargets=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True)
```
