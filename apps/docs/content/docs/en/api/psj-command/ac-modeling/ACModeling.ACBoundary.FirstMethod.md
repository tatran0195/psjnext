---
title: "ACModeling.ACBoundary.FirstMethod()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "ACModeling > ACBoundary > FirstMethod"
---

## Description

Unknown Description

## Syntax

```psj
ACModeling.ACBoundary.FirstMethod(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bIsMergePart`

- The is merge part.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bIsRenumber`

- The is renumber.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
ACModeling.ACBoundary.FirstMethod(crlParts, bIsMergePart, bIsRenumber)
```
