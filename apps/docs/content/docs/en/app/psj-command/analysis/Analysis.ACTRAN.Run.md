---
title: 'Analysis.ACTRAN.Run()'
description: 'Run Actran analysis'
version_introduced: '5.0.1'
available_versions: 'all'
ribbon: 'Analysis > ACTRAN > Run'
---

<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Run Actran analysis"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Run Actran analysis

## Syntax

```psj
Analysis.ACTRAN.Run(...)
```

## Inputs

### `actranAnalysis` @type(ACTRAN_ANALYSIS) @default(ACTRAN_ANALYSIS)

- The Actran analysis data structure.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ACTRAN.Run(actranAnalysis=ACTRAN_ANALYSIS(), crlTargets=[], crEdit=None)
```
