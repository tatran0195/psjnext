---
title: "Geometry.Part.Elems()"
description: "create part from element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Part > Elems"
---

## Description

Create part from element

## Syntax

```psj
Geometry.Part.Elems(crlElems, strName)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlElems

- Specify the element.

<!-- @since:5.0.1 @required -->
### strName

- Specify the part name.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Elems(crlElems, strName)
```
