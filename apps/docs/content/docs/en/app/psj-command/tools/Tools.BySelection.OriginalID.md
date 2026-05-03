---
title: "Tools.BySelection.OriginalID()"
description: "Renumber by original ID"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > BySelection > OriginalID"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Renumber by original ID

## Syntax

```psj
Tools.BySelection.OriginalID(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `iType` @type(Integer) @default(0)

- The type.

### `iMethod` @type(Integer) @default(0)

- The method.

### `iStartID` @type(Integer) @default(1)

- The start ID.

### `iIncrementStep` @type(Integer) @default(1)

- The increment step.

### `bAscending` @type(Boolean) @default(True)

- The ascending.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
```
