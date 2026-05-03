---
title: "JPT.GetDictMatPropKeys()"
description: "Get list keys from dictMatProps"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Get list keys from dictMatProps.

## Syntax

```psj
JPT.GetDictMatPropKeys(dictMatProps)
```

## Inputs

### `dictMatProps` @type(Dictionary) @required

- Th&#x65;_[dictMatProps](../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_.

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
