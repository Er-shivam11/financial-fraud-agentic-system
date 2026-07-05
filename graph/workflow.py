# graph/workflow.py
from langgraph.graph import StateGraph, START, END

from graph.state import BankingState
from graph.nodes import (
    sql_generator_node,
    execute_sql_node,
    explain_node,
)

from memory.checkpointer import memory

builder = StateGraph(BankingState)

builder.add_node("generate_sql", sql_generator_node)
builder.add_node("execute_sql", execute_sql_node)
builder.add_node("explain", explain_node)

builder.add_edge(START, "generate_sql")
builder.add_edge("generate_sql", "execute_sql")
builder.add_edge("execute_sql", "explain")
builder.add_edge("explain", END)

graph = builder.compile(checkpointer=memory)