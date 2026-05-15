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

<!-- @since:5.1.0 @optional -->
### listERIBushData

- Specify the element related information of bush.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEricontEndProp

- Specify the ericont end property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEricontOriVecProp

- Specify the ericont ori vector property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listCidProp

- Specify the cid property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEricontDamperLocProp

- Specify the ericont damper location property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listOcidProp

- Specify the ocid property.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listDamperOffsetVecs

- Specify the damper offset vecs.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### listEricontNodeidProp

- Specify the ericont nodeid property.
- The default value is \[].

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
