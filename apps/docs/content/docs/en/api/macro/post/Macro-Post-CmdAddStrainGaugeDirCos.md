---
title: "CmdAddStrainGaugeDirCos()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute Strain Gauge - Direction Cosine.

## Syntax

```psj
CmdAddStrainGaugeDirCos(int[] nodes, vector DirInput, double Width, double Height, double AmendFactor, string GaugeName)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. int\[]

Target nodes.

<!-- @since:5.0.1 -->
### 2. vector

Direction vector x, y, z.

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
CmdAddStrainGaugeDirCos([8475], [0, 0, 1], 0.003, 0.003, 1, "")
```
