"""
Custom Error classes
"""
from reoptimization_algorithms.errors.BaseError import Error


class InputError(Error):
    """
    Exception raised for errors in the input

    :param expression: input expression in which the error occurred
    :param message: explanation of the error
    :type message: str
    """

    def __init__(self, expression, message):
        """
        Exception raised for errors in the input

        :param expression: input expression in which the error occurred
        :param message: explanation of the error
        :type message: str
        """
        self.expression = expression
        self.message = message
