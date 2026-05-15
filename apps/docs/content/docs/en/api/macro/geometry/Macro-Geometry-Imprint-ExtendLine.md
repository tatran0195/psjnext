---
title: "Imprint _ExtendLine()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create imprint Extend line

## Syntax

```psj
Imprint _ExtendLine(int Edge _ID,int Method _Type,int Position _Type,bool Break _Face ,Cursor[] bodyCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int

Edge ID

<!-- @since:5.0.1 -->
### 2. Int

Method Type 0=Straight,1=Same Curvature

<!-- @since:5.0.1 -->
### 3. Int

Position Type 0=Nearest Edge,1=Boundary Edge

<!-- @since:5.0.1 -->
### 4. Bool

Flag true = 1,false=0

<!-- @since:5.0.1 -->
### 5. Cursor\[]

Body Cursor(\[3:\*]\*=Body ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Imprint _ExtendLine(27, 0, 0, 1, [3:1])
```
