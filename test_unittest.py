import pytest
from pytest_trio.enable_trio_mode import \
    pytest_fixture_setup as trio_pytest_fixture_setup

from kivy.config import Config
Config.set('modules', 'touchring', '')

from pytest_kivy.app import AsyncUnitApp
from simpleapp import SimpleApp


class SimpleTestApp(AsyncUnitApp):
    app: SimpleApp


def pytest_fixture_setup(fixturedef, request):
    # unfortunately we can't parameterize fixtures from fixtures, so we have to
    # use a hammer to set window size and test class to use
    if fixturedef.argname == 'trio_kivy_app':
        request.param = {
            'kwargs': {'width': 1600, 'height': 900}, 'cls': SimpleTestApp}

    trio_pytest_fixture_setup(fixturedef, request)


@pytest.fixture
async def simple_app(trio_kivy_app) -> SimpleTestApp:
    try:
        await trio_kivy_app(SimpleApp)
        yield trio_kivy_app
    finally:
        if trio_kivy_app.app is not None:
            trio_kivy_app.app.clean_up()


async def test_open_app(simple_app):
    await simple_app.wait_clock_frames(5)


async def test_app_settings(simple_app):
    assert simple_app.app.root.get_screen("HomeScreen").note == "I am a note"