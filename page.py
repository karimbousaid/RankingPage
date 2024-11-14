class Page:
    def __init__(self, id):
        self.id = id
        self.out_links = []
        self.in_links = []
        self.page_rank = 1.0

    def add_out_link(self, page):
        self.out_links.append(page)

    def add_in_link(self, page):
        self.in_links.append(page)

    def __str__(self):
        if self.page_rank == 1:
            return f"Page: {self.id}, PageRank: {int(self.page_rank)}"
        else:
            return f"Page: {self.id}, PageRank: {self.page_rank:.2f}"
