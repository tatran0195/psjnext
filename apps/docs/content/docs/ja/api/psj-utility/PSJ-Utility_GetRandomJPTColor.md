---
title: "JPT.GetRandomJPTColor()"
description: "Get random color code in Jupiter"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get random color code in Jupiter.

## Syntax

```psj
JPT.GetRandomJPTColor()
```

## Inputs

This utility function does not require any input value.

## Return Code

An _Integer_ specifying a color code in Jupiter.

## Sample Code

```psj {2}
# Get a random color code in Jupiter
color = JPT.GetRandomJPTColor()
JPT.Debugger(color)
```
