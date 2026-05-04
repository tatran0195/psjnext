---
title: "ACModeling.ACBoundary.FirstMethod()"
description: "Unknown Description"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "ACModeling > ACBoundary > FirstMethod"
---

## Description

Unknown Description

## Syntax

```psj
ACModeling.ACBoundary.FirstMethod(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The part.

### `bIsMergePart` @type(Boolean) @required

- The is merge part.

### `bIsRenumber` @type(Boolean) @required

- The is renumber.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
ACModeling.ACBoundary.FirstMethod(crlParts, bIsMergePart, bIsRenumber)
```
