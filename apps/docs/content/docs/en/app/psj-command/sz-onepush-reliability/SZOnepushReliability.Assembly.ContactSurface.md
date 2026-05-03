---
title: "SZOnepushReliability.Assembly.ContactSurface()"
description: "Contact surface"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "SZOnepushReliability > Assembly > ContactSurface"
---

## Description

Contact surface

## Syntax

```psj
SZOnepushReliability.Assembly.ContactSurface(crlSrcFace, crlTarPart, dTolerance, iLayer)
```

## Inputs

### `crlSrcFace` @type(List\[Cursor]) @required

- The source face.

### `crlTarPart` @type(List\[Cursor]) @required

- The tar part.

### `dTolerance` @type(Double) @required

- The tolerance.

### `iLayer` @type(Integer) @required

- The layer.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SZOnepushReliability.Assembly.ContactSurface(crlSrcFace, crlTarPart, dTolerance, iLayer)
```
