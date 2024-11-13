# Dokumentation des PageRank

Diese Dokumentation beschreibt die Klassen `Page` und `Graph`, die verwendet werden, um ein Netzwerk von verknüpften Seiten zu modellieren und deren PageRank-Werte zu berechnen. Das beigefügte Beispielskript zeigt, wie diese Klassen verwendet werden, um einen Graphen aufzubauen, Seiten zu verlinken und PageRank-Werte zu berechnen.

---

## Klasse: `Page`

Die `Page`-Klasse repräsentiert eine einzelne Seite innerhalb des Graphen. Jede Seite hat Verknüpfungen zu anderen Seiten und einen anfänglichen PageRank-Wert.

### Attribute

- **`id`** (str): Eine eindeutige Kennung für die Seite.
- **`out_links`** (list): Eine Liste der Seiten, zu denen diese Seite verlinkt (ausgehende Links).
- **`in_links`** (list): Eine Liste der Seiten, die auf diese Seite verlinken (eingehende Links).
- **`page_rank`** (float): Der PageRank-Wert der Seite, anfänglich auf `1.0` gesetzt.

### Methoden

- **`__init__(self, id)`**  
  Konstruktor zur Initialisierung einer `Page`-Instanz.
  - **Parameter**: 
    - `id` (str): Die eindeutige Kennung der Seite.
  
- **`add_out_link(self, page)`**  
  Fügt einen ausgehenden Link von der aktuellen Seite zu einer anderen Seite hinzu.
  - **Parameter**: 
    - `page` (`Page`): Die Seite, zu der verlinkt wird.

- **`add_in_link(self, page)`**  
  Fügt einen eingehenden Link von einer anderen Seite zur aktuellen Seite hinzu.
  - **Parameter**: 
    - `page` (`Page`): Die Seite, die auf die aktuelle Seite verlinkt.

- **`__str__(self)`**  
  Gibt eine Zeichenkettendarstellung der Seite mit ihrem PageRank zurück.
  - **Rückgabewert**: 
    - Eine Zeichenkette im Format `"Page: <id>, PageRank: <page_rank>"`.

---

## Klasse: `Graph`

Die `Graph`-Klasse repräsentiert ein Netzwerk von verknüpften `Page`-Instanzen und enthält Methoden, um Seiten zu verlinken und ihre PageRank-Werte zu berechnen.

### Attribute

- **`pages`** (list): Eine Liste aller `Page`-Instanzen im Graphen.

### Methoden

- **`__init__(self)`**  
  Konstruktor zur Initialisierung eines leeren Graphen.
  
- **`add_page(self, page)`**  
  Fügt eine `Page`-Instanz zum Graphen hinzu.
  - **Parameter**:
    - `page` (`Page`): Die hinzuzufügende Seite.

- **`link_pages(self, from_page, to_page)`**  
  Erstellt eine gerichtete Verlinkung von einer Seite zu einer anderen.
  - **Parameter**:
    - `from_page` (`Page`): Die Seite, die die Verlinkung initiiert.
    - `to_page` (`Page`): Die Seite, zu der verlinkt wird.

- **`calculate_page_rank(self, damping_factor=0.85, iterations=100)`**  
  Berechnet die PageRank-Werte für alle Seiten im Graphen mit einem iterativen Algorithmus.
  - **Parameter**:
    - `damping_factor` (float, optional): Der Dämpfungsfaktor für die PageRank-Formel, normalerweise auf `0.85` gesetzt.
    - `iterations` (int, optional): Die Anzahl der Iterationen für den Algorithmus.

- **`__str__(self)`**  
  Gibt eine Zeichenkettendarstellung des Graphen mit den PageRank-Werten für jede Seite zurück.
  - **Rückgabewert**:
    - Eine formatierte Zeichenkette, die jede Seite und ihren PageRank anzeigt.

---

## Beispielskript

Das Beispielskript zeigt, wie die `Graph`- und `Page`-Klassen verwendet werden, um ein Netzwerk von Seiten zu erstellen, Links festzulegen und PageRank-Werte zu berechnen.

### Code

```python
from graph import Graph
from page import Page

def main():
    graph = Graph()

    # Beispiel 1: Einfache Verlinkung zwischen zwei Seiten
    pageA1 = Page("A1")
    pageB1 = Page("B1")
    graph.add_page(pageA1)
    graph.add_page(pageB1)
    graph.link_pages(pageA1, pageB1)
    graph.link_pages(pageB1, pageA1)

    # Beispiel 2: Kreisförmige Verlinkung zwischen drei Seiten
    pageA2 = Page("A2")
    pageB2 = Page("B2")
    pageC2 = Page("C2")
    graph.add_page(pageA2)
    graph.add_page(pageB2)
    graph.add_page(pageC2)
    graph.link_pages(pageA2, pageC2)
    graph.link_pages(pageC2, pageB2)
    graph.link_pages(pageB2, pageA2)

    # Beispiel 3: Komplexes Netzwerk mit mehreren Links
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

    # Beispiel 4: Netzwerk mit bidirektionalen und unidirektionalen Links
    pageA4 = Page("A4")
    pageB4 = Page("B4")
    pageC4 = Page("C4")
    graph.add_page(pageA4)
    graph.add_page(pageB4)
    graph.add_page(pageC4)
    graph.link_pages(pageA4, pageB4)
    graph.link_pages(pageB4, pageA4)
    graph.link_pages(pageB4, pageC4)
    graph.link_pages(pageA4, pageC4)

    # PageRank-Werte berechnen
    graph.calculate_page_rank()

    # PageRank-Ergebnisse ausgeben
    print(graph)

if __name__ == "__main__":
    main()
