---
title: "CreateCustomNote()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Create a custom note or edit an exist custom note.

## Syntax

```psj
CreateCustomNote(string noteName, double[] position, bool createNewCollection, cursor entity, cursor customNoteCollection, string collectionName, string[] content, int fontSize, color fontColor, int bold, color bgColor, int width, color outlineColor, int size, color arrowColor, int type, int alignment, cursor customNote)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

Specifies the name of the custom note.

<!-- @since:5.1.0 -->
### 2. double\[]

Specifies the position of the note by coordinate \[x,y,z].

<!-- @since:5.1.0 -->
### 3. bool

Specifies whether it create a new collection or not.

- 0 : no
- 1 : yes

<!-- @since:5.1.0 -->
### 4. cursor

Specifies the target entity which the custom note is created on. Set 0:0 if no target.

<!-- @since:5.1.0 -->
### 5. cursor

Specifies a custom note collection where the new custom note is append. Set 0:0 if create a new collection.

<!-- @since:5.1.0 -->
### 6. string

Specifies the name of new custom note collection if createNewCollection is 1.

<!-- @since:5.1.0 -->
### 7. string\[]

Describe content in the format of a list of string. When writing multiple lines of content, list multiple strings here.

<!-- @since:5.1.0 -->
### 8. int

Specifies the font size of the text of Content.

<!-- @since:5.1.0 -->
### 9. color

Specifies the color of the text of Content.

<!-- @since:5.1.0 -->
### 10. int

Bold text or not in the Content. Set 1 and bold.

<!-- @since:5.1.0 -->
### 11. color

Specifies the ground color of the creating custom note.

<!-- @since:5.1.0 -->
### 12. int

Specifies the width of the note border.

<!-- @since:5.1.0 -->
### 13. color

Specifies the color of the note border.

<!-- @since:5.1.0 -->
### 14. int

Specifies the thickness of the line extending from the note to the coordinate position. Setting it to 0 hides the line.

<!-- @since:5.1.0 -->
### 15. color

Specifies the color of the line extending from the note to the coordinate position.

<!-- @since:5.1.0 -->
### 16. int

Specifies the shape type that points to the coordinate position.

- 0: "None"
- 1: "Arrow"

<!-- @since:5.1.0 -->
### 17. int

Specify the alignment type. Currently, no setting is available (always 0).

<!-- @since:5.1.0 -->
### 18. cursor

Specify the custom note to edit. Set 0:0 if create a new note.

## Return Code

Nothing.

## Sample Code

```psj
CreateCustomNote("CustomNote _1", [0, 0, 0], 0, 0:0, 0:0, "Collection _1", ["1st Line","2nd Line","3rd Line"], 30, 0, 0, 16777215, 1, 0, 1, 0, 1, 0, 0:0)
```
