---
title: "MMCCarACTools.ClearanceElement.Connect()"
description: "MMCCarACTools ClearanceElement Connect"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MMCCarACTools > ClearanceElement > Connect"
---

## Description

MMCCarACTools ClearanceElement Connect

## Syntax

```psj
MMCCarACTools.ClearanceElement.Connect(crlFaces, crlElems, iConnectionMethod)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the face.

<!-- @since:5.0.1 @required -->
### crlElems

- Specify the element.

<!-- @since:5.0.1 @required -->
### iConnectionMethod

- Specify the connection method.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MMCCarACTools.ClearanceElement.Connect(crlFaces, crlElems, iConnectionMethod)
```
