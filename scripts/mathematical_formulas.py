"""
Mathematical formulas and LaTeX representations for the calculus encryption
"""

# Core encryption formulas
ENCRYPTION_FORMULAS = {
    "basic_encryption": r"E(x) = \int_0^x f'(t) \cdot g(t) \, dt + C",
    "advanced_encryption": r"E(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} \left(\frac{d^n f}{dx^n}\right) \cdot g^{(n)}(x)",
    "key_generation": r"K(x) = e^{-x^2/2} \cdot \prod_{k=1}^{n} \left(1 + \frac{x^k}{k!}\right)",
    "security_measure": r"S = \lim_{n \to \infty} \left|\frac{\partial^n E}{\partial x^n}\right| \cdot \left|\frac{\partial^n K}{\partial x^n}\right|"
}

DECRYPTION_FORMULAS = {
    "basic_decryption": r"D(y) = \frac{d}{dx}\left[\frac{y - C}{g(x)}\right]",
    "inverse_transform": r"D(y) = \mathcal{L}^{-1}\left\{\frac{Y(s) - C/s}{G(s)}\right\}",
    "series_expansion": r"D(y) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \left(\frac{y - C}{g(x)}\right)^n"
}

# Complexity analysis
COMPLEXITY_FORMULAS = {
    "time_complexity": r"T(n) = O\left(n \cdot \log n \cdot \sum_{k=1}^{n} \frac{1}{k!}\right)",
    "space_complexity": r"S(n) = O\left(n^2 \cdot \int_0^n e^{-t^2} dt\right)",
    "security_strength": r"\text{Strength} = 2^{\sum_{i=1}^{n} \lfloor \log_2(f_i!) \rfloor}"
}

# Implementation constants
MATHEMATICAL_CONSTANTS = {
    "euler": 2.718281828459045,
    "pi": 3.141592653589793,
    "golden_ratio": 1.618033988749895,
    "sqrt_2": 1.4142135623730951,
    "sqrt_3": 1.7320508075688772
}

def get_latex_formula(category, formula_name):
    """Get LaTeX representation of a formula"""
    formulas = {
        "encryption": ENCRYPTION_FORMULAS,
        "decryption": DECRYPTION_FORMULAS,
        "complexity": COMPLEXITY_FORMULAS
    }
    
    return formulas.get(category, {}).get(formula_name, "Formula not found")

def generate_key_sequence(n, base_constant="euler"):
    """Generate a mathematical key sequence"""
    base = MATHEMATICAL_CONSTANTS.get(base_constant, 2.718281828459045)
    sequence = []
    
    for i in range(1, n + 1):
        # Complex mathematical transformation
        value = (base ** (i % 5)) * (i ** 0.5) + ((-1) ** i) / (i + 1)
        sequence.append(round(value, 6))
    
    return sequence

# Example usage and test functions
if __name__ == "__main__":
    print("Calculus Encryption Mathematical Formulas")
    print("=" * 50)
    
    print("\nEncryption Formulas:")
    for name, formula in ENCRYPTION_FORMULAS.items():
        print(f"{name}: {formula}")
    
    print("\nDecryption Formulas:")
    for name, formula in DECRYPTION_FORMULAS.items():
        print(f"{name}: {formula}")
    
    print("\nComplexity Analysis:")
    for name, formula in COMPLEXITY_FORMULAS.items():
        print(f"{name}: {formula}")
    
    print("\nSample Key Sequence:")
    key_seq = generate_key_sequence(10)
    print(key_seq)
