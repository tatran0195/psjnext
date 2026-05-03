---
title: "Assemble.SeparateFaces.Shell()"
description: "Separate shared Nodes for Shell that is shared between the shell parts into double nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assemble > Separate Faces > Shell"
---

## Description

Separate shared Nodes for Shell that is shared between the shell parts into double nodes.

## Syntax

```psj
Assemble.SeparateFaces.Shell(...)
```

## Inputs

### `iType` @type(Integer) @default(0)

- The type of entity to be selected.

### `crlEntity` @type(List\[Cursor]) @default(\[])

- The list of target item which will be separated.

### `bCreateGroup` @type(Boolean) @default(False)

- Enable/disable create group option.

## Return Code

A _List Cursor_ of separated edges if success, or _None_ if fail.

## Sample Code

```psj {8,9}
Geometry.Part.Cube(strName="Cube_1",
                   iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=7463537)
MeshEdit.MergeNodes(crlTargets=[Part(1, 2)])

edges = Assemble.SeparateFaces.Shell(iType=1,
                                    crlEntity=[Part(1, 2)])
JPT.Debugger(edges)
```
