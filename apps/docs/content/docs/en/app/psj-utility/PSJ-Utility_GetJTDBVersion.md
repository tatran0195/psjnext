---
title: "JPT.GetJTDBVersion()"
description: "Get all the version information of the current Jupiter file"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get all the version information of the current Jupiter file.

## Syntax

```psj
JPT.GetJTDBVersion()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[VersionInfo](../data-type/psj-utility/pre-utility/built-in-types/VersionInfo)_ object specifying a _List_ containing the version information of the current Jupiter file, including:

- Build
- Major
- Minor
- Sub

## Sample Code

```psj {2}
# Get the version information of the current Jupiter
version = JPT.GetJTDBVersion()
JPT.Debugger(version)
```
