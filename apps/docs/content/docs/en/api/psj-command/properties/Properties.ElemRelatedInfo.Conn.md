---
title: "Properties.ElemRelatedInfo.Conn()"
description: "Set Shell Parameter"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > ElemRelatedInfo > Conn"
---

## Description

Set Shell Parameter

## Syntax

```psj
Properties.ElemRelatedInfo.Conn(listEricontEndProp=[], listEricontOriVecProp=[], listCidProp=[], listEricontDamperLocProp=[], listOcidProp=[], listDamperOffsetVecs=[], listEricontNodeidProp=[])
```

## Inputs

<!-- @since:5.0.1 @type:ERICONT _END _PROP List @optional @default:[] -->
### `listEricontEndProp`

- The ericont end property.

<!-- @since:5.0.1 @type:ERICONT _ORI _VEC _PROP List @optional @default:[] -->
### `listEricontOriVecProp`

- The ericont ori vector property.

<!-- @since:5.0.1 @type:CID _PROP List @optional @default:[] -->
### `listCidProp`

- The cid property.

<!-- @since:5.0.1 @type:ERICONT _DAMPER _LOC _PROP List @optional @default:[] -->
### `listEricontDamperLocProp`

- The ericont damper location property.

<!-- @since:5.0.1 @type:OCID _PROP List @optional @default:[] -->
### `listOcidProp`

- The ocid property.

<!-- @since:5.0.1 @type:DAMPER _OFFSET _VECS List @optional @default:[] -->
### `listDamperOffsetVecs`

- The damper offset vecs.

<!-- @since:5.0.1 @type:ERICONT _NODEID _PROP List @optional @default:[] -->
### `listEricontNodeidProp`

- The ericont nodeid property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.ElemRelatedInfo.Conn(listEricontEndProp=[], listEricontOriVecProp=[], listCidProp=[], listEricontDamperLocProp=[], listOcidProp=[], listDamperOffsetVecs=[], listEricontNodeidProp=[])
```
