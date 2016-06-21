import logging
from datamodel.nodes import printer

log_level = logging.INFO
logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)


def test_requirements():
    expected = ['message', 'logger', 'loglevel']
    instance = printer.LogPrinter()
    assert instance.requirements == expected


def test_input():
    msg = 'Hello world'
    instance = printer.LogPrinter()
    instance.input(dict(message=msg, logger=logger, loglevel=log_level))
    assert instance.output() == msg


def test_output():
    msg = 'Hello world'
    instance = printer.LogPrinter(message=msg, logger=logger, loglevel=log_level)
    assert instance.output() == msg

