#!/usr/bin/python3

"""Minimum operations."""


def minOperations(n):
    """((Ctrl + A, Ctrl + C)), Ctrl + V"""
    if n <= 1:
        return 0

    laOperations = 0
    currentLen = 1
    iWillJustCallThisCache = 0

    while currentLen < n:
        if n % currentLen == 0:
            iWillJustCallThisCache = currentLen
            laOperations += 1
        currentLen += iWillJustCallThisCache
        laOperations += 1

    return laOperations
