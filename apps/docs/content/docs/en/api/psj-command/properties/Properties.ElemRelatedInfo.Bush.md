---
title: "Properties.ElemRelatedInfo.Bush()"
description: "Modify information such as direction vectors and end releases for the selected bush elements, individually"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > ElemRelatedInfo > Bush"
---

## Description

Modify information such as direction vectors and end releases for the selected bush elements, individually

## Syntax

```psj
Properties.ElemRelatedInfo.Bush(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[ERIBUSH _DATA class] @optional @default:[] -->
### `listERIBushData`

- The element related information of bush.

<!-- @since:5.0.1 @type:ERICONT _END _PROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEricontEndProp`

- The ericont end property.

<!-- @since:5.0.1 @type:ERICONT _ORI _VEC _PROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEricontOriVecProp`

- The ericont ori vector property.

<!-- @since:5.0.1 @type:CID _PROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listCidProp`

- The cid property.

<!-- @since:5.0.1 @type:ERICONT _DAMPER _LOC _PROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEricontDamperLocProp`

- The ericont damper location property.

<!-- @since:5.0.1 @type:OCID _PROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listOcidProp`

- The ocid property.

<!-- @since:5.0.1 @type:DAMPER _OFFSET _VECS List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listDamperOffsetVecs`

- The damper offset vecs.

<!-- @since:5.0.1 @type:ERICONT _NODEID _PROP List @removed:5.1.0 @optional @deprecated @default:[] -->
### `listEricontNodeidProp`

- The ericont nodeid property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {6-12}
Geometry.Part.Cube(iPartColor=6409934)
Connections.SpringsDampers.Bush.TwoNodes(
    crlMaster=[Node(53)], 
    crlSlave=[Node(61)], 
    iOriMode=1)
ret = Properties.ElemRelatedInfo.Bush(
    listERIBushData=[
        ERIBUSH _DATA(
            iElemId=1089, 
            iEndA=53, 
            iEndB=61, 
            dlOrientVec=[0.0, 1.0, 0.0])])
print(ret)
```
