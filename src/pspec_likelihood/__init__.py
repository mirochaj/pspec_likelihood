"""The PSpec Likelihood Package."""
from . import likelihood
from .arbitrary_linear_systematics import LikelihoodLinearSystematic
from .likelihood import (
    DataModelInterface,
    Gaussian,
    GaussianLinearSystematics,
    MarginalizedLinearPositiveSystematics,
)

# This gets managed by python-semantic-release, don't touch!
__version__ = "0.1.1"
