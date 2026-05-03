---
title: "MMCCarACTools.ClearanceElement.Connect()"
description: "MMCCarACTools ClearanceElement Connect"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MMCCarACTools > ClearanceElement > Connect"
---

## Description

MMCCarACTools ClearanceElement Connect

## Syntax

```psj
MMCCarACTools.ClearanceElement.Connect(crlFaces, crlElems, iConnectionMethod)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `crlElems` @type(List\[Cursor]) @required

- The element.

### `iConnectionMethod` @type(Integer) @required

- The connection method.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MMCCarACTools.ClearanceElement.Connect(crlFaces, crlElems, iConnectionMethod)
```
