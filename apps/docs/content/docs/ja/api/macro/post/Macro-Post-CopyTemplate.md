---
title: "CopyTemplate()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Copy specified template.

## Syntax

```psj
CopyTemplate(string CurrentName, string NewTemplate)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Copy source template's name.

<!-- @since:5.0.1 -->
### 2. string

Copied templates' name.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
CopyTemplate("Current Template","New Template")
```
