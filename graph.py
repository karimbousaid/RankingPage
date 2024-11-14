from page import Page

class Graph:
    def __init__(self):
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def link_pages(self, from_page, to_page):
        from_page.add_out_link(to_page)
        to_page.add_in_link(from_page)

    def calculate_page_rank(self, damping_factor=0.85, iterations=15, startwert=1):
        for page in self.pages:
            page.page_rank = startwert

        # Single iteration to update PageRank values
        for _ in range(iterations):
            # Temporary dictionary to store the new ranks for pages
            new_ranks = {}

            # Calculate PageRank for each page
            for page in self.pages:
                rank_sum = 0.0
                # Sum the PageRank contributions from incoming links
                for in_link in page.in_links:
                    if len(in_link.out_links) > 0:
                        rank_sum += in_link.page_rank / len(in_link.out_links)
                
                # Apply the PageRank formula
                new_rank = (1 - damping_factor) + damping_factor * rank_sum
                new_ranks[page] = new_rank
            
            # Update the PageRank values with the new ranks
            for page, new_rank in new_ranks.items():
                page.page_rank = new_rank

    def __str__(self):
        return "\n".join(str(page) for page in self.pages)