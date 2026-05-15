---
title: "Tools.ToPost()"
description: "Convert the model's data and from an opening Pre document to a new Post document enables to add result to the model."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > ToPost"
macro _link: ""
---

## Description

Convert the model's data and from an opening Pre document to a new Post document enables to add result to the model.

## Syntax

```psj
Tools.ToPost(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strName

- Specify the name of Post document will be converted.

<!-- @since:5.1.0 @optional -->
### ilOptions

- Specify the related settings will be converted with model.
  - 0: Group
  - 1: LBC
  - 2: Connection
  - 3: Coordinate
  - 4: Property
- The default value is \[].

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
