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

<!-- @since:5.0.1 @required -->
### strTarget

- Specify the target.

<!-- @since:5.0.1 @required -->
### strFindType

- Specify the find type.

<!-- @since:5.0.1 @optional -->
### bFindMatch

- Specify the find match.
- The default value is False.

## Return Code

A _List of Cursor_ of result entities found.

## Sample Code

```psj
Geometry.Part.Cube()

list _faces = Utility.FindEntities("24 26", "Face")
```
