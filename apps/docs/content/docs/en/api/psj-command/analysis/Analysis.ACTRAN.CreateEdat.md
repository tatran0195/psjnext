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

<!-- @since:5.0.1 @type:ACTRAN _ANALYSIS @optional @default:ACTRAN _ANALYSIS -->
### `actranAnalysis`

- The Actran analysis data structure.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ACTRAN.CreateEdat(actranAnalysis=ACTRAN _ANALYSIS(), crlTargets=[], crEdit=None)
```
