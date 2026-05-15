---
title: "ElemRelatedInfo _Conn()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set Bush/Gap Parameter

## Syntax

```psj
ElemRelatedInfo _Conn(ERIConn _Ends[] ends, ERIConn _orientVec[] orientVec,
    ERIConn _cid[] CID, ERIConn _damperLoc[] damperLocs, ERIConn _ocid[] ocids,
    ERIConn _damperOffsetVec[] damperOffsetVecs, ERIConn _nodeId[] nodeIds)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. ERIConn\_Ends\[]

ERIConn\_end list

<!-- @since:5.0.1 -->
### 2. ERIConn\_orientVec\[]

ERIConn\_orientVec list

<!-- @since:5.0.1 -->
### 3. ERIConn\_cid\[]

ERIConn\_CID list

<!-- @since:5.0.1 -->
### 4. ERIConn\_damperLoc\[]

ERIConn\_damperLoc list

<!-- @since:5.0.1 -->
### 5. ERIConn\_ocid\[]

ERIConn\_ocid list

<!-- @since:5.0.1 -->
### 6. ERIConn\_damperOffsetVec\[]

ERIConn\_damperOffsetVec list

<!-- @since:5.0.1 -->
### 7. ERIConn\_nodeId\[]

ERIConn\_nodeId list

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ElemRelatedInfo _Conn([[267, 14, 1]], [[267, 1, 0, 0]], [[267, 1]], [[267, 0.001]],
    [[267, 1]], [[267, 0, 0, 0.001]])
```
