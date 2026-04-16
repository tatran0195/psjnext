# Title:   Tools.BySelection.Position()
# Desc:    Renumber by position
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.BySelection.Position
# ---
# model and environment settings
JPT.Exec('ViewShowID(1)')
Geometry.Part.Cube(ilAxialNodes=[4, 4, 4], iPartColor=7434735)
JPT.ViewFitToModel()

# show current node ids
curl_nodes=MainWindow.RightClick.AssociatedPick(crlInput=[Part(1)], strTarget="Node")
ditem_nodes=JPT.MacroListTCursorToListDItem(curl_nodes)

JPT.SelectionByIDs(JPT.DItemType.NODE, [ditem.id for ditem in ditem_nodes], True)
JPT.MessageBoxPSJ("Check current node IDs", JPT.MsgBoxType.MB_INFORMATION_OK)

# renumber nodes
Tools.BySelection.Position(  # [hl:start]
    crlTargets=[Node(*[ditem_node.id for ditem_node in ditem_nodes])],
    iMethod=2, 
    bAscending2=True, 
    bAscending3=True, 
    iEnableSortSecond=1, 
    iEnableSortThird=1, 
    iOffset1=100, 
    iOffset2=1000, 
    iOffset3=1, 
    dTol1=1e-05, 
    dTol2=1e-05, 
    dTol3=1e-05)  # [hl:end]
    
# show renumbered node ids
curl_nodes=MainWindow.RightClick.AssociatedPick(crlInput=[Part(1)], strTarget="Node")
ditem_nodes=JPT.MacroListTCursorToListDItem(curl_nodes)
JPT.SelectionByIDs(JPT.DItemType.NODE, [ditem.id for ditem in ditem_nodes], True)
JPT.MessageBoxPSJ("Node IDs have changed and aligned.", JPT.MsgBoxType.MB_INFORMATION_OK)

