from functools import partial
from typing import Optional
import subprocess

from bazaarci.runner import Step


class SubprocessStep(Step):
    def __init__(self, name, graph: Optional["Graph"], *sp_args, **sp_kwargs):
        self.returned = None
        super().__init__(
            name,
            graph,
            target=self.run_grabbing_returned(*sp_args, **sp_kwargs),
        )

    def run_grabbing_returned(self, *sp_args, **sp_kwargs):
        self.returned = subprocess.run(*sp_args, **sp_kwargs)
