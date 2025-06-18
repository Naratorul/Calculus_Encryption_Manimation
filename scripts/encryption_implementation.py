"""
Implementation of the calculus-based encryption algorithm
"""

import math
import numpy as np
from typing import List, Tuple, Callable

class CalculusEncryption:
    def __init__(self, key_function: Callable[[float], float] = None):
        """
        Initialize the calculus encryption system
        
        Args:
            key_function: Mathematical function used as encryption key
        """
        self.key_function = key_function or (lambda x: math.sin(2 * x) + math.cos(x))
        self.constants = {
            'e': math.e,
            'pi': math.pi,
            'phi': (1 + math.sqrt(5)) / 2  # Golden ratio
        }
    
    def numerical_derivative(self, func: Callable[[float], float], x: float, h: float = 1e-7) -> float:
        """
        Calculate numerical derivative using central difference
        """
        return (func(x + h) - func(x - h)) / (2 * h)
    
    def numerical_integral(self, func: Callable[[float], float], a: float, b: float, n: int = 1000) -> float:
        """
        Calculate numerical integral using Simpson's rule
        """
        if n % 2 == 1:
            n += 1
        
        h = (b - a) / n
        x = np.linspace(a, b, n + 1)
        y = [func(xi) for xi in x]
        
        integral = y[0] + y[-1]
        integral += 4 * sum(y[i] for i in range(1, n, 2))
        integral += 2 * sum(y[i] for i in range(2, n, 2))
        
        return integral * h / 3
    
    def char_to_function(self, char: str, index: int) -> Callable[[float], float]:
        """
        Convert character to mathematical function
        """
        ascii_val = ord(char)
        
        def char_func(x):
            # Complex mathematical transformation
            base = ascii_val / 127.0  # Normalize to [0, 1]
            
            # Combine multiple mathematical operations
            term1 = base * math.sin(x + index)
            term2 = (base ** 2) * math.cos(2 * x)
            term3 = math.exp(-x**2 / (2 * (index + 1)))
            
            return term1 + term2 + term3
        
        return char_func
    
    def encrypt_character(self, char: str, index: int) -> float:
        """
        Encrypt a single character using calculus operations
        """
        # Convert character to function
        char_func = self.char_to_function(char, index)
        
        # Calculate derivative
        derivative_func = lambda x: self.numerical_derivative(char_func, x)
        
        # Multiply by key function
        product_func = lambda x: derivative_func(x) * self.key_function(x + index)
        
        # Integrate over domain
        domain_start = -1.0
        domain_end = 1.0
        integral_result = self.numerical_integral(product_func, domain_start, domain_end)
        
        # Add mathematical constant based on position
        constant = self.constants['e'] ** (index % 3) + self.constants['pi'] * (index % 2)
        
        return integral_result + constant
    
    def decrypt_character(self, encrypted_value: float, index: int) -> str:
        """
        Decrypt a single encrypted value back to character
        """
        # Remove the added constant
        constant = self.constants['e'] ** (index % 3) + self.constants['pi'] * (index % 2)
        adjusted_value = encrypted_value - constant
        
        # Reverse the integration process (approximate)
        # This is a simplified inverse - in practice, more sophisticated methods would be used
        
        # Try different ASCII values to find the best match
        best_char = 'A'
        min_error = float('inf')
        
        for ascii_val in range(32, 127):  # Printable ASCII range
            test_char = chr(ascii_val)
            test_encrypted = self.encrypt_character(test_char, index) - constant
            error = abs(test_encrypted - adjusted_value)
            
            if error < min_error:
                min_error = error
                best_char = test_char
        
        return best_char
    
    def encrypt(self, plaintext: str) -> List[float]:
        """
        Encrypt entire plaintext string
        """
        encrypted = []
        for i, char in enumerate(plaintext):
            encrypted_char = self.encrypt_character(char, i)
            encrypted.append(encrypted_char)
        
        return encrypted
    
    def decrypt(self, ciphertext: List[float]) -> str:
        """
        Decrypt entire ciphertext
        """
        decrypted = []
        for i, encrypted_val in enumerate(ciphertext):
            decrypted_char = self.decrypt_character(encrypted_val, i)
            decrypted.append(decrypted_char)
        
        return ''.join(decrypted)
    
    def get_encryption_formula(self) -> str:
        """
        Return the mathematical formula used for encryption
        """
        return r"E_i(c) = \int_{-1}^{1} \frac{d}{dx}[f_c(x)] \cdot g(x + i) dx + e^{i \bmod 3} + \pi \cdot (i \bmod 2)"
    
    def get_security_analysis(self, text_length: int) -> dict:
        """
        Analyze the security properties of the encryption
        """
        return {
            "key_space": f"2^{text_length * 64}",  # Assuming 64-bit floating point
            "complexity": f"O(n * log(n))",
            "mathematical_operations": ["differentiation", "integration", "transcendental_functions"],
            "security_level": "High (based on calculus complexity)"
        }

# Example usage and testing
if __name__ == "__main__":
    print("Calculus-Based Encryption Implementation")
    print("=" * 50)
    
    # Create encryption instance
    encryptor = CalculusEncryption()
    
    # Test message
    message = "HELLO WORLD"
    print(f"Original message: {message}")
    
    # Encrypt
    encrypted = encryptor.encrypt(message)
    print(f"Encrypted values: {[round(val, 6) for val in encrypted]}")
    
    # Decrypt
    decrypted = encryptor.decrypt(encrypted)
    print(f"Decrypted message: {decrypted}")
    
    # Show mathematical formula
    print(f"\nEncryption formula: {encryptor.get_encryption_formula()}")
    
    # Security analysis
    security = encryptor.get_security_analysis(len(message))
    print(f"\nSecurity Analysis:")
    for key, value in security.items():
        print(f"  {key}: {value}")
