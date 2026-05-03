---
title: "Properties.Property1DBeamSimple()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Property1DBeamSimple"
macro_link: "[Property1DBeamSimple](../../macro/properties/Property1DBeamSimple)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description is missing in all versions — placeholder inserted
-->

## Description

## Syntax

```psj
Properties.Property1DBeamSimple(strName, iId, crSection=None, crMat=None, vecOrient=[DFLT_DBL,DFLT_DBL,DFLT_DBL], crlTargets=[], crEdit=None)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `iId` @type(Integer) @required

- The ID.

### `crSection` @type(Cursor) @default(None)

- The section.

### `crMat` @type(Cursor) @default(None)

- The material.

### `vecOrient` @type(Vector) @default(\[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL])

- The orient.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Property1DBeamSimple(strName, iId, crSection=None, crMat=None, vecOrient=[DFLT_DBL,DFLT_DBL,DFLT_DBL], crlTargets=[], crEdit=None)
```
