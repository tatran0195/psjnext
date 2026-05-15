---
title: "ContactTable _Advc()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create contact for advc by table.

## Syntax

```psj
ContactTable _Advc(TCONTACTTABLEDATA _ADVC[] taContactFound _ADVC, cursor[] taContactFound _ADVC)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. TCONTACTTABLEDATA\_ADVC\[]

List of contact setting.

<!-- @since:5.1.0 -->
### 2. Cursor\[]

List of group from where remove contact.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ContactTable _Advc([("Cube _2-G0002 _Cube _1-G0001", "Cube _2", "Cube _1", [6:49], [6:24], 1, 0:0, (0, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 0, 0, 1.79769e+308, 0, 0, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 0, 0, 0, 1, 0, 0, [1, 2, 0, 0], 0, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 2, 0, 0, [1, 2, 0, 0], 0), [], 65280, 0), ("Cube _3-G0004 _Cube _2-G0003", "Cube _3", "Cube _2", [6:75], [6:50], 1, 0:0, (0, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 0, 0, 1.79769e+308, 0, 0, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 0, 0, 0, 1, 0, 0, [1, 2, 0, 0], 0, 0, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 1.79769e+308, 1.79769e+308, 2, 0, 0, [1, 2, 0, 0], 0), [], 65280, 0)], [])
```
