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

<!-- @since:5.0.1 @optional -->
### listEricontEndProp

- Specify the ericont end property.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listEricontOriVecProp

- Specify the ericont ori vector property.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listCidProp

- Specify the cid property.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listEricontDamperLocProp

- Specify the ericont damper location property.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listOcidProp

- Specify the ocid property.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listDamperOffsetVecs

- Specify the damper offset vecs.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### listEricontNodeidProp

- Specify the ericont nodeid property.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.ElemRelatedInfo.Conn(listEricontEndProp=[], listEricontOriVecProp=[], listCidProp=[], listEricontDamperLocProp=[], listOcidProp=[], listDamperOffsetVecs=[], listEricontNodeidProp=[])
```
