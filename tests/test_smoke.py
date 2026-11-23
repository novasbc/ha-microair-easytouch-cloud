"""Minimal import smoke test; behavior tests can be added later."""

from custom_components import microair_cloud
from homeassistant.core import HomeAssistant
from homeassistant.loader import async_get_integration


async def test_manifest_loads(hass: HomeAssistant) -> None:
    """The custom integration manifest is available to Home Assistant."""
    integration = await async_get_integration(hass, "microair_cloud")
    assert integration.domain == "microair_cloud"
    assert integration.manifest["version"]
    assert microair_cloud.DOMAIN == integration.domain
