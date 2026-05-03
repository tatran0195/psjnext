---
title: "Connections.BoltConnections.Edge.TypeD()"
description: "Create Lbc TypeD Bolt Edge method"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > BoltConnections > Edge > TypeD"
---

## Description

Create Lbc TypeD Bolt Edge method.

## Syntax

```psj
Connections.BoltConnections.Edge.TypeD(...)
```

## Inputs

### `crlEdgeCur1` @type(List\[Cursor]) @required

- The edge cur1.

### `crlEdgeCur2` @type(List\[Cursor]) @required

- The edge cur2.

### `strMpcName` @type(String) @default("MPC")

- The mpc name.

### `dConnRadius` @type(Double) @default(0.0)

- The conn radius.

### `dPlaneTol` @type(Double) @default(20.0)

- The plane tolerance.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltConnections.Edge.TypeD(crlEdgeCur1, crlEdgeCur2, strMpcName="MPC", dConnRadius=0.0, dPlaneTol=20.0)
```
