# Title:   JPT.MacroListTCursorToListDItem()
# Desc:    Convert a cursor list (Macro string type) to a DItemVector
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_MacroListTCursorToListDItem
# ---
# Prepare model
Geometry.Part.Cube()

# Convert a cursor list (Macro string type) to a DItemVector
## Create a list of Node cursor
strCursorNode1 = "10:467"
strCursorNode2 = "10:477"
strCursorNode3 = "10:483"
listCursorNode = f"[{strCursorNode1}, {strCursorNode2}, {strCursorNode3}]"
## Convert cursor list to list of DItem
JPT.Debugger(JPT.MacroListTCursorToListDItem(listCursorNode))  # [hl]
