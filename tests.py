import unittest
import importlib.util
import sys
import os

def load_module_from_path(path, module_name="submission"):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

class TestReverseWords(unittest.TestCase):
    def setUp(self):
        self.module_path = os.environ.get("SUBMISSION_PATH", "solution.py") #default location is solution.py
        self.module = load_module_from_path(self.module_path)
        self.func = self.module.reverse_words

    def test_basic(self):
        self.assertEqual(self.func("Hello world"), "olleH dlrow")

    def test_single_word(self):
        self.assertEqual(self.func("Python"), "nohtyP")

    def test_empty_string(self):
        self.assertEqual(self.func(""), "")

    def test_with_punctuation(self):
        self.assertEqual(self.func("Hi there!"), "iH !ereht")

if __name__ == "__main__":
    unittest.main()
