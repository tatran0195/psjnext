---
title: "MuxWeld.Prop3DWeldBead()"
description: "create Property 3D Weld Bead"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MuxWeld > Prop3DWeldBead"
---

## Description

Create Property 3D Weld Bead

## Syntax

```psj
MuxWeld.Prop3DWeldBead(strName="Bead_1", crMaterial=None, crlTargets=[], crEdit=None)
```

## Inputs

### `strName` @type(String) @default("Bead\_1")

- The name.

### `crMaterial` @type(Cursor) @default(None)

- The material.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.Prop3DWeldBead(strName="Bead_1", crMaterial=None, crlTargets=[], crEdit=None)
```
