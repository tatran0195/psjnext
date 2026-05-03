---
title: "Properties.ElemRelatedInfo.Conn()"
description: "Set Shell Parameter"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > ElemRelatedInfo > Conn"
---

## Description

Set Shell Parameter

## Syntax

```psj
Properties.ElemRelatedInfo.Conn(listEricontEndProp=[], listEricontOriVecProp=[], listCidProp=[], listEricontDamperLocProp=[], listOcidProp=[], listDamperOffsetVecs=[], listEricontNodeidProp=[])
```

## Inputs

### `listEricontEndProp` @type(ERICONT\_END\_PROP List) @default(\[])

- The ericont end property.

### `listEricontOriVecProp` @type(ERICONT\_ORI\_VEC\_PROP List) @default(\[])

- The ericont ori vector property.

### `listCidProp` @type(CID\_PROP List) @default(\[])

- The cid property.

### `listEricontDamperLocProp` @type(ERICONT\_DAMPER\_LOC\_PROP List) @default(\[])

- The ericont damper location property.

### `listOcidProp` @type(OCID\_PROP List) @default(\[])

- The ocid property.

### `listDamperOffsetVecs` @type(DAMPER\_OFFSET\_VECS List) @default(\[])

- The damper offset vecs.

### `listEricontNodeidProp` @type(ERICONT\_NODEID\_PROP List) @default(\[])

- The ericont nodeid property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.ElemRelatedInfo.Conn(listEricontEndProp=[], listEricontOriVecProp=[], listCidProp=[], listEricontDamperLocProp=[], listOcidProp=[], listDamperOffsetVecs=[], listEricontNodeidProp=[])
```
