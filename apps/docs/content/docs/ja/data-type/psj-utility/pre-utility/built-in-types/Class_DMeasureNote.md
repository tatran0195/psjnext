---
title: DMeasureNote
id: DMeasureNote
---

## Description

This is an instance of a DMeasureNote class, represents a measure note inside Jupiter.

## Properties

| Attribute       | Description                                                                                                                                                      |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------- |
| typeID          | Type ID of the measure note (ID = 278).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                     |
| tableID         | Table ID of the measure note item (ID = 160). The return value is an [`Int notation of DTable Types`](../enumeration-types/dtable-types)(int).                   |
| id              | External ID of the measure note.<br />The return value is ID (int).                                                                                              |
| name            | Name of the measure note.<br />The return value is a string.                                                                                                     |
| positions       | Position coordinate of the measure note.<br /> The return value is [`TVector3d.`](../built-in-types/TVector3d)                                                   |
| targets         | The target entities which the measure note is created on. The return value is a [`DItem`](../../../psj-command/DItem-types).                                     |          |
| parent          | The measure note collection where the new measure note is append.<br /> The return value is [`DMeasureNoteCollection.`](../built-in-types/DCustomNoteCollection) | fontSize | The font size of the text of Content. <br /> The return value is int. |
| fontColor       | The color of the text of Content. <br /> The return value is a RGB color.                                                                                        |
| fontSize        | The size of font. <br /> The return value is a int.                                                                                                              |
| fontBold        | Bold text or not in the Content.<br /> The return value is 0 or 1 (bold)                                                                                         |
| backgroundColor | The ground color of the measure note.<br /> The return value is a RGB color.                                                                                     |
| outlineWidth    | The width of the note border.<br /> The return value is int.                                                                                                     |
| outlineColor    | The color of the note border.<br /> The return value is a RGB color.                                                                                             |
| arrowWidth      | The thickness of the line extending from the note to the coordinate position.<br />The return value is int.                                                      |
| arrowColor      | The color of the line extending from the note to the coordinate position.<br />The return value is a RGB color.                                                  |
| arrowType       | The type of arrow.                                                                                                                                               |
| arrowWidth      | The shape type that points to the coordinate position.<br /> The return value is 0 (None) or 1 (Arrow)                                                           |
| coordinate      | Coordinate that the measure value refer to.                                                                                                                      |
| titleType       | Measuer title type of the measure note.                                                                                                                          |
| type            | Command name that the measure note is created by.                                                                                                                |
| values          | Measured values                                                                                                                                                  |
