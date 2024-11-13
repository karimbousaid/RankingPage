import unittest
from page import Page
from graph import Graph

class TestPageRank(unittest.TestCase):

    def setUp(self):
        # Create pages for testing
        self.pageA1 = Page("A1")
        self.pageB1 = Page("B1")
        self.pageA2 = Page("A2")
        self.pageB2 = Page("B2")
        self.pageC2 = Page("C2")
        self.pageA3 = Page("A3")
        self.pageB3 = Page("B3")
        self.pageC3 = Page("C3")
        self.pageA4 = Page("A4")
        self.pageB4 = Page("B4")
        self.pageC4 = Page("C4")

        # Create a graph instance
        self.graph = Graph()
        self.graph.add_page(self.pageA1)
        self.graph.add_page(self.pageB1)
        self.graph.add_page(self.pageA2)
        self.graph.add_page(self.pageB2)
        self.graph.add_page(self.pageC2)
        self.graph.add_page(self.pageA3)
        self.graph.add_page(self.pageB3)
        self.graph.add_page(self.pageC3)
        self.graph.add_page(self.pageA4)
        self.graph.add_page(self.pageB4)
        self.graph.add_page(self.pageC4)

        # Link pages as per the request
        self.graph.link_pages(self.pageA1, self.pageB1)
        self.graph.link_pages(self.pageB1, self.pageA1)
        self.graph.link_pages(self.pageA2, self.pageC2)
        self.graph.link_pages(self.pageC2, self.pageB2)
        self.graph.link_pages(self.pageB2, self.pageA2)
        self.graph.link_pages(self.pageA3, self.pageB3)
        self.graph.link_pages(self.pageB3, self.pageA3)
        self.graph.link_pages(self.pageB3, self.pageC3)
        self.graph.link_pages(self.pageA3, self.pageC3)
        self.graph.link_pages(self.pageA4, self.pageB4)
        self.graph.link_pages(self.pageB4, self.pageA4)
        self.graph.link_pages(self.pageB4, self.pageC4)
        self.graph.link_pages(self.pageA4, self.pageC4)

        # Calculate PageRank
        self.graph.calculate_page_rank()

    def test_calculated_page_rank(self):
        # Expected values
        expected_values = {
            "A1": 1,
            "B1": 1,
            "A2": 1,
            "B2": 1,
            "C2": 1,
            "A3": 0.26,
            "B3": 0.26,
            "C3": 0.37,
            "A4": 0.15,
            "B4": 0.27,
            "C4": 0.39
        }

        # Collect failed results
        failures = []

        # Check if the PageRank values are as expected
        for page_id, expected_rank in expected_values.items():
            page = getattr(self, f"page{page_id}")
            try:
                self.assertAlmostEqual(
                    page.page_rank, expected_rank, places=2,
                    msg=f'Failed for page {page_id}'
                )
            except AssertionError as e:
                # Capture the failure message and details
                failures.append(f'Failed for page {page_id}\nExpected: "Page: {page_id}, PageRank: {expected_rank:.2f}"\nGot: "{page}"')

        # If there are failures, print them all at once
        if failures:
            failure_message = "\n\n".join(failures)
            self.fail(f"Some PageRank calculations failed:\n\n{failure_message}")

if __name__ == '__main__':
    unittest.main()
