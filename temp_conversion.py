from langgraph.graph import StateGraph, START, END
from typing import TypedDict  # ✅ Correct import

# Definition of Parameters
class Parameters(TypedDict):
    temp_celsius: float
    temp_fahrenhiet: float  # ⚠️ Note: "farenhiet" is misspelled here

# Conversion function
def Temp_conversion(state: Parameters) -> Parameters:
    celsius = state['temp_celsius']
    fahrenhiet = (celsius * 9/5) + 32
    state['temp_fahrenhiet'] = fahrenhiet  # ⚠️ "temp_fahrenhiet" matches the class key
    return state

# Graph setup
graph = StateGraph(Parameters)  # ✅ Now works with correct import
graph.add_node('convert_temp', Temp_conversion)
graph.add_edge(START, 'convert_temp')
graph.add_edge('convert_temp', END)

workflow = graph.compile()

initial_state = {'temp_celsius': 28.5}
final_state = workflow.invoke(initial_state)
print(final_state)  # ✅ Fixed syntax
