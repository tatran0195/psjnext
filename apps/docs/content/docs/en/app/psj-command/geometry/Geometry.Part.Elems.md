---
title: "Geometry.Part.Elems()"
description: "create part from element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Part > Elems"
---

## Description

Create part from element

## Syntax

```psj
Geometry.Part.Elems(crlElems, strName)
```

## Inputs

### `crlElems` @type(List\[Cursor]) @required

- The element.

### `strName` @type(String) @required

- The part name.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Elems(crlElems, strName)
```
