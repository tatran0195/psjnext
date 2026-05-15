---
title: "Analysis.ACTRAN.CreateEdat()"
description: "Export edat file."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Analysis > ACTRAN > CreateEdat"
---

## Description

Export edat file.

## Syntax

```psj
Analysis.ACTRAN.CreateEdat(...)
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
Analysis.ACTRAN.CreateEdat(actranAnalysis=ACTRAN _ANALYSIS(), crlTargets=[], crEdit=None)
```
