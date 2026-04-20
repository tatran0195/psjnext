# Title:   JPT.GetOpnList()
# Desc:    Get a list of string stores name of functions having their own GUI
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetOpnList
# ---
# Get all the functions having their own GUI
allFuncsWithGUI = JPT.GetOpnList()  # [hl]
JPT.Debugger(allFuncsWithGUI)
JPT.Debugger(allFuncsWithGUI[3])
