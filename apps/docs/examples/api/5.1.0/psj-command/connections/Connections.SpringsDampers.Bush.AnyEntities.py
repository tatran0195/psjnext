# Title:   Connections.SpringsDampers.Bush.AnyEntities()
# Desc:    Create bush connection between nodes in target entities.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/connections/Connections.SpringsDampers.Bush.AnyEntities
# ---
#Prepare Model
Geometry.Part.Cube(iPartColor=6409934)

Connections.SpringsDampers.Bush.AnyEntities(  # [hl:start]
    strName="BUSH_1", 
    crlMaster=[Edge(18)], 
    crlSlave=[Edge(10)], 
    iOriMode=1, 
    poslVector=[0, 0, 0], 
    dlStiffness=[100.0, 200.0, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL], 
    dlDampCoef=[500.0, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL], 
    dlDampConst=[0.2, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL],
    crlStiffTbl=[Unknown(0, 0, 0, 0, 0, 0)], 
    crlDampCoefTbl=[Unknown(0, 0, 0, 0, 0, 0)], 
    crlDampConstTbl=[Unknown(0, 0, 0, 0, 0, 0)])  # [hl:end]
