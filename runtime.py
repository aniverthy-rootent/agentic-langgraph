"""LangGraph runtime: every agent is a node in a StateGraph.

Edges come from common.flow.dependencies(); fan-in uses a join edge so the
merger node waits for all parallel specialists.
"""
from __future__ import annotations

from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph

from common.flow import compose_input, dependencies, system_prompt
from common.offline_llm import offline_complete


def _merge(a: dict, b: dict) -> dict:
    return {**a, **b}


class State(TypedDict):
    outputs: Annotated[dict, _merge]


def call_llm(system: str, user: str) -> str:
    """Replace with a LangChain chat model (see README) for real LLM calls."""
    return offline_complete(system, user)


def build_graph(agents, task, pattern):
    deps = dependencies(pattern, len(agents))
    graph = StateGraph(State)

    def make_node(i):
        key, role, instr = agents[i]

        def node(state: State) -> dict:
            ups = [(agents[j][1], state["outputs"][agents[j][0]]) for j in deps[i]]
            text = call_llm(system_prompt(role, instr), compose_input(task, ups))
            return {"outputs": {key: text}}

        return node

    for i, (key, _, _) in enumerate(agents):
        graph.add_node(key, make_node(i))
    for i, (key, _, _) in enumerate(agents):
        if not deps[i]:
            graph.add_edge(START, key)
        elif len(deps[i]) == 1:
            graph.add_edge(agents[deps[i][0]][0], key)
        else:
            graph.add_edge([agents[j][0] for j in deps[i]], key)
    graph.add_edge(agents[-1][0], END)
    return graph.compile()


def run_app(title, agents, task, pattern="sequential", provider=None) -> dict:
    final = build_graph(agents, task, pattern).invoke({"outputs": {}})
    return {key: final["outputs"][key] for key, _, _ in agents}
