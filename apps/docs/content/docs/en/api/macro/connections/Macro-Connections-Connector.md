---
title: "Connector()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create a connector

## Syntax

```psj
Connector(string nameConnector, int iMethod, int iConnectType, int ReferenceNode,
    int ElementCS, Cursor LocalCS, Cursor[] Elasticity, Cursor[] Damping,
    Cursor[] MasterTarget, Cursor[] SlaveTarget, Cursor Edit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

name of connector

<!-- @since:5.0.1 -->
### 2. int

Method \[1: NODE\_TO\_NODE;2:EDGE\_TO\_EDGE;3:FACE\_TO\_FACE]

<!-- @since:5.0.1 -->
### 3. int

Connection type \[0:PARALLEL; 1:TRANSLATION; 2:ROTATION; 3:BUSHING; 4:CYLINDRICAL; 5:JOINT; 6:RIGIDROD; 7:RIGIDBAR]

<!-- @since:5.0.1 -->
### 4. int

Reference node

<!-- @since:5.0.1 -->
### 5. int

Element coordinate system \[0-no; 1-yes]

<!-- @since:5.0.1 -->
### 6. Cursor

Local Coordinate System

<!-- @since:5.0.1 -->
### 7. Cursor\[]

Elasticity

<!-- @since:5.0.1 -->
### 8. Cursor\[]

Damping

<!-- @since:5.0.1 -->
### 9. Cursor\[]

Master targets

<!-- @since:5.0.1 -->
### 10. Cursor\[]

Slave targets

<!-- @since:5.0.1 -->
### 11. Cursor

Edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Connector("Connector _1", 1, 1, 0, 0, 0:0, [0:0, 0:0, 0:0, 0:0, 0:0, 0:0],
    [0:0, 0:0, 0:0, 0:0, 0:0, 0:0], [10:1], [10:2], 0:0)
```
