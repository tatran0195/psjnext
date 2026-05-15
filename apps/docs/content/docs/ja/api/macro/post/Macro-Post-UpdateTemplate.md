---
title: "UpdateTemplate()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Load template to current document.

## Syntax

```psj
UpdateTemplate(string templateName, string comment)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Template name.

<!-- @since:5.0.1 -->
### 2. string

Comment.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
UpdateTemplate("My Template", "Comment")
```
