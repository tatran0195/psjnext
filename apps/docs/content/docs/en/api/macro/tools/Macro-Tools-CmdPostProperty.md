---
title: "CmdPostProperty()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Lists all the information in the output for the selected entity.

## Syntax

```psj
CmdPostProperty(cursor Target)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor

A Cursor specifying the target to output the information.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
CmdPostProperty(3:1)
```
