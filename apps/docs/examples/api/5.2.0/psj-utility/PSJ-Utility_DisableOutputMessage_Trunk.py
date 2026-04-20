# Title:   JPT.DisableOutputMessage()
# Desc:    Disable all the output messages which will be written to the Python API window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_DisableOutputMessage_Trunk
# ---
# Disable the execution message
JPT.DisableOutputMessage(JPT.MsgConsoleType.MSG_EXECUTION)  # [hl]
Geometry.Part.Cube(strName="Cube_2", iPartColor=12934597) # won't print "CreateCube" [0.0, 0.0, 0.0],...
print("test")
JPT.Debugger("Test")

# Disable the return message
JPT.DisableOutputMessage(JPT.MsgConsoleType.MSG_RETURN)  # [hl]
Geometry.Part.Cube(strName="Cube_2", iPartColor=12934597) # won't print 3:1
print("test")
JPT.Debugger("Test")

# Disable the user message (print/debug message)
JPT.DisableOutputMessage(JPT.MsgConsoleType.MSG_USER)  # [hl]
Geometry.Part.Cube(strName="Cube_2", iPartColor=12934597)
print("test") # won't print "test"
JPT.Debugger("Test") # won't print "Test"
