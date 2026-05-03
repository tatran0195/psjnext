---
title: "Analysis.ACTRAN.CreateEdat()"
description: "Export edat file."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Analysis > ACTRAN > CreateEdat"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Export edat file."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Export edat file.

## Syntax

```psj
Analysis.ACTRAN.CreateEdat(...)
```

## Inputs

### `actranAnalysis` @type(ACTRAN\_ANALYSIS) @default(ACTRAN\_ANALYSIS)

- The Actran analysis data structure.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Analysis.ACTRAN.CreateEdat(actranAnalysis=ACTRAN_ANALYSIS(), crlTargets=[], crEdit=None)
```
