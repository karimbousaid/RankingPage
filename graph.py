from page import Page

class Graph:
    def __init__(self):
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def link_pages(self, from_page, to_page):
        from_page.add_out_link(to_page)
        to_page.add_in_link(from_page)

    def calculate_page_rank(self, damping_factor=0.85, iterations=100):
        # Initialize PageRank values to 1.0
        for page in self.pages:
            page.page_rank = 1.0

        # Calculate PageRank iteratively
        for _ in range(iterations):
            for page in self.pages:
                rank_sum = 0.0
                # Sum up the PageRank contributions from the incoming links
                for in_link in page.in_links:
                    rank_sum += in_link.page_rank / len(in_link.out_links)
                # Apply the PageRank formula
                page.page_rank = (1 - damping_factor) + damping_factor * rank_sum

    def __str__(self):
        return "\n".join(str(page) for page in self.pages)
