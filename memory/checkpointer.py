from langgraph.checkpoint.memory import MemorySaver

# In-memory checkpoint storage
# Later we can replace this with Redis/Postgres

memory = MemorySaver()