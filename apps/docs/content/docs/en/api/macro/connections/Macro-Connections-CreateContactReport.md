---
title: "CreateContactReport()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create a contact check report

## Syntax

```psj
CreateContactReport(string path, double zoomFactor, int fitGroupBy, int listBy, int listOrder, int listFormat)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Exported report file path

<!-- @since:5.0.1 -->
### 2. Double

Zoom factor

<!-- @since:5.0.1 -->
### 3. Int

Fit group by:

- 0: Part
- 1: Face

<!-- @since:5.0.1 -->
### 4. Int

List by:

- 0: Part
- 1: Contact Condition

<!-- @since:5.0.1 -->
### 5. Int

List order:

- 0: Name
- 1: ID

<!-- @since:5.0.1 -->
### 6. Int

List format:

- 0: html
- 1: excel

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateContactReport("D:/contact _report.html", 2, 0, 0, 0, 0)
```
