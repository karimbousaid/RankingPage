from graph import Graph
from page import Page

def test_startwert_and_iterations(graph, startwert_values, iteration_values):
    for startwert in startwert_values:
        for iterations in iteration_values:
            for page in graph.pages:
                page.page_rank = startwert
            
            print(f"Startwert={startwert}, Iterations={iterations}")
            
            graph.calculate_page_rank(iterations=iterations, startwert=startwert)
            
            print("Result:")
            for page in graph.pages:
                print(f"{page.id}: {page.page_rank:.2f}")
            print("-" * 30)

def main():
    graph = Graph()

    # Example 1
    pageA1 = Page("A1")
    pageB1 = Page("B1")
    graph.add_page(pageA1)
    graph.add_page(pageB1)
    graph.link_pages(pageA1, pageB1)
    graph.link_pages(pageB1, pageA1)

    # Example 2
    pageA2 = Page("A2")
    pageB2 = Page("B2")
    pageC2 = Page("C2")
    graph.add_page(pageA2)
    graph.add_page(pageB2)
    graph.add_page(pageC2)
    graph.link_pages(pageA2, pageC2)
    graph.link_pages(pageC2, pageB2)
    graph.link_pages(pageB2, pageA2)

    # Example 3
    pageA3 = Page("A3")
    pageB3 = Page("B3")
    pageC3 = Page("C3")
    graph.add_page(pageA3)
    graph.add_page(pageB3)
    graph.add_page(pageC3)
    graph.link_pages(pageA3, pageB3)
    graph.link_pages(pageB3, pageA3)
    graph.link_pages(pageB3, pageC3)
    graph.link_pages(pageA3, pageC3)

    # Example 4
    pageA4 = Page("A4")
    pageB4 = Page("B4")
    pageC4 = Page("C4")
    graph.add_page(pageA4)
    graph.add_page(pageB4)
    graph.add_page(pageC4)
    graph.link_pages(pageA4, pageB4)
    graph.link_pages(pageB4, pageC4)

    # Test different start values and iterations
    startwert_values = [1, 0.5, 0.25]
    iteration_values = [5, 10, 15, 100]

    test_startwert_and_iterations(graph, startwert_values, iteration_values)

if __name__ == "__main__":
    main()