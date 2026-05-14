---
title: "JPT.GetAppPathInfo()"
description: "Get all the working path of the current Jupiter program"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get all the working path of the current Jupiter program.

## Syntax

```psj
JPT.GetAppPathInfo(PathType)
```

## Inputs

<!-- @since:5.0.1 @type:PathType @required -->
### `PathType`

- The _[PathType](../data-type/psj-utility/pre-utility/enumeration-types/path-types)_ describing the type of paths which are available for using.

## Return Code

A _String_ specifying the path relating to the inputted _[PathType](../data-type/psj-utility/pre-utility/enumeration-types/path-types)_.

## Sample Code

```psj {2}
# Path to the installation folder
print(JPT.GetAppPathInfo(JPT.PathType.PROGRAM _PATH))
```
