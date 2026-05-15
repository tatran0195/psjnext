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

<!-- @since:5.0.1 @required -->
### crlSrcElems

- Specify the source elems.

<!-- @since:5.0.1 @required -->
### crlDstElems

- Specify the dst elems.

<!-- @since:5.0.1 @required -->
### crlSideElems

- Specify the side elems.

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the part.

<!-- @since:5.0.1 @required -->
### crMaterial

- Specify the material.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.CreateElementForWelding(crlSrcElems, crlDstElems, crlSideElems, crlParts, crMaterial)
```
