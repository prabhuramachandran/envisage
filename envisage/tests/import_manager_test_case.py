""" Tests for the import manager. """


# Standard library imports.
import unittest

# Enthought library imports.
from envisage.api import Application, ImportManager


class ImportManagerTestCase(unittest.TestCase):
    """ Tests for the import manager. """

    ###########################################################################
    # 'TestCase' interface.
    ###########################################################################

    def setUp(self):
        """ Prepares the test fixture before each test method is called. """

        # We do all of the testing via the application to make sure it offers
        # the same interface!
        self.import_manager = Application(import_manager=ImportManager())

        return

    def tearDown(self):
        """ Called immediately after each test method has been called. """

        return

    ###########################################################################
    # Tests.
    ###########################################################################

    def test_import_dotted_symbol(self):
        """ import dotted symbol """

        symbol = self.import_manager.import_symbol('unittest.TestCase')
        self.assertEqual(symbol, unittest.TestCase)

        return

    def test_import_nested_symbol(self):
        """ import nested symbol """

        symbol = self.import_manager.import_symbol('unittest:TestCase.setUp')
        self.assertEqual(symbol, unittest.TestCase.setUp)

        return

    def test_import_dotted_module(self):
        """ import dotted modulel """

        symbol = self.import_manager.import_symbol(
            'envisage.api:ImportManager'
        )
        self.assertEqual(symbol, ImportManager)

        return


# Entry point for stand-alone testing.
if __name__ == '__main__':
    unittest.main()

#### EOF ######################################################################
