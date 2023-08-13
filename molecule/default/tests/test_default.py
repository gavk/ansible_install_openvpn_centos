"""Role testing files using testinfra."""
import pytest


@pytest.mark.parametrize("name", [
    "epel-release",
    "openvpn"
])
def test_packages(host, name):
    package = host.package(name)
    assert package.is_installed
