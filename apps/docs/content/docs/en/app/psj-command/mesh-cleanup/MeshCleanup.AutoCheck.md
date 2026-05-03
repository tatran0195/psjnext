---
title: "MeshCleanup.AutoCheck()"
description: "check meshing quality"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshCleanup > AutoCheck"
---

## Description

Check meshing quality

## Syntax

```psj
MeshCleanup.AutoCheck(crlParts, iElemType, blCheckCondition, blElemQuality, dlLimitValue, crlElems)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The part.

### `iElemType` @type(Integer) @required

- The element type.

### `blCheckCondition` @type(Boolean List) @required

- The check condition.

### `blElemQuality` @type(Boolean List) @required

- The element quality.

### `dlLimitValue` @type(Double List) @required

- The limit value.

### `crlElems` @type(List\[Cursor]) @required

- The element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.AutoCheck(crlParts, iElemType, blCheckCondition, blElemQuality, dlLimitValue, crlElems)
```
