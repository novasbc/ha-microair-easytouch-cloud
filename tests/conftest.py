"""Shared fixtures for custom integration tests."""

import pytest


@pytest.fixture
def hass_config_dir(hass_tmp_config_dir: str) -> str:
    """Keep PEM files written by the integration out of the installed test package."""
    return hass_tmp_config_dir


@pytest.fixture(autouse=True)
def enable_custom_component(enable_custom_integrations: None) -> None:
    """Allow Home Assistant to load custom integrations in tests."""
