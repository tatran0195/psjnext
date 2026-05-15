---
title: "JPT.GetScreenHeight()"
description: "Get the height of screen window."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get the height of screen window.

## Syntax

```psj
JPT.GetScreenHeight()
```

## Inputs

This utility function does not require any input value.

## Return Code

An _Integer_ specifying the height value of Main Window.

## Sample Code

```psj {1}
height=JPT.GetScreenHeight()
JPT.Debugger(height)
```
