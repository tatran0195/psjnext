---
title: "Mpc()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create mpc connection

## Syntax

```psj
Mpc(int method, String name, Cursor[] master, Cursor[] slave, MPCTermAttribute[] termAtb,
    double tol, double value, double mpcType, int searchType, int coordId, Cursor editObj)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

method to create mpc,1:2Nodes, 2: 2Edges, 3: 2Faces, 4: Node to Any, 7: Semi Auto, 8: Nodes to Nodes, 9: Node to Edge, 10: Node to Face, 14: Faces to faces, 16: Any Entities

<!-- @since:5.0.1 -->
### 2. String

Name of MPC

<!-- @since:5.0.1 -->
### 3. Cursor\[]

master entities of mpc

<!-- @since:5.0.1 -->
### 4. Cursor\[]

slave entities of mpc

<!-- @since:5.0.1 -->
### 5. MPCTermAttribute\[]

stores attribute for each mpc term, includes coef. and DoF

<!-- @since:5.0.1 -->
### 6. Double

tolerance to find node pair

<!-- @since:5.0.1 -->
### 7. Double

constant value for equation mpc

<!-- @since:5.0.1 -->
### 8. Int

mpc type, 0:General, 1: equation

<!-- @since:5.0.1 -->
### 9. Int

mode to find node pair between master and slave, 0: free, 1: 1 to 1

<!-- @since:5.0.1 -->
### 10. Int

id of referred coordinate system

<!-- @since:5.0.1 -->
### 11. Cursor

used for edit mode

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Mpc(1, "MPC _1", [10:10546], [10:483], [(2, 1), (0, 2), (0, 4), (0, 0), (0, 0), (0, 0)], 0, 0, 0, 1, 0, 0:0)
```
