---
title: CursorStr
id: CursorStr
---

## Description

Represents a single cursor or multiple cursors separated by commas. It can be used as instead of _Cursor_, or a content of _List of Cursor_

## Properties

| Attribute       | Description                                                                                                             |
| --------------- | ----------------------------------------------------------------------------------------------------------------------- |
| getID()         | Returns ID of an entity or list of IDs of the entities .                                                                |
| getType()       | Returns the type of the entity as [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int) in CursorStr. |
| getCursorData() | Returns a DItem data of an entity of a list of DItems data of the entities.                                             |
