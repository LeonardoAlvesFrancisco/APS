import logging
from services.manager.logging_manager import LogginManager

class TriangleCalculator:
    def __init__(self) -> None:
        LogginManager().setup_logging()
        
    def validate_triangle(self, a, b, c) -> bool:
        """
        Valida se os comprimentos dos lados a, b e c formam um triângulo válido.
        
        Args:
            a (float): Comprimento do lado a.
            b (float): Comprimento do lado b.
            c (float): Comprimento do lado c.
            
        Returns:
            bool: True se os lados formam um triângulo válido, False caso contrário.
        """
        try:
            if a + b > c and a + c > b and b + c > a:
                return True
            else:
                return False
        except Exception as e:
            logging.error(f"Um erro ocorreu enquanto se validava o triangulo: {e}")
            return False

    def get_triangle_type(self, a, b, c) -> str:
        """
        Determina o tipo de triângulo com base nos comprimentos dos lados.
        
        Args:
            a (float): Comprimento do lado a.
            b (float): Comprimento do lado b.
            c (float): Comprimento do lado c.
            
        Returns:
            str: O tipo de triângulo ("Equilátero", "Isósceles" ou "Escaleno").
            Retorna uma mensagem de erro se os lados não formarem um triângulo válido.
        """
        try:
            if not self.validate_triangle(a, b, c):
                return "Triangulo invalido, forneça outras informações."

            if a == b == c:
                return "Equilátero"
            elif a == b or b == c or a == c:
                return "Isósceles"
            else:
                return "Escaleno"
        except Exception as e:
            logging.error(f"Um erro ocorreu enquanto se validava o triangulo: {e}")

