---
title: "Assembly.RightClick.AddSubAssembly()"
description: "Add a new assembly (Sub-assembly) to the selected assembly"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assembly > Right Click > Add Subassembly"
---

## Description

Add a new assembly (Sub-assembly) to the selected assembly.

## Syntax

```psj
Assembly.RightClick.AddSubAssembly(...)
```

## Inputs

### `crInst` @type(Cursor) @default(None)

- The instance inwhich the new subassembly will be added.

## Return Code

A _Cursor_ specifying the created sub-assembly.

## Sample Code

```psj {3,4}
Geometry.Part.Cube()

Assembly.RightClick.AddSubAssembly()
created_sub_assem = Assembly.RightClick.AddSubAssembly(crInst=Inst(1))

JPT.Debugger(created_sub_assem)
```
