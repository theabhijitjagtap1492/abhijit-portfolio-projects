from langgraph.graph import StateGraph, END             # LangGraph components for stateful workflows
from langchain_core.runnables import RunnableLambda     # Giving custom Python logic to LangChain runnables
from agents.research_agent import build_research_agent  # Importing research agent
from agents.writer_agent import build_writer_agent      # Importing writer agent
from dotenv import load_dotenv
load_dotenv()

# Defining the 'research' node LangGraph
def research_node(state):
    """
    This node performs web research using the research agent.
    the state (dict): The current state containing at least a 'query' key.
    Returns:
        dict: Updated state with added 'context' key.
    """
    
    # Ensures requirement exists
    if "query" not in state:
        raise KeyError("The key 'query' is missing in the state.")

    query = state["query"]
    # Activates research agent with the query
    context = build_research_agent().invoke(query)
    
    # Debuging: Printing what the state looks like
    print(f"🔍 RESEARCH NODE received state of type {type(state)}: {state}")
    
    return state | {"context": context} # Merge with existing state

# Defining the 'writer' node in the LangGraph
def writer_node(state):
    """
    Generates the final answer using the writer agent.
    the state (dict): The current state containing 'query' and 'context'.
    Returns:
        dict: Updated state with the added 'answer' key.
    """
    # Ensure both keys exist
    if "query" not in state or "context" not in state:
        raise KeyError("Either 'query' or 'context' is missing in the state.")

    query = state["query"]
    context = state["context"]
    # Activates the writer agent with query + context
    answer = build_writer_agent().invoke({"query": query, "context": context})
    
    # Debugging: Print what the state looks like
    print(f"🔍 RESEARCH NODE received state of type {type(state)}: {state}")
    
    return state | {"answer": answer} # Merging with existing state

# Building LangGraph

# Initializing the LangGraph using custom state structure
graph = StateGraph(dict)
graph.add_node("research", RunnableLambda(research_node))
graph.add_node("writer", RunnableLambda(writer_node))

# Defining flow of execution
graph.set_entry_point("research")        # Starting research node
graph.add_edge("research", "writer")     # Then research, going to writer
graph.add_edge("writer", END)            # Writer is final node

# Compiling graph into an executable app
app = graph.compile()

# User Interface

# ✅ THIS function imported in Streamlit
def run_langgraph_pipeline(user_query):
    """
    Running the full LangGraph pipeline.
    then
        user_query (str): The user's research question or URL.
    Returns:
        final generated answer from the pipeline.
    """
    initial_state = {"query": user_query}
    
    # Debugging: Printing initial state
    print(f"Initial state: {initial_state}")
    
    final_state = app.invoke(initial_state)
    
    # Debugging: Printing final state
    print(f"Final state: {final_state}")
    
    # Returning final answer else fallback message
    return final_state.get("answer", "No answer found")

