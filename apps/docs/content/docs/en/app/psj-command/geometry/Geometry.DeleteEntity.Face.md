---
title: "Geometry.DeleteEntity.Face()"
description: "Delete face entities"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Delete Entity > Face"
---

## Description

Delete face entities.

## Syntax

```psj
Geometry.DeleteEntity.Face(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- Faces to be deleted.

## Return Code

True if success, or False if fail.

## Sample Code

```psj {3}
Geometry.Part.Cube()

flag = Geometry.DeleteEntity.Face(crlFaces=[Face(26)])

JPT.Debugger(flag)
```
