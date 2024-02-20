import simplestream as ss


#api
def increment(state, value):
    state["counter"] += 1
    
def decrement(state, value):
    state["counter"] -= 1

    
#conditional func
def func(state):
    if state["counter"] > 5:
        return True
    else:
        return False

# State initialisation
ss.init_state({"counter": 0}) 


#ui
ss.text("The count is @counter.")

ss.button("Increment", onclick=increment)
ss.button("Decrement", onclick=decrement)


with ss.when(func): # Conditional rendering
    ss.text("Well done on reaching 5")
