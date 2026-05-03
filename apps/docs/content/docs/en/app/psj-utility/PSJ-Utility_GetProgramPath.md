---
title: "JPT.GetProgramPath()"
description: "Get the path to the current Jupiter installation folder"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get the path to the current Jupiter installation folder.

## Syntax

```psj
JPT.GetProgramPath()
```

## Inputs

This utility function does not require any input value.

## Return Code

The path to the current Jupiter installation folder.

## Sample Code

```psj {2}
# Get the current Jupiter installation folder
path = JPT.GetProgramPath()
JPT.Debugger(path)
```
