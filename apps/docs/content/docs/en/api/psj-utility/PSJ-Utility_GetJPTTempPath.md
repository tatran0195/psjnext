---
title: "JPT.GetJPTTempPath()"
description: "Get the path to the temporary folder of the current Jupiter program"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the path to the temporary folder of the current Jupiter program.

## Syntax

```psj
JPT.GetJPTTempPath()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _String_ specifying the path to the current Jupiter temporary folder.

## Sample Code

```psj {2}
# Get the current Jupiter temporary folder
path = JPT.GetJPTTempPath()
JPT.Debugger(path)
```
