---
title: "Home.Synchronize()"
description: "Enable/Disable the synchronize function between documents"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Home > Synchronize"
---

## Description

Enable/Disable the synchronize function between documents.

## Syntax

```psj
Home.Synchronize(...)
```

## Inputs

This function does not contain any input values.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: The windows are synchronized.
- _False_: Synchronizing mode is disabled.

## Sample Code

```psj {1}
synchronize = Home.Synchronize()

JPT.Debugger(synchronize)
```
