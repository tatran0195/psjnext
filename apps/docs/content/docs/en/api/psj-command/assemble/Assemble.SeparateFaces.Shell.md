---
title: "Assemble.SeparateFaces.Shell()"
description: "Separate shared Nodes for Shell that is shared between the shell parts into double nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assemble > Separate Faces > Shell"
---

## Description

Separate shared Nodes for Shell that is shared between the shell parts into double nodes.

## Syntax

```psj
Assemble.SeparateFaces.Shell(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type of entity to be selected.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlEntity`

- The list of target item which will be separated.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCreateGroup`

- The enable/disable create group option.

## Return Code

A _List Cursor_ of separated edges if success, or _None_ if fail.

## Sample Code

```psj {8,9}
Geometry.Part.Cube(strName="Cube _1",
                   iPartColor=7697908)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube _2",
                   iPartColor=7463537)
MeshEdit.MergeNodes(crlTargets=[Part(1, 2)])

edges = Assemble.SeparateFaces.Shell(iType=1,
                                    crlEntity=[Part(1, 2)])
JPT.Debugger(edges)
```
