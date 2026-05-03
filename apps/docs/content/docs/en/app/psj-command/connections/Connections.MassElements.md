---
title: "Connections.MassElements()"
description: "Connection new mass"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > MassElements"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Connection new mass

## Syntax

```psj
Connections.MassElements(...)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `crlTargets` @type(List\[Cursor]) @required

- The target.

### `dMass` @type(Double) @default(0.01)

- The mass.

### `iDof` @type(Integer) @default(1)

- The dof.

### `bDesigner` @type(Boolean) @default(True)

- For license switcher. If true, it is used in Designer.

### `crCoordinate` @type(Cursor) @default(None)

- The coordinate.

### `dOffset0` @type(Double) @default(0.0)

- The offset0.

### `dOffset1` @type(Double) @default(0.0)

- The offset1.

### `dOffset2` @type(Double) @default(0.0)

- The offset2.

### `dInertia0` @type(Double) @default(0.0)

- The inertia0.

### `dInertia1` @type(Double) @default(0.0)

- The inertia1.

### `dInertia2` @type(Double) @default(0.0)

- The inertia2.

### `dInertia3` @type(Double) @default(0.0)

- The inertia3.

### `dInertia4` @type(Double) @default(0.0)

- The inertia4.

### `dInertia5` @type(Double) @default(0.0)

- The inertia5.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `bUpdateDispCS` @type(Boolean) @default(True)

- The update displacement coordinate system.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2-5}
Geometry.Part.Cube()
Connections.MassElements(strName="Mass1", crlTargets=[Node(5)], dMass=0.01, iDof=1, bDesigner=True, 
                        crCoordinate=None, dOffset0=0.0, dOffset1=0.0, dOffset2=0.0, dInertia0=0.0, 
                        dInertia1=0.0, dInertia2=0.0, dInertia3=0.0, dInertia4=0.0, dInertia5=0.0, 
                        crEdit=None, bUpdateDispCS=True)
```
