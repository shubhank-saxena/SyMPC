"""function used to calculate sigmoid of a given tensor."""
# stdlib
from typing import Any

# third party
import torch

from sympc.approximations.exponential import exp
from sympc.approximations.reciprocal import reciprocal
from sympc.approximations.utils import sign


