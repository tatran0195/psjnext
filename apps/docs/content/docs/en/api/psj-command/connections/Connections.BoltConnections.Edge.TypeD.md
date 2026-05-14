---
title: "Connections.BoltConnections.Edge.TypeD()"
description: "Create Lbc TypeD Bolt Edge method"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > BoltConnections > Edge > TypeD"
---

## Description

Create Lbc TypeD Bolt Edge method.

## Syntax

```psj
Connections.BoltConnections.Edge.TypeD(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdgeCur1`

- The edge cur1.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlEdgeCur2`

- The edge cur2.

<!-- @since:5.0.1 @type:String @optional @default:"MPC" -->
### `strMpcName`

- The mpc name.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dConnRadius`

- The conn radius.

<!-- @since:5.0.1 @type:Double @optional @default:20.0 -->
### `dPlaneTol`

- The plane tolerance.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltConnections.Edge.TypeD(crlEdgeCur1, crlEdgeCur2, strMpcName="MPC", dConnRadius=0.0, dPlaneTol=20.0)
```
