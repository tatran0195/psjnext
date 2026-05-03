---
title: "Connections.BarBeam()"
description: "Create Connections Bar or Beam"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > BarBeam"
---

## Description

Create Connections Bar or Beam.

## Syntax

```psj
Connections.BarBeam(...)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `iEType` @type(Integer) @default(10)

- The e type.

### `iMethod` @type(Integer) @default(1)

- The method.

### `crProp` @type(Cursor) @default(None)

- The property.

### `dlOrient` @type(Double List) @default(\[])

- The orient.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[])

- The slave target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BarBeam(strName, iEType=10, iMethod=1, crProp=None, dlOrient=[], crlMasterTargets=[], crlSlaveTargets=[])
```
