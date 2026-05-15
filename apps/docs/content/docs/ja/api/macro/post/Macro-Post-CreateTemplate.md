---
title: "CreateTemplate()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create a new template.

## Syntax

```psj
CreateTemplate(string templateName, string comment)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Template name.

<!-- @since:5.0.1 -->
### 2. string

Comment for the template.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
CreateTemplate("New Template", "For my default template.")
```
