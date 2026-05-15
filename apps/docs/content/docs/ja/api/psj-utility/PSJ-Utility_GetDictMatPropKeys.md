---
title: "JPT.GetDictMatPropKeys()"
description: "Get list keys from dictMatProps"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get list keys from dictMatProps.

## Syntax

```psj
JPT.GetDictMatPropKeys(dictMatProps)
```

## Inputs

<!-- @since:5.1.0 @required -->
### dictMatProps

- Specify the_[dictMatProps](../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_.

## Return Code

A _List of String_ specifying the keys of dictMatProps.

## Sample Code

```psj {11}
# Get 1st material in the library materials
mat0 = JPT.GetAllLibraryMaterials()[0]

# Get & print dicMatProps
dict1 = mat0.dictMatProps
pprint(dict1)
```
