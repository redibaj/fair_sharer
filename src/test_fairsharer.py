import pytest
from fair_sharer import fair_sharer

def test_fair_sharer():
    # Testen mit den Beispielen aus der Aufgabenstellung
    assert fair_sharer([0, 1000, 800, 0], 1) == [100.0, 800.0, 900.0, 0]
    assert fair_sharer([0, 1000, 800, 0], 2) == [100.0, 890.0, 720.0, 90.0]

    # Zusätzliche Testfälle
    # Testen mit einer leeren Liste
    assert fair_sharer([], 1) == []
    # Testen mit einer Liste, in der alle Werte gleich sind
    assert fair_sharer([100, 100, 100], 1) == [100, 100, 100]
    # Testen mit num_iterations als 0
    assert fair_sharer([10, 20, 30], 0) == [10, 20, 30]
