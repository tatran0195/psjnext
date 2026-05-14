---
title: "MuxWeld.Prop3DWeldBead()"
description: "create Property 3D Weld Bead"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MuxWeld > Prop3DWeldBead"
---

## Description

Create Property 3D Weld Bead

## Syntax

```psj
MuxWeld.Prop3DWeldBead(strName="Bead _1", crMaterial=None, crlTargets=[], crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"Bead _1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMaterial`

- The material.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.Prop3DWeldBead(strName="Bead _1", crMaterial=None, crlTargets=[], crEdit=None)
```
