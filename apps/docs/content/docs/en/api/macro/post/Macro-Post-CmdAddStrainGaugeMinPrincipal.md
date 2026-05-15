---
title: "CmdAddStrainGaugeMinPrincipal()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute Strain Gauge - Min principal.

## Syntax

```psj
CmdAddStrainGaugeMinPrincipal(int[] nodes, double Width, double Height, double AmendFactor, string GaugeName)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int\[]

Target nodes.

<!-- @since:5.0.1 -->
### 2. double

Gauge Width.

<!-- @since:5.0.1 -->
### 3. double

Gauge Height.

<!-- @since:5.0.1 -->

#### 4. double

Amend Factor.

<!-- @since:5.0.1 -->

#### 5. string

Gauge name.

## Return Code

Nothing.

## Sample Code

```psj
CmdAddStrainGaugeMinPrincipal([9428], 0, 0, 1, "")
```
