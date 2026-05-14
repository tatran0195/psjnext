---
title: "Geometry.DeleteEntity.Face()"
description: "Delete face entities"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Delete Entity > Face"
---

## Description

Delete face entities.

## Syntax

```psj
Geometry.DeleteEntity.Face(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The faces to be deleted.

## Return Code

True if success, or False if fail.

## Sample Code

```psj {3}
Geometry.Part.Cube()

flag = Geometry.DeleteEntity.Face(crlFaces=[Face(26)])

JPT.Debugger(flag)
```
