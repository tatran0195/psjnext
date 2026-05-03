---
title: "Connections.CreateConnConm()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > CreateConnConm"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description is missing in all versions — placeholder inserted
-->

## Description

## Syntax

```psj
Connections.CreateConnConm(strName, iEType, iMethod, iCoordSys, iConmId, crMatCoord, dMass, dlX=[0, 0, 0], dlVintertia0=[0, 0, 0], dlVintertia1=[0, 0, 0])
```

## Inputs

### `strName` @type(String) @required

- The name.

### `iEType` @type(Integer) @required

- The e type.

### `iMethod` @type(Integer) @required

- The method.

### `iCoordSys` @type(Integer) @required

- The coordinate system.

### `iConmId` @type(Integer) @required

- The conm ID.

### `crMatCoord` @type(Cursor) @required

- The material coordinate.

### `dMass` @type(Double) @required

- The mass.

### `dlX` @type(Double List) @default(\[0, 0, 0])

- The x.

### `dlVintertia0` @type(Double List) @default(\[0, 0, 0])

- The vintertia0.

### `dlVintertia1` @type(Double List) @default(\[0, 0, 0])

- The vintertia1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.CreateConnConm(strName, iEType, iMethod, iCoordSys, iConmId, crMatCoord, dMass, dlX=[0, 0, 0], dlVintertia0=[0, 0, 0], dlVintertia1=[0, 0, 0])
```
