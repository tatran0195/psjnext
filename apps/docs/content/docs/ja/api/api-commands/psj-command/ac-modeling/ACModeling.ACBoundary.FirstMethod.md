---
title: 'ACModeling.ACBoundary.FirstMethod() '
description: 'Unknown Description'
version_introduced: '5.1.0'
available_versions: 'all'
ribbon: 'ACModeling > ACBoundary > FirstMethod'
---

## Description

Unknown Description

## Syntax

```psj
ACModeling.ACBoundary.FirstMethod(...)
```

## Inputs

<!-- @since:5.0.1 @required @deprecated:5.1.0 -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @required @removed:5.2.0 -->
### `bIsMergePart`

- The is merge part.

<!-- @since:5.1.0 @required -->
### `bIsRenumber`

- The is renumber.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
ACModeling.ACBoundary.FirstMethod(crlParts, bIsMergePart, bIsRenumber)
```
