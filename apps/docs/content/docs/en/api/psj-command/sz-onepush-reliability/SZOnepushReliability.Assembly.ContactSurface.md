---
title: "SZOnepushReliability.Assembly.ContactSurface()"
description: "Contact surface"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "SZOnepushReliability > Assembly > ContactSurface"
---

## Description

Contact surface

## Syntax

```psj
SZOnepushReliability.Assembly.ContactSurface(crlSrcFace, crlTarPart, dTolerance, iLayer)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlSrcFace`

- The source face.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTarPart`

- The tar part.

<!-- @since:5.0.1 @type:Double @required -->
### `dTolerance`

- The tolerance.

<!-- @since:5.0.1 @type:Integer @required -->
### `iLayer`

- The layer.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SZOnepushReliability.Assembly.ContactSurface(crlSrcFace, crlTarPart, dTolerance, iLayer)
```
