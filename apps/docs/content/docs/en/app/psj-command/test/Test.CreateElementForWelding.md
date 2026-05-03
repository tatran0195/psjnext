---
title: "Test.CreateElementForWelding()"
description: "Create weld elements"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Test > CreateElementForWelding"
---

## Description

Create weld elements

## Syntax

```psj
Test.CreateElementForWelding(crlSrcElems, crlDstElems, crlSideElems, crlParts, crMaterial)
```

## Inputs

### `crlSrcElems` @type(List\[Cursor]) @required

- The source elems.

### `crlDstElems` @type(List\[Cursor]) @required

- The dst elems.

### `crlSideElems` @type(List\[Cursor]) @required

- The side elems.

### `crlParts` @type(List\[Cursor]) @required

- The part.

### `crMaterial` @type(Cursor) @required

- The material.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.CreateElementForWelding(crlSrcElems, crlDstElems, crlSideElems, crlParts, crMaterial)
```
