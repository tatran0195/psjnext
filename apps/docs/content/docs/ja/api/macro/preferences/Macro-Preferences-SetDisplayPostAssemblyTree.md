---
title: "SetDisplayPostAssemblyTree()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Enalble/disable calculating the Tresca Stress automatically when the result file is opened.

## Syntax

```psj
SetDisplayPostAssemblyTree(bool UseTrescaStress)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. bool

- "1": Enable saving load with Tresca Stress calculation
- "0": Disable saving load with Tresca Stress calculation

## Return Code

No return code.

## Sample Code

```psj
SetDisplayPostAssemblyTree(0)
```
