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

<!-- @type:List[Cursor] @required @since:5.0.1 @deprecated:5.1.0 -->
### `crlParts`

- The part.

<!-- @type:Boolean @required @since:5.0.1 @removed:5.2.0 -->
### `bIsMergePart`

- The is merge part.

<!-- @type:Boolean @required -->
### `bIsRenumber`

- The is renumber.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
ACModeling.ACBoundary.FirstMethod(crlParts, bIsMergePart, bIsRenumber)
```
