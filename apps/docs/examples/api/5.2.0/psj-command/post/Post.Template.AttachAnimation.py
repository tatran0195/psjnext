# Title:   Post.Template.AttachAnimation()
# Desc:    Attach the current animation settings to the specified template
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Template.AttachAnimation
# ---
Post.Template.Create(strName="Animation_Template", strComment="Attach Animation Template")
template = Post.Template.AttachAnimation(strName="Animation_Template",   # [hl:start]
                                        postDataVizOptAnimation=POST_DATA_VIZ_OPT_ANIMATION(
                                            iFPS=10, 
                                            iFrameNumber=10, 
                                            iLoopType=0, 
                                            bPhaseAngle=True))  # [hl:end]
JPT.Debugger(template)
