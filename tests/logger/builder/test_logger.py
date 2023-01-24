"""Unit test file for logger.builder.logger.py."""
from src.probable_fiesta.logger.builder import logger

from logging import DEBUG
from unittest import TestCase

# Create a logger
#LOG = set_logger("test_logger", DEBUG)

import os

root_dir = os.getcwd()

class TestLogger(TestCase):

    def setUp(self):
        self.logger = None

    def test_init(self):
        print("Test init")
        self.logger = logger.Logger()

        self.assertEqual(self.logger.name, None)
        self.assertEqual(self.logger.level, None)
        self.assertEqual(self.logger.fmt, None)
        self.assertEqual(self.logger.directory, None)
        self.assertEqual(self.logger.logger, None)
        self.assertEqual(self.logger.file_handler, None)

        # test _str__
        self.assertEqual(str(self.logger), "Logger: {'name': None, 'level': None, 'fmt': None, 'directory': None, 'logger': None, 'file_handler': None}")

    def test_new(self):
        print("Test new")
        log_name = "test_logger"
        log_level = DEBUG
        log_fmt = 'simple'
        log_directory = '/logs'

        self.logger = logger.Logger().new(log_name, log_level, log_fmt, log_directory)

        self.assertEqual(self.logger.name, log_name)
        self.assertEqual(self.logger.level, log_level)
        self.assertEqual(self.logger.fmt, log_fmt)
        self.assertEqual(self.logger.directory, log_directory)
        self.assertEqual(self.logger.logger, None)
        self.assertEqual(self.logger.file_handler, None)

    def test_set_logger(self):
        print("Test set_logger")
        self.logger = logger.Logger()
        self.logger.set_logger("MY_MOCK_CLASS")
        self.assertEqual(self.logger.logger, "MY_MOCK_CLASS")

    def test_get_logger(self):
        print("Test get_logger")
        log_name = "test_logger"
        log_level = DEBUG
        log_fmt = 'simple'
        log_directory = root_dir+'/tests/logs'
        self.logger = logger.Logger().new(log_name, log_level, log_fmt, log_directory)
        parsed_logger = self.logger.get_logger()
        print(parsed_logger)
        self.assertEqual(str(parsed_logger.__class__), "<class 'logging.RootLogger'>")
