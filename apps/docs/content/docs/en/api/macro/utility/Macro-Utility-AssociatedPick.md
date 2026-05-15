---
title: "AssociatedPick()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute of Associated Pick

## Syntax

```psj
AssociatedPick(Cursor[] tacursor,String str2,String str3)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target cursors

<!-- @since:5.0.1 -->
### 2. String

Target Entity Name(BarBody,Part,Face,Edge,Elem,SolidElem,Node,CornerNode,MidNodes,MidNodesNoBoundary,Connection,Mass,Contact)

<!-- @since:5.0.1 -->
### 3. String

Use only str2=Connection.(UNKNOWN,MPC,RBE2,RBE3,SPRING,MASS,BOLT,CONM,PROD,RBAR,BARBEAM,BUSH,MOMENT,GAP,WELD,DAMPER)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AssociatedPick([6:26], "Node", "UNKNOWN")
```
