---
title: "JPT.GetOpnList()"
description: "Get a list of string stores name of functions having their own GUI"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get a _List of String_ stores name of functions having their own GUI.

## Syntax

```psj
JPT.GetOpnList()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[StringVector](../data-type/psj-utility/pre-utility/built-in-types/StringVector)_ specifying the functions having their own GUI.

## Sample Code

```psj {2}
# Get all the functions having their own GUI
allFuncsWithGUI = JPT.GetOpnList()
JPT.Debugger(allFuncsWithGUI)
JPT.Debugger(allFuncsWithGUI[3])
```
