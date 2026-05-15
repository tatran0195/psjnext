---
title: "CmdAddStrainGauge2Nodes()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute Strain Gauge - 2 Nodes.

## Syntax

```psj
CmdAddStrainGauge2Nodes(int node1, int node2, double Width, double Height, double AmendFactor, string GaugeName)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int

Target node1.

<!-- @since:5.0.1 -->
### 2. int

Target node2.

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
CmdAddStrainGauge2Nodes(8365, 8608, 0.005, 0.005, 1, "")
```
