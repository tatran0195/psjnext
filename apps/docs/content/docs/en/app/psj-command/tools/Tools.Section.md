---
title: "Tools.Section()"
description: "Enable / Disable section display."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Tools > Section"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Enable / Disable section display."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Enable / Disable section display.

## Syntax

```psj
Tools.Section(bSection)
```

## Inputs

### `bSection` @type(Boolean) @required

- The section.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Tools.Section(bSection=True)
```
