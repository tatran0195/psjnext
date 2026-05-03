---
title: "JPT.GetAppPathInfo()"
description: "Get all the working path of the current Jupiter program"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get all the working path of the current Jupiter program.

## Syntax

```psj
JPT.GetAppPathInfo(PathType)
```

## Inputs

### `PathType` @type(Enum) @required

- Th&#x65;_[PathType](../data-type/psj-utility/pre-utility/enumeration-types/path-types)_&#x64;escribing the type of paths which are available for using.

## Return Code

A _String_ specifying the path relating to the inputted _[PathType](../data-type/psj-utility/pre-utility/enumeration-types/path-types)_.

## Sample Code

```psj {2}
# Path to the installation folder
print(JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH))
```
