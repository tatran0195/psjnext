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

<!-- @since:5.0.1 @required -->
<!-- 
@since:5.1.0 
@deprecated:'Use ACModeling.ACBoundary.CreateBoundary instead.
This is a multi-line deprecation message.
It uses whitespace-pre-wrap to maintain line breaks.' 
-->
### `crlParts`

- The part.

<!-- @removed:5.2.0 -->
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
