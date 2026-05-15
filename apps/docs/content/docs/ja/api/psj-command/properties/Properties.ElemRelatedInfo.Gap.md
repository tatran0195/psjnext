---
title: "Properties.ElemRelatedInfo.Gap()"
description: "Modify information such as direction vectors and end releases for the selected gap elements, individually"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > ElemRelatedInfo > Gap"
---

## Description

Modify information such as direction vectors and end releases for the selected gap elements, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Gap(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### listERIGapData

- Specify the element related information of gap.
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

```psj {8-14}
Geometry.Part.Cube(iPartColor=6409934)
Connections.Gaps.TwoNodes(
    crlMaster=[Node(6)], 
    crlSlave=[Node(8)], 
    iOriMode=1, 
    strName="GAP _1", 
    dlOriVec=[0.0, 0.0, 0.0])
ret = Properties.ElemRelatedInfo.Gap(
        listERIGapData=[
            ERIGAP _DATA(
                iElemId=1090, 
                iEndA=6, 
                iEndB=8, 
                dlOrientVec=[0.0, 1.0, 0.0])])
print(ret)
```
