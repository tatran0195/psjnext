---
title: "Utility.FindEntities()"
description: "Search entity by ID, Name ...etc"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Utility > FindEntities"
macro _link: "[FindEntities](../../macro/utility/FindEntities)"
---

## Description

Search entity by ID, Name ...etc

## Syntax

```psj
Utility.FindEntities(strTarget, strFindType, bFindMatch=False)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strTarget`

- The target.

<!-- @since:5.0.1 @type:String @required -->
### `strFindType`

- The find type.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bFindMatch`

- The find match.

## Return Code

A _List of Cursor_ of result entities found.

## Sample Code

```psj
Geometry.Part.Cube()

list _faces = Utility.FindEntities("24 26", "Face")
```
