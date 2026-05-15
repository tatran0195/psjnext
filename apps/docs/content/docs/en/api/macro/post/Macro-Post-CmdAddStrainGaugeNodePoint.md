---
title: "CmdAddStrainGaugeNodePoint()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute Strain Gauge - Node-Point.

## Syntax

```psj
CmdAddStrainGaugeNodePoint(int node, vector position, double Width, double Height, double AmendFactor, string GaugeName)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Target node1.

<!-- @since:5.0.1 -->
### 2. vector

position x,y,z.

<!-- @since:5.0.1 -->
### 3. double

Gauge Width.

<!-- @since:5.0.1 -->
### 4. double

Gauge Height.

<!-- @since:5.0.1 -->

#### 5. double

Amend Factor.

<!-- @since:5.0.1 -->

#### 6. string

Gauge name.

## Return Code

Nothing.

## Sample Code

```psj
CmdAddStrainGaugeNodePoint(8647, [-0.00256365, -0.00125307, 0.000465], 5, 5, 1, "")
```
