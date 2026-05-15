---
title: "EditUserProperty()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Edit existing User Property in Assemble Tree.

## Syntax

```psj
EditUserProperty(string name, string[] values)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

The Name of user property to edit.

<!-- @since:5.1.0 -->
### 2. string\[]

The values corresponding to the properties  inside the newly created user property.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
EditUserProperty("Name", ["1.0", "2.0", "3.0"])
```
