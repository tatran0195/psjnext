---
title: "JPT.GetScreenWidth()"
description: "Get the width of screen window."
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Get the width of screen window.

## Syntax

```psj
JPT.GetScreenWidth()
```

## Inputs

This utility function does not require any input value.

## Return Code

An _Integer_ specifying the width value of Main Window.

## Sample Code

```psj {1}
width=JPT.GetScreenWidth()
JPT.Debugger(width)
```
