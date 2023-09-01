import logging
from services.triangle_calculator import TriangleCalculator
from services.manager.logging_manager import LogginManager

if __name__ == "__main__":
    triangle_calculator = TriangleCalculator()
    while True:
        try:
            sides = []
            for i in range(3):
                side = float(input(f"Adicione o comprimento do lado {chr(97 + i)}: "))
                sides.append(side)
        
            a, b, c = sides

            triangle_type = triangle_calculator.get_triangle_type(a, b, c)
            print(f"O triangulo é {triangle_type}.")

            user_input = input("Desejar continuar? (s/n): ")
            if user_input.lower() != 's':
                break
        except Exception as e:
            logging.error(f"Um erro ocorreu durante o loop de validação: {e}")
            break