# how to run a single test:
# $ python -m unittest tests.test_demo.Main.test_algus1

from lino.utils.pythontest import TestCase


class Main(TestCase):

    demo_projects_root = "lino_algus/projects"

    def test_amici1(self):
        self.do_test_demo_project('algus1')
