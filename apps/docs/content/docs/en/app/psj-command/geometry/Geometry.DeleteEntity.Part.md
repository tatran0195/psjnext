---
title: "Geometry.DeleteEntity.Part()"
description: "Delete part entities"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Delete Entity > Part"
---

## Description

Delete part entities.

## Syntax

```psj
Geometry.DeleteEntity.Part(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- Parts to be deleted.

## Return Code

True if success, or False if fail.

## Sample Code

```psj {3}
cube = Geometry.Part.Cube()

flag = Geometry.DeleteEntity.Part(crlParts=[cube])

JPT.Debugger(flag)
```
