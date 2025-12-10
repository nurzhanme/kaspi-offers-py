"""Pytest configuration and shared fixtures."""

import pytest
from client import KaspiClient
from tests.fixtures.sample_responses import (
    SAMPLE_OFFER_FULL,
    SAMPLE_OFFER_MINIMAL,
    SAMPLE_OFFER_EDGE_CASE,
    SAMPLE_RESPONSE_MULTIPLE,
    SAMPLE_RESPONSE_EMPTY,
    SAMPLE_RESPONSE_SINGLE,
    SAMPLE_RESPONSE_PAGINATED,
)


@pytest.fixture
def sample_offer_dict():
    """Return a valid offer dictionary with all fields."""
    return SAMPLE_OFFER_FULL.copy()


@pytest.fixture
def sample_offer_minimal_dict():
    """Return a minimal valid offer dictionary."""
    return SAMPLE_OFFER_MINIMAL.copy()


@pytest.fixture
def sample_offer_edge_case_dict():
    """Return an offer with edge cases."""
    return SAMPLE_OFFER_EDGE_CASE.copy()


@pytest.fixture
def sample_response_dict():
    """Return a valid API response with multiple offers."""
    return SAMPLE_RESPONSE_MULTIPLE.copy()


@pytest.fixture
def sample_response_empty_dict():
    """Return an empty offers response."""
    return SAMPLE_RESPONSE_EMPTY.copy()


@pytest.fixture
def sample_response_single_dict():
    """Return a response with a single offer."""
    return SAMPLE_RESPONSE_SINGLE.copy()


@pytest.fixture
def sample_response_paginated_dict():
    """Return a paginated response."""
    return SAMPLE_RESPONSE_PAGINATED.copy()


@pytest.fixture
def kaspi_client():
    """Return a KaspiClient instance with default configuration."""
    return KaspiClient()


@pytest.fixture
def kaspi_client_custom_timeout():
    """Return a KaspiClient instance with custom timeout."""
    return KaspiClient(timeout=10)
