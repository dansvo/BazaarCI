from typing import Optional

from bazaarci.runner.node import Node


class Graph(Node, set):
    def __init__(self, name: str, graph: Optional["Graph"] = None):
        super().__init__(name, graph)

    def produces(self):
        for node in self:
            for product in node.produces():
                yield product

    def consumes(self):
        for node in self:
            for product in node.consumes():
                yield product

    def start(self):
        [step.start() for step in self]

    def wait(self):
        [step.thread.join() for step in self if step.thread and step.thread.is_alive()]

    def to_dot(self):
        all_step_statements = "\n".join(step.to_dot() for step in self)
        if self.graph is None:  # this is the top level graph
            return f"digraph \"{self.name}\" {{ compound=true; rankdir=LR; {all_step_statements} }}"
        else:  # this is a subgraph
            return f"subgraph \"{self.name}\" {{ {all_step_statements} }}"
