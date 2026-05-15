---
title: "Lbc _Bolt _Modeling _Type _D()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Lbc TypeD Bolt

## Syntax

```psj
Lbc _Bolt _Modeling _Type _D(cursor[] taEdgeTop, cursor[] taEdgeBot, string strMPCName, double dConnRadius, double dPlaneTol)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target top part edge cursor(\[5:Edge ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target bottom part edge cursor(\[5:Edge ID])

<!-- @since:5.0.1 -->
### 3. String

MPC name

<!-- @since:5.0.1 -->
### 4. Double

Connection Radius

<!-- @since:5.0.1 -->
### 5. Double

Plane Tolerance

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Lbc _Bolt _Modeling _Type _D([5:1], [5:7], "MPC", 5e-15, 2.42929e-08)
```
