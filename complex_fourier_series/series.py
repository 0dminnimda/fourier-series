#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

from cmath import exp, tau
from typing import List

from scipy.integrate import quad

from .svg_handling import FLOAT_TO_COMPLEX


TAU_I: complex = tau * 1j


def create_nth_constant_function(
        n: int, path_func: FLOAT_TO_COMPLEX) -> FLOAT_TO_COMPLEX:

    def f(t: float) -> complex:
        return path_func(t) * exp(-n * TAU_I * t)

    return f


def calculate_nth_constant(
        n: int, constant_func: FLOAT_TO_COMPLEX) -> complex:

    return quad(constant_func, 0, 1)


def create_nth_series_function(
        n: int, nth_constant: complex) -> FLOAT_TO_COMPLEX:

    def f(t: float) -> complex:
        return nth_constant * exp(n * TAU_I * t)

    return f


def get_frequency_by_index(index: int) -> int:
    """
    -> 0  1  2  3  4  5  6  7  8 ...
    <- 0  1 -1  2 -2  3 -3  4 -4 ...
    """

    sign: int = -1 if index % 2 == 0 else 1

    return ((index + 1) // 2) * sign

