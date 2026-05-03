---
title: "Tools.TotalLoad.Face()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > TotalLoad > Face"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description is missing in all versions — placeholder inserted
-->

## Description

## Syntax

```psj
Tools.TotalLoad.Face(crlTargets=[], crCoordinate=None, strOutput="Total", iPrecision=6)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crCoordinate` @type(Cursor) @default(None)

- The coordinate.

### `strOutput` @type(String) @default("Total")

- The output.

### `iPrecision` @type(Integer) @default(6)

- The precision.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.TotalLoad.Face(crlTargets=[], crCoordinate=None, strOutput="Total", iPrecision=6)
```
