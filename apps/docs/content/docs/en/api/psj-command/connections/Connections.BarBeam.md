---
title: "Connections.BarBeam()"
description: "Create Connections Bar or Beam"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > BarBeam"
---

## Description

Create Connections Bar or Beam.

## Syntax

```psj
Connections.BarBeam(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:10 -->
### `iEType`

- The e type.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crProp`

- The property.

<!-- @since:5.0.1 @type:Double List @optional @default:[] -->
### `dlOrient`

- The orient.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMasterTargets`

- The master target.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlaveTargets`

- The slave target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BarBeam(strName, iEType=10, iMethod=1, crProp=None, dlOrient=[], crlMasterTargets=[], crlSlaveTargets=[])
```
