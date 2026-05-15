---
title: "AdvcEigenProcess()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create ADVC eigen value process

## Syntax

```psj
AdvcEigenProcess(string m _strName,bool m _bEigenValue,int number _of _modes,
    int eigenvec _norm,double shift,double cgcgpi _tol,double cgcgpi _eig _tol,
    int cgcgpi _loop _max,double cgcgpi _inner _tol,int cgcgpi _block _size,
    int cgcgpi _extra _mode,Cursor m _crEdit,list m _LoadNodeList,
    list m _LoadCaseNodeList,list m _LoadNodeContactList,list m _OutputParamList,
    int m _iRefType,string m _strRefPath,list m _ReferenceResultList)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Name of ADVC eigen value process

<!-- @since:5.0.1 -->
### 2. Bool

If eigen value parameter defined

<!-- @since:5.0.1 -->
### 3. Int

Number of modes

<!-- @since:5.0.1 -->
### 4. Int

Eigenvec\_norm\[-1:default; 0:mass; 1:max; 2:unity]

<!-- @since:5.0.1 -->
### 5. Double

Shift

<!-- @since:5.0.1 -->
### 6. Double

cgcgpi\_tol

<!-- @since:5.0.1 -->
### 7. Double

cgcgpi\_eig\_tol

<!-- @since:5.0.1 -->
### 8. Int

cgcgpi\_loop\_max

<!-- @since:5.0.1 -->
### 9. Double

cgcgpi\_inner\_tol

<!-- @since:5.0.1 -->
### 10. Int

cgcgpi\_block\_size

<!-- @since:5.0.1 -->
### 11. Int

cgcgpi\_extra\_mode

<!-- @since:5.0.1 -->
### 12. Cursor

edit cursor

<!-- @since:5.0.1 -->
### 13. List

status of Loads

<!-- @since:5.0.1 -->
### 14. List

status of Load Cases

<!-- @since:5.0.1 -->
### 15. List

status and other data of Contacts

<!-- @since:5.0.1 -->
### 16. List

output parameters

<!-- @since:5.0.1 -->
### 17. Int

reference result type\[0:Temperature Load; 1:Stress]

<!-- @since:5.0.1 -->
### 18. String

path of reference result

<!-- @since:5.0.1 -->
### 19. List

data of reference result

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
AdvcEigenProcess("Test",1,1,1,0.001,0.001,0.001,1,0.001,1,1,1:11,,,,,1,"Test",)
```
