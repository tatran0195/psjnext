---
title: "Test.CreateElementForWelding()"
description: "Create weld elements"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Test > CreateElementForWelding"
---

## Description

Create weld elements

## Syntax

```psj
Test.CreateElementForWelding(crlSrcElems, crlDstElems, crlSideElems, crlParts, crMaterial)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlSrcElems`

- The source elems.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlDstElems`

- The dst elems.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlSideElems`

- The side elems.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crMaterial`

- The material.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.CreateElementForWelding(crlSrcElems, crlDstElems, crlSideElems, crlParts, crMaterial)
```
