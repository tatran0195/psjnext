---
title: "ShowContactDialog()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Show contact dialog.

## Syntax

```psj
ShowContactDialog(int iResultSet, int iTimeStep, string strResultTypeName, string strResultCompName, int iResultPosition)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

Result set.

<!-- @since:5.1.0 -->
### 2. int

Time step.

<!-- @since:5.1.0 -->
### 3. string

Name of result type.

<!-- @since:5.1.0 -->
### 4. string

Name of component.

<!-- @since:5.1.0 -->
### 5. int

Data Location.

## Return Code

Nothing.

## Sample Code

```psj
ShowContactDialog(1, 0, 0, ContactForceShear, Translational, 1)
```
