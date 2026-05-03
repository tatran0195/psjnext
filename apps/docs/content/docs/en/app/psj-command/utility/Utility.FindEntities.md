---
title: "Utility.FindEntities()"
description: "Search entity by ID, Name ...etc"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Utility > FindEntities"
macro_link: "[FindEntities](../../macro/utility/FindEntities)"
---

## Description

Search entity by ID, Name ...etc

## Syntax

```psj
Utility.FindEntities(strTarget, strFindType, bFindMatch=False)
```

## Inputs

### `strTarget` @type(String) @required

- The target.

### `strFindType` @type(String) @required

- The find type.

### `bFindMatch` @type(Boolean) @default(False)

- The find match.

## Return Code

A _List of Cursor_ of result entities found.

## Sample Code

```psj
Geometry.Part.Cube()

list_faces = Utility.FindEntities("24 26", "Face")
```
