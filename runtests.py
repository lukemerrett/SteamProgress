import unittest

if __name__ == "__main__":
    # Finds all tests in submodules ending in *tests.py and runs them
    suite = unittest.TestLoader().discover('.', pattern = "*tests.py")
    unittest.TextTestRunner(verbosity=2).run(suite)
