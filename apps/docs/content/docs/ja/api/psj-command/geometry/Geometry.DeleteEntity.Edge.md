---
title: "Geometry.DeleteEntity.Edge()"
description: "Delete the selected edge entities"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Delete Entity > Edge"
---

## Description

Delete the selected edge entities.

## Syntax

```psj
Geometry.DeleteEntity.Edge(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlEdges

- Specify edges to be deleted.

## Return Code

True if success, or False if fail.

## Sample Code

```psj {3}
Geometry.Part.Cube()

flag = Geometry.DeleteEntity.Edge(crlEdges=[Edge(15, 18, 19)])

JPT.Debugger(flag)
```
