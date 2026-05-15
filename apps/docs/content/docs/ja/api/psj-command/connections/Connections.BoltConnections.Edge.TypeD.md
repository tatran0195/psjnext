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

<!-- @since:5.0.1 @required -->
### crlEdgeCur1

- Specify the edge cur1.

<!-- @since:5.0.1 @required -->
### crlEdgeCur2

- Specify the edge cur2.

<!-- @since:5.0.1 @optional -->
### strMpcName

- Specify the mpc name.
- The default value is "MPC".

<!-- @since:5.0.1 @optional -->
### dConnRadius

- Specify the conn radius.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dPlaneTol

- Specify the plane tolerance.
- The default value is 20.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltConnections.Edge.TypeD(crlEdgeCur1, crlEdgeCur2, strMpcName="MPC", dConnRadius=0.0, dPlaneTol=20.0)
```
