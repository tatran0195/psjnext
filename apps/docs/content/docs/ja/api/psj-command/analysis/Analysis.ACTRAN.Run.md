---
title: "Analysis.ACTRAN.Run()"
description: "Run Actran analysis"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ACTRAN > Run"
---

## Description

Run Actran analysis

## Syntax

```psj
Analysis.ACTRAN.Run(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### actranAnalysis

- Specify the Actran analysis data structure.
- The default value is _[ACTRAN\_ANALYSIS](./../../data-type/psj-command/parameter-types/ACTRAN _ANALYSIS)_.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ACTRAN.Run(actranAnalysis=ACTRAN _ANALYSIS(), crlTargets=[], crEdit=None)
```
