#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# External functions.
# Each function must return value, that can be
# represent as string by str() function

import random

def rnd(imin, imax, step=1):
	i = random.randrange(imin, imax)
	return i - i % step

def frnd(fmin=0, fmax=1):
	return random.uniform(fmin, fmax)
