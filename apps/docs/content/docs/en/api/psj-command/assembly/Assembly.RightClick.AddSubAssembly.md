---
title: "Assembly.RightClick.AddSubAssembly()"
description: "Add a new assembly (Sub-assembly) to the selected assembly"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assembly > Right Click > Add Subassembly"
---

## Description

Add a new assembly (Sub-assembly) to the selected assembly.

## Syntax

```psj
Assembly.RightClick.AddSubAssembly(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crInst`

- The instance inwhich the new subassembly will be added.

## Return Code

A _Cursor_ specifying the created sub-assembly.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

Assembly.RightClick.AddSubAssembly()
created _sub _assem = Assembly.RightClick.AddSubAssembly(crInst=Inst(1))

JPT.Debugger(created _sub _assem)
```
