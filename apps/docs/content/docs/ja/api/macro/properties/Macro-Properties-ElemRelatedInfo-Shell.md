---
title: "ElemRelatedInfo _Shell()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set Shell Parameter

## Syntax

```psj
ElemRelatedInfo _Shell(list[] erishell _data)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. list\[]

list of erishell data

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 1. Int\[]

thetas parameter

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 2. Int\[]

coordinate system parameter

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 3. Int\[]

zoffs parameter

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ElemRelatedInfo _Shell([[117, 2, 1.0472, 2147483647, 1.79769e+308], [117, 2, 1.0472, 2147483647, 1.79769e+308]])
```
