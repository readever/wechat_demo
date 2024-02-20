import streamsync as ss

ss.text("基础用法")
ss.text_input(placeholder="Please input")

ss.text("一键清空")

def onchange(state, value):
    ss.message(f"onchange, {value}")

def onclear(state, value):
    ss.message("onclear event happend")

def onblur(state, value):
    print("onblur")
    ss.message(f"onblur, {value}")
    
def testme():
    ss.message(myinput.value)

myinput = ss.text_input("clearable", value="初始值", handlers={"change": onchange, "clear":onclear, "blur":onblur})
 
ss.button("读取文本框值", onclick=testme)


ss.text("密码框")
ss.text_input("show-password", value="123456", type="password")

ss.text("带图标的输入框")
ss.text_input(placeholder="pick a date", suffix_icon = "Calendar")
ss.text_input(placeholder="type something", prefix_icon = "Search")

ss.text("文本域")
input = ss.text_input(placeholder="please input", type="textarea")
