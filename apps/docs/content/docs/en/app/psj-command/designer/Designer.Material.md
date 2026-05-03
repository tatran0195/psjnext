---
title: "Designer.Material()"
description: "Create a material."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Designer > Material"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","Create a material."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a material.

## Syntax

```psj
Designer.Material(strMatName, strPropName, dThickness, crlTargets)
```

## Inputs

### `strMatName` @type(String) @required

- The material name.

### `strPropName` @type(String) @required

- The property name.

### `dThickness` @type(Double) @required

- The thickness.

### `crlTargets` @type(List\[Cursor]) @required

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Designer.Material(strMatName, strPropName, dThickness, crlTargets)
```
