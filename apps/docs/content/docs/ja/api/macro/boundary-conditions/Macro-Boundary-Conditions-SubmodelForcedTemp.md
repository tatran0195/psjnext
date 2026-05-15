---
title: "SubmodelForcedTemp()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create sub model forced temperature

## Syntax

```psj
SubmodelForcedTemp(string m _strName,int iSolver,String strFilePathName,int iProcessNo,
    int iReferType,double dExtensionRange,double dExtensionTol,double dExtensionLimitTol,
    string strGlobalElementSet,int iUseBucket,int iNumBucketMaxX,int iNumBucketMaxY,
    int iNumBucketMaxZ,int iPrevBc,Cursor[] m _taTarget,Cursor m _crEdit)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

name of sub model forced temperature

<!-- @since:5.0.1 -->
### 2. Int

Solver \[0:ADVC]

<!-- @since:5.0.1 -->
### 3. String

file path

<!-- @since:5.0.1 -->
### 4. Int

process number

<!-- @since:5.0.1 -->
### 5. Int

refer type\[0:blank; 1:result; 2:restart]

<!-- @since:5.0.1 -->
### 6. Double

extension\_range

<!-- @since:5.0.1 -->
### 7. Double

extension\_tol

<!-- @since:5.0.1 -->
### 8. Double

extension\_limit\_tol

<!-- @since:5.0.1 -->
### 9. String

global\_element\_set

<!-- @since:5.0.1 -->
### 10. Int

use\_bucket\[0:blank; 1:Yes; 2:No]

<!-- @since:5.0.1 -->
### 11. Int

num\_bucket\_max\_x

<!-- @since:5.0.1 -->
### 12. Int

num\_bucket\_max\_y

<!-- @since:5.0.1 -->
### 13. Int

num\_bucket\_max\_z

<!-- @since:5.0.1 -->
### 14. Int

prev\_bc\[0:blank; 1:default hold]

<!-- @since:5.0.1 -->
### 15. Cursor\[]

targets

<!-- @since:5.0.1 -->
### 16. Cursor

edit cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SubmodelForcedTemp("SubmodelForcedTemperature1", 0, "D:/test", 0, -1,1.79769e+308, 1.79769e+308,
    1.79769e+308, "", -1, 2147483647, 2147483647, 2147483647, -1, [6:26], 0:0)
```
