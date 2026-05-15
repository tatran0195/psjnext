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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "Bead\_1".

<!-- @since:5.0.1 @optional -->
### crMaterial

- Specify the material.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MuxWeld.Prop3DWeldBead(strName="Bead _1", crMaterial=None, crlTargets=[], crEdit=None)
```
