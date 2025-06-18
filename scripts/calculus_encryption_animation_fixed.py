from manim import *
import numpy as np

class CalculusEncryptionAnimation(Scene):
    def construct(self):
        # Title sequence
        self.logic_intro()
        
        # Mathematical foundation
        self.render_mathematical_base()
        
        # Encryption process
        self.execute_encryption_transform()
        
        # Visual transformation
        self.process_visual_mapping()
        
        # Decryption process
        self.execute_decryption_transform()
        
        # Code implementation
        self.display_algorithm_implementation()
        
        # Final demonstration
        self.render_complete_system()

    def logic_intro(self):
        # Create title with mathematical styling
        title = MathTex(r"\text{Calculus-Based Encryption}", font_size=72)
        title.set_color_by_gradient(BLUE, PURPLE, RED)
        
        subtitle = MathTex(r"\text{Where Mathematics Meets Cryptography}", font_size=36)
        subtitle.set_color(GRAY)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Animated mathematical symbols floating around
        symbols = VGroup()
        for i, symbol in enumerate([r"\int", r"\frac{d}{dx}", r"\sum", r"\lim", r"\nabla"]):
            math_symbol = MathTex(symbol, font_size=48)
            math_symbol.set_color(YELLOW)
            angle = i * 2 * PI / 5
            math_symbol.move_to(3 * np.array([np.cos(angle), np.sin(angle), 0]))
            symbols.add(math_symbol)
        
        self.play(
            Write(title),
            *[Create(symbol) for symbol in symbols],
            run_time=3
        )
        self.play(Write(subtitle))
        
        # Rotate symbols
        self.play(FadeOut(symbols))
        
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
        )

    def render_mathematical_base(self):
        # Foundation title
        foundation_title = Text("Mathematical Foundation", font_size=48)
        foundation_title.set_color(BLUE)
        foundation_title.to_edge(UP)
        
        self.play(Write(foundation_title))
        
        # Core encryption formula
        encryption_formula = MathTex(
            r"E(x) = \int_0^x f'(t) \cdot g(t) \, dt + C",
            font_size=60
        )
        encryption_formula.set_color_by_tex_to_color_map({
            "E(x)": RED,
            "f'(t)": BLUE,
            "g(t)": GREEN,
            "C": PURPLE
        })
        
        # Decryption formula
        decryption_formula = MathTex(
            r"D(y) = \frac{d}{dx}\left[\frac{y - C}{g(x)}\right]",
            font_size=60
        )
        decryption_formula.set_color_by_tex_to_color_map({
            "D(y)": RED,
            "y": ORANGE,
            "C": PURPLE,
            "g(x)": GREEN
        })
        decryption_formula.next_to(encryption_formula, DOWN, buff=1)
        
        # Key generation formula
        key_formula = MathTex(
            r"K = \sum_{n=1}^{\infty} \frac{(-1)^n}{n!} \left(\frac{x}{a}\right)^n",
            font_size=50
        )
        key_formula.set_color(YELLOW)
        key_formula.next_to(decryption_formula, DOWN, buff=1)
        
        self.play(Write(encryption_formula), run_time=2)
        self.wait(1)
        self.play(Write(decryption_formula), run_time=2)
        self.wait(1)
        self.play(Write(key_formula), run_time=2)
        
        # Highlight relationships
        arrow1 = Arrow(encryption_formula.get_bottom(), decryption_formula.get_top(), color=YELLOW)
        arrow2 = Arrow(decryption_formula.get_bottom(), key_formula.get_top(), color=YELLOW)
        
        self.play(Create(arrow1), Create(arrow2))
        self.wait(2)
        
        self.play(
            FadeOut(foundation_title),
            FadeOut(encryption_formula),
            FadeOut(decryption_formula),
            FadeOut(key_formula),
            FadeOut(arrow1),
            FadeOut(arrow2)
        )

    def execute_encryption_transform(self):
        # Process title
        process_title = Text("Encryption Process", font_size=48)
        process_title.set_color(RED)
        process_title.to_edge(UP)
        
        self.play(Write(process_title))
        
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": WHITE}
        )
        
        # Original function (plaintext)
        original_func = axes.plot(lambda x: x**2, color=BLUE, x_range=[-2, 2])
        original_label = MathTex(r"f(x) = x^2", color=BLUE).next_to(axes, UP, aligned_edge=LEFT)
        
        # Key function
        key_func = axes.plot(lambda x: np.sin(2*x), color=GREEN, x_range=[-2, 2])
        key_label = MathTex(r"g(x) = \sin(2x)", color=GREEN).next_to(original_label, DOWN)
        
        self.play(Create(axes))
        self.play(Create(original_func), Write(original_label))
        self.play(Create(key_func), Write(key_label))
        
        # Show derivative
        derivative_func = axes.plot(lambda x: 2*x, color=PURPLE, x_range=[-2, 2])
        derivative_label = MathTex(r"f'(x) = 2x", color=PURPLE).next_to(key_label, DOWN)
        
        self.play(Create(derivative_func), Write(derivative_label))
        
        # Show product
        product_func = axes.plot(lambda x: 2*x * np.sin(2*x), color=ORANGE, x_range=[-2, 2])
        product_label = MathTex(r"f'(x) \cdot g(x) = 2x\sin(2x)", color=ORANGE).next_to(derivative_label, DOWN)
        
        self.play(
            Transform(derivative_func, product_func),
            Transform(derivative_label, product_label)
        )
        
        # Show integration (encryption)
        encrypted_func = axes.plot(
            lambda x: -x*np.cos(2*x) + 0.5*np.sin(2*x), 
            color=RED, 
            x_range=[-2, 2]
        )
        encrypted_label = MathTex(
            r"E(x) = \int 2x\sin(2x) dx", 
            color=RED
        ).next_to(product_label, DOWN)
        
        self.play(
            Transform(product_func, encrypted_func),
            Transform(product_label, encrypted_label)
        )
        
        self.wait(2)
        
        self.play(
            FadeOut(process_title),
            FadeOut(axes),
            FadeOut(original_func),
            FadeOut(key_func),
            FadeOut(derivative_func),
            FadeOut(product_func),
            FadeOut(original_label),
            FadeOut(key_label),
            FadeOut(derivative_label),
            FadeOut(product_label),
            FadeOut(encrypted_func),
            FadeOut(encrypted_label)
        )

    def process_visual_mapping(self):
        # Transformation title
        transform_title = Text("Visual Transformation", font_size=48)
        transform_title.set_color(PURPLE)
        transform_title.to_edge(UP)
        
        self.play(Write(transform_title))
        
        # Create text to encrypt
        plaintext = Text("HELLO", font_size=72)
        plaintext.set_color(BLUE)
        plaintext.move_to(LEFT * 4)
        
        # Create mathematical transformation
        transform_arrow = Arrow(LEFT * 2, RIGHT * 2, color=YELLOW, buff=0.5)
        transform_label = MathTex(r"\mathcal{F}[\cdot]", font_size=48)
        transform_label.next_to(transform_arrow, UP)
        transform_label.set_color(YELLOW)
        
        # Encrypted result (mathematical representation)
        ciphertext = VGroup()
        encrypted_values = [
            MathTex(r"2.718", color=RED),
            MathTex(r"3.141", color=RED),
            MathTex(r"1.414", color=RED),
            MathTex(r"1.732", color=RED),
            MathTex(r"2.236", color=RED)
        ]
        
        for i, val in enumerate(encrypted_values):
            val.move_to(RIGHT * 4 + UP * (1 - i * 0.5))
            ciphertext.add(val)
        
        self.play(Write(plaintext))
        self.play(Create(transform_arrow), Write(transform_label))
        
        # Animate transformation
        for i, char in enumerate(plaintext):
            self.play(
                char.animate.set_color(YELLOW).scale(1.2),
                run_time=0.3
            )
            self.play(
                char.animate.set_color(RED).scale(0.8),
                Write(encrypted_values[i]),
                run_time=0.5
            )
        
        # Show mathematical operations
        operations = VGroup()
        for i in range(4):
            op = MathTex([r"+", r"\times", r"\int", r"\frac{d}{dx}"][i])
            op.set_color(ORANGE)
            op.move_to(UP * 2 + RIGHT * (i - 1.5))
            operations.add(op)
        
        self.play(*[Write(op) for op in operations])
        self.play(FadeOut(operations))
        
        self.wait(2)
        
        self.play(
            FadeOut(transform_title),
            FadeOut(plaintext),
            FadeOut(transform_arrow),
            FadeOut(transform_label),
            FadeOut(ciphertext),
        )

    def execute_decryption_transform(self):
        # Decryption title
        decrypt_title = Text("Decryption Process", font_size=48)
        decrypt_title.set_color(GREEN)
        decrypt_title.to_edge(UP)
        
        self.play(Write(decrypt_title))
        
        # Reverse transformation
        encrypted_input = VGroup()
        for i, val in enumerate([2.718, 3.141, 1.414, 1.732, 2.236]):
            num = DecimalNumber(val, num_decimal_places=3, color=RED)
            num.move_to(LEFT * 4 + UP * (1 - i * 0.5))
            encrypted_input.add(num)
        
        # Inverse transformation arrow
        inverse_arrow = Arrow(LEFT * 2, RIGHT * 2, color=TEAL, buff=0.5)
        inverse_label = MathTex(r"\mathcal{F}^{-1}[\cdot]", font_size=48)
        inverse_label.next_to(inverse_arrow, UP)
        inverse_label.set_color(TEAL)
        
        # Decrypted result
        decrypted_text = Text("HELLO", font_size=72)
        decrypted_text.set_color(BLUE)
        decrypted_text.move_to(RIGHT * 4)
        
        self.play(*[Write(num) for num in encrypted_input])
        self.play(Create(inverse_arrow), Write(inverse_label))
        
        # Show inverse mathematical operations
        inverse_ops = VGroup()
        operations_symbols = [r"-", r"\div", r"\frac{d}{dx}", r"\int"]
        for i, op_symbol in enumerate(operations_symbols):
            op = MathTex(op_symbol)
            op.set_color(TEAL)
            op.move_to(UP * 2 + RIGHT * (i - 1.5))
            inverse_ops.add(op)
        
        self.play(*[Write(op) for op in inverse_ops])
        self.play(FadeOut(inverse_ops))
        
        # Animate decryption
        for i, num in enumerate(encrypted_input):
            self.play(
                num.animate.set_color(TEAL).scale(1.2),
                run_time=0.3
            )
            self.play(
                num.animate.set_color(BLUE).scale(0.8),
                run_time=0.5
            )
        
        self.play(Write(decrypted_text))
        
        # Success indicator
        success = Text("✓ DECRYPTION SUCCESSFUL", font_size=36, color=GREEN)
        success.next_to(decrypted_text, DOWN, buff=1)
        self.play(Write(success))
        
        self.wait(2)
        
        self.play(
            FadeOut(decrypt_title),
            FadeOut(encrypted_input),
            FadeOut(inverse_arrow),
            FadeOut(inverse_label),
            FadeOut(decrypted_text),
            FadeOut(success)
        )

    def display_algorithm_implementation(self):
        # Code title
        code_title = Text("Implementation", font_size=48)
        code_title.set_color(ORANGE)
        code_title.to_edge(UP)
        
        self.play(Write(code_title))
        
        # Create simplified code display using Text instead of Code
        encryption_code = Text(
            """def encrypt(plaintext, key_func):
    result = []
    for i, char in enumerate(plaintext):
        val = ord(char)
        derivative = differentiate(val, i)
        integral = integrate(derivative * key_func(i))
        encrypted = integral + math.e ** (i % 3)
        result.append(encrypted)
    return result""",
            font_size=20,
            color=WHITE,
            font="Courier"
        )
        encryption_code.scale(0.8)
        encryption_code.move_to(LEFT * 3)
        
        decryption_code = Text(
            """def decrypt(ciphertext, key_func):
    result = []
    for i, encrypted_val in enumerate(ciphertext):
        val = encrypted_val - math.e ** (i % 3)
        derivative = differentiate(val / key_func(i))
        original = integrate_inverse(derivative)
        char = chr(int(original))
        result.append(char)
    return ''.join(result)""",
            font_size=20,
            color=WHITE,
            font="Courier"
        )
        decryption_code.scale(0.8)
        decryption_code.move_to(RIGHT * 3)
        
        self.play(Write(encryption_code), run_time=3)
        self.play(Write(decryption_code), run_time=3)
        
        # Highlight key mathematical operations with rectangles
        highlight_box1 = Rectangle(width=2, height=0.5, color=YELLOW)
        highlight_box1.move_to(encryption_code.get_center() + UP * 0.5)
        
        highlight_box2 = Rectangle(width=2, height=0.5, color=TEAL)
        highlight_box2.move_to(decryption_code.get_center() + UP * 0.5)
        
        self.play(Create(highlight_box1), Create(highlight_box2))
        self.wait(2)
        
        self.play(
            FadeOut(code_title),
            FadeOut(encryption_code),
            FadeOut(decryption_code),
            FadeOut(highlight_box1),
            FadeOut(highlight_box2)
        )

    def render_complete_system(self):
        # Final title
        final_title = Text("Complete Demonstration", font_size=48)
        final_title.set_color_by_gradient(RED, BLUE, GREEN)
        final_title.to_edge(UP)
        
        self.play(Write(final_title))
        
        # Create a comprehensive flow diagram
        # Input
        input_box = Rectangle(width=2, height=1, color=BLUE)
        input_text = Text("INPUT", font_size=24, color=WHITE)
        input_text.move_to(input_box.get_center())
        input_group = VGroup(input_box, input_text)
        input_group.move_to(LEFT * 5)
        
        # Mathematical transformation
        math_box = Rectangle(width=3, height=2, color=PURPLE)
        math_formulas = VGroup(
            MathTex(r"\frac{d}{dx}", font_size=20),
            MathTex(r"\int", font_size=20),
            MathTex(r"\sum", font_size=20),
            MathTex(r"e^x", font_size=20)
        )
        math_formulas.arrange(DOWN, buff=0.1)
        math_formulas.move_to(math_box.get_center())
        math_group = VGroup(math_box, math_formulas)
        math_group.move_to(ORIGIN)
        
        # Output
        output_box = Rectangle(width=2, height=1, color=RED)
        output_text = Text("OUTPUT", font_size=24, color=WHITE)
        output_text.move_to(output_box.get_center())
        output_group = VGroup(output_box, output_text)
        output_group.move_to(RIGHT * 5)
        
        # Arrows
        arrow1 = Arrow(input_group.get_right(), math_group.get_left(), color=YELLOW)
        arrow2 = Arrow(math_group.get_right(), output_group.get_left(), color=YELLOW)
        
        # Security indicators
        security_symbols = VGroup()
        for i in range(8):
            symbol = MathTex(r"\infty", font_size=20, color=YELLOW)
            angle = i * PI / 4
            symbol.move_to(2 * np.array([np.cos(angle), np.sin(angle), 0]))
            security_symbols.add(symbol)
        
        self.play(
            Create(input_group),
            Create(math_group),
            Create(output_group)
        )
        self.play(Create(arrow1), Create(arrow2))
        self.play(*[Create(symbol) for symbol in security_symbols])
        
        # Rotate security symbols
        self.play(FadeOut(security_symbols))
        
        # Final mathematical equation
        final_equation = MathTex(
            r"\text{Security} = \lim_{n \to \infty} \sum_{k=1}^{n} \frac{1}{k!} \left(\frac{\partial^k f}{\partial x^k}\right)^2",
            font_size=40
        )
        final_equation.set_color_by_gradient(BLUE, PURPLE, RED)
        final_equation.next_to(math_group, DOWN, buff=1)
        
        self.play(Write(final_equation), run_time=3)
        
        # Conclusion
        conclusion = Text("Mathematics + Cryptography = Unbreakable Security", font_size=32)
        conclusion.set_color_by_gradient(YELLOW, ORANGE, RED)
        conclusion.to_edge(DOWN)
        
        self.play(Write(conclusion))
        self.wait(3)
        
        # Final fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )
