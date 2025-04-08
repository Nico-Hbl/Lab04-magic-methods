# Vektor-Klasse mit Magic Methods
# TODO: Implementieren Sie die Methode Ausgabe des Vektors
class Vektor:
    def __init__(self, x, y):
        """Initialisiert einen Vektor mit x- und y-Koordinate."""
        self.x = x
        self.y = y
         
    def __str__(self):
        """Gibt eine lesbare Darstellung des Vektors zurück."""
        return f"({self.x}, {self.y})"
    
    #   """Gibt eine lesbare Darstellung des Vektors zurück."""
    #   ...

    # TODO: Implementieren Sie die Methode zur Addition zweier Vektoren
    #   """Gibt eine lesbare Darstellung des Vektors zurück."""
    #   ...
    def __add__(self, anderer):
        """Ermöglicht die Addition zweier Vektoren."""
        return Vektor(self.x + anderer.x, self.y + anderer.y)
  
    #   """Ermöglicht die Addition zweier Vektoren."""
    #   ...

    # TODO: Implementieren Sie die Methode zur Subtraktion zweier Vektoren           
    def __sub__(self, anderer):
        """Ermöglicht die Addition zweier Vektoren."""
        return Vektor(self.x - anderer.x, self.y - anderer.y)
    
    #   """Ermöglicht die Subtraktion zweier Vektoren."""
    #   ...

    # TODO: Implementieren Sie die Methode zur skalaren Multiplikation
    def __mul__(self, skalar):
        """Ermöglicht die skalare Multiplikation."""
        return Vektor(self.x * skalar, self.y * skalar)
     
    #   """Ermöglicht die skalare Multiplikation."""
    #   ...

    # TODO: Implementieren Sie die Vergleichsmethode für zwei Vektoren
    def __eq__(self, anderer):
        """Vergleicht zwei Vektoren auf Gleichheit."""
        return self.x == anderer.x and self.y == anderer.y
      
    #   """Vergleicht zwei Vektoren auf Gleichheit."""
    #   ...

    # TODO: Implementieren Sie die Methode zur elementweisen Potenzierung
    def __pow__(self, exponent):
        """Ermöglicht die elementweise Potenzierung des Vektors."""
        return Vektor(self.x ** exponent, self.y ** exponent)
       
    #   """Ermöglicht die elementweise Potenzierung des Vektors."""
    #   ...

    # TODO: Implementieren Sie die Methode für das Skalarprod. zweier Vektoren
    def __matmul__(self, anderer):
        """Ermöglicht das Skalarprodukt zweier Vektoren."""
        return self.x * anderer.x + self.y * anderer.y
        
    #   """Ermöglicht das Skalarprodukt zweier Vektoren."""
    #   ...

    # Testfälle für die Vektor-Klasse
def main():
    v1 = Vektor(3, 4)
    v2 = Vektor(1, 2)

    # TODO: Aktivieren Sie die folgenden Zeilen nach Implementierung der Methoden
    print("Vektor 1:", v1)
    print("Vektor 2:", v2)

    print("Addition:", v1 + v2)

    # TODO: Aktivieren Sie die folgenden Zeilen nach Implementierung der Methoden
    print("Subtraktion:", v1 - v2)
    print("Multiplikation mit Skalar 2:", v1 * 2)
    print("Vergleich (sollte False sein):", v1 == v2)
    print("Vergleich (sollte True sein):", v1 == Vektor(3, 4))
    print("Elementweise Potenzierung mit Exponent 2:", v1 ** 2)
    print("Skalarprodukt (Matmul-Operator):", v1 @ v2)

if __name__ == "__main__":
    main()