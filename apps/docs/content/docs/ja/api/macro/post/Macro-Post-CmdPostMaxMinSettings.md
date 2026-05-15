---
title: "CmdPostMaxMinSettings()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Max Min setting.

## Syntax

```psj
CmdPostMaxMinSettings(int GroupMethod, color Max, color Min, color Text)
```

<!-- @since:5.0.1 -->
### 1. int

Group method. 0: Whole model, 1: By parts.

<!-- @since:5.0.1 -->
### 2. color

Max color.

<!-- @since:5.0.1 -->
### 3. color

Min color.

<!-- @since:5.0.1 -->
### 4. color

Text color.

## Inputs

Nothing.

## Return Code

Nothing.

## Sample Code

```psj
CmdPostMaxMinSettings(0, 255, 16711680, 65535)
```
