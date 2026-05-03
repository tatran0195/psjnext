---
title: "Tools.ToPost()"
description: "Convert the model's data and from an opening Pre document to a new Post document enables to add result to the model."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > ToPost"
macro_link: ""
---

## Description

Convert the model's data and from an opening Pre document to a new Post document enables to add result to the model.

## Syntax

```psj
Tools.ToPost(...)
```

## Inputs

### `strName` @type(String) @required

- The name of Post document will be converted.

### `ilOptions` @type(List\[Integer]) @default(\[])

- The related settings will be converted with model.
  - 0: Group
  - 1: LBC
  - 2: Connection
  - 3: Coordinate
  - 4: Property

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {5}
# Prepare Pre model
Geometry.Part.Cube()

# Convert to Post
Tools.ToPost(strName="Jupiter1", ilOptions=[0, 1, 2, 3, 4])
```
