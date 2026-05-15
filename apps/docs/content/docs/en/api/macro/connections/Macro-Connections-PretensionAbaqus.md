---
title: "PretensionAbaqus()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Pretension Abaqus

## Syntax

```psj
PretensionAbaqus(string strName, bool bFixedLength, cursor crTable, double dValue,
    int iLocalUnit, string stNormal, double[3] dNodePos, cursor crEdit, cursor[] taTarget)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Pretension abaqus name

<!-- @since:5.0.1 -->
### 2. Bool

Bolt FixLength bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 3. Cursor

Table cursor

<!-- @since:5.0.1 -->
### 4. Double

Pretension\_1 force value

<!-- @since:5.0.1 -->
### 5. Int

Input Unit

- 0: N
- 1: MN
- 2: kgf
- 3: Lbf
- 4: Tf

<!-- @since:5.0.1 -->
### 6. String

String normal

<!-- @since:5.0.1 -->
### 7. Double\[3]

Coordinate of the control node

<!-- @since:5.0.1 -->
### 8. Cursor

Edit cursor

<!-- @since:5.0.1 -->
### 9. Cursor\[]

Target entities cursor: Face/1D Element

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PretensionAbaqus("PreTensionAbaqus1", 1, 0:0, 100, 0, "1,0,0", [0.0083333, 0.015556, 0.025], 0:0, [6:180])
```
