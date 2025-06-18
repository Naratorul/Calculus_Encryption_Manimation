from manim import *
import numpy as np

class CalculusEncryptionAnimation(Scene):
    def construct(self):
        self.logic_intro()
        self.render_mathematical_base()
        self.execute_encryption_transform()
        self.process_visual_mapping()
        self.execute_decryption_transform()
        self.display_algorithm_implementation()
        self.render_complete_system()

    def logic_intro(self):
        primary_title = MathTex(r"\text{Calculus-Based Encryption}", font_size=72)
        primary_title.set_color_by_gradient(BLUE, PURPLE, RED)
        
        secondary_title = MathTex(r"\text{Where Mathematics Meets Cryptography}", font_size=36)
        secondary_title.set_color(GRAY)
        secondary_title.next_to(primary_title, DOWN, buff=0.5)
        
        mathematical_symbols = VGroup()
        symbol_list = [r"\int", r"\frac{d}{dx}", r"\sum", r"\lim", r"\nabla"]
        for i, symbol_tex in enumerate(symbol_list):
            math_symbol = MathTex(symbol_tex, font_size=48)
            math_symbol.set_color(YELLOW)
            angle_position = i * 2 * PI / 5
            math_symbol.move_to(3 * np.array([np.cos(angle_position), np.sin(angle_position), 0]))
            mathematical_symbols.add(math_symbol)
        
        self.play(
            Write(primary_title),
            *[Create(symbol) for symbol in mathematical_symbols],
            run_time=3
        )
        self.play(Write(secondary_title))
        self.wait(2)
        
        self.play(
            FadeOut(primary_title),
            FadeOut(secondary_title),
            FadeOut(mathematical_symbols)
        )

    def render_mathematical_base(self):
        foundation_header = Text("Mathematical Foundation", font_size=48)
        foundation_header.set_color(BLUE)
        foundation_header.to_edge(UP)
        
        self.play(Write(foundation_header))
        
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
        encryption_formula.move_to(UP * 1.5)
        
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
        decryption_formula.move_to(ORIGIN)
        
        key_generation_formula = MathTex(
            r"K = \sum_{n=1}^{\infty} \frac{(-1)^n}{n!} \left(\frac{x}{a}\right)^n",
            font_size=50
        )
        key_generation_formula.set_color(YELLOW)
        key_generation_formula.move_to(DOWN * 1.5)
        
        self.play(Write(encryption_formula), run_time=2)
        self.wait(1)
        self.play(Write(decryption_formula), run_time=2)
        self.wait(1)
        self.play(Write(key_generation_formula), run_time=2)
        
        connection_arrow_1 = Arrow(encryption_formula.get_bottom(), decryption_formula.get_top(), color=YELLOW)
        connection_arrow_2 = Arrow(decryption_formula.get_bottom(), key_generation_formula.get_top(), color=YELLOW)
        
        self.play(Create(connection_arrow_1), Create(connection_arrow_2))
        self.wait(2)
        
        self.play(
            FadeOut(foundation_header),
            FadeOut(encryption_formula),
            FadeOut(decryption_formula),
            FadeOut(key_generation_formula),
            FadeOut(connection_arrow_1),
            FadeOut(connection_arrow_2)
        )

    def execute_encryption_transform(self):
        process_header = Text("Encryption Process", font_size=48)
        process_header.set_color(RED)
        process_header.to_edge(UP)
        
        self.play(Write(process_header))
        
        coordinate_system = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": WHITE}
        )
        coordinate_system.move_to(LEFT * 1)
        
        original_function = coordinate_system.plot(lambda x: x**2, color=BLUE, x_range=[-2, 2])
        original_label = MathTex(r"f(x) = x^2", color=BLUE, font_size=36)
        original_label.move_to(RIGHT * 4 + UP * 2)
        
        key_function = coordinate_system.plot(lambda x: np.sin(2*x), color=GREEN, x_range=[-2, 2])
        key_label = MathTex(r"g(x) = \sin(2x)", color=GREEN, font_size=36)
        key_label.move_to(RIGHT * 4 + UP * 1)
        
        self.play(Create(coordinate_system))
        self.play(Create(original_function), Write(original_label))
        self.play(Create(key_function), Write(key_label))
        
        derivative_function = coordinate_system.plot(lambda x: 2*x, color=PURPLE, x_range=[-2, 2])
        derivative_label = MathTex(r"f'(x) = 2x", color=PURPLE, font_size=36)
        derivative_label.move_to(RIGHT * 4 + ORIGIN)
        
        self.play(Create(derivative_function), Write(derivative_label))
        
        product_function = coordinate_system.plot(lambda x: 2*x * np.sin(2*x), color=ORANGE, x_range=[-2, 2])
        product_label = MathTex(r"f'(x) \cdot g(x) = 2x\sin(2x)", color=ORANGE, font_size=32)
        product_label.move_to(RIGHT * 4 + DOWN * 1)
        
        self.play(
            Transform(derivative_function, product_function),
            Transform(derivative_label, product_label)
        )
        
        encrypted_function = coordinate_system.plot(
            lambda x: -x*np.cos(2*x) + 0.5*np.sin(2*x), 
            color=RED, 
            x_range=[-2, 2]
        )
        encrypted_label = MathTex(
            r"E(x) = \int 2x\sin(2x) dx", 
            color=RED,
            font_size=32
        )
        encrypted_label.move_to(RIGHT * 4 + DOWN * 2)
        
        self.play(
            Transform(product_function, encrypted_function),
            Transform(product_label, encrypted_label)
        )
        
        self.wait(2)
        
        self.play(
            FadeOut(process_header),
            FadeOut(coordinate_system),
            FadeOut(original_function),
            FadeOut(key_function),
            FadeOut(derivative_function),
            FadeOut(product_function),
            FadeOut(original_label),
            FadeOut(key_label),
            FadeOut(derivative_label),
            FadeOut(product_label)
        )

    def process_visual_mapping(self):
        transform_header = Text("Visual Transformation", font_size=48)
        transform_header.set_color(PURPLE)
        transform_header.to_edge(UP)
        
        self.play(Write(transform_header))
        
        plaintext_input = Text("HELLO", font_size=72)
        plaintext_input.set_color(BLUE)
        plaintext_input.move_to(LEFT * 4)
        
        transform_operator = Arrow(LEFT * 2, RIGHT * 2, color=YELLOW, buff=0.5)
        transform_notation = MathTex(r"\mathcal{F}[\cdot]", font_size=48)
        transform_notation.next_to(transform_operator, UP)
        transform_notation.set_color(YELLOW)
        
        ciphertext_output = VGroup()
        encrypted_values_list = [
            MathTex(r"2.718", color=RED),
            MathTex(r"3.141", color=RED),
            MathTex(r"1.414", color=RED),
            MathTex(r"1.732", color=RED),
            MathTex(r"2.236", color=RED)
        ]
        
        for i, value_tex in enumerate(encrypted_values_list):
            value_tex.move_to(RIGHT * 4 + UP * (1 - i * 0.5))
            ciphertext_output.add(value_tex)
        
        self.play(Write(plaintext_input))
        self.play(Create(transform_operator), Write(transform_notation))
        
        for i, char in enumerate(plaintext_input):
            self.play(
                char.animate.set_color(YELLOW).scale(1.2),
                run_time=0.3
            )
            self.play(
                char.animate.set_color(RED).scale(0.8),
                Write(encrypted_values_list[i]),
                run_time=0.5
            )
        
        mathematical_operations = VGroup()
        operation_symbols = [r"+", r"\times", r"\int", r"\frac{d}{dx}"]
        for i, op_symbol in enumerate(operation_symbols):
            operation = MathTex(op_symbol)
            operation.set_color(ORANGE)
            operation.move_to(UP * 2 + RIGHT * (i - 1.5))
            mathematical_operations.add(operation)
        
        self.play(*[Write(op) for op in mathematical_operations])
        self.wait(2)
        self.play(FadeOut(mathematical_operations))
        
        self.wait(2)
        
        self.play(
            FadeOut(transform_header),
            FadeOut(plaintext_input),
            FadeOut(transform_operator),
            FadeOut(transform_notation),
            FadeOut(ciphertext_output)
        )

    def execute_decryption_transform(self):
        decrypt_header = Text("Decryption Process", font_size=48)
        decrypt_header.set_color(GREEN)
        decrypt_header.to_edge(UP)
        
        self.play(Write(decrypt_header))
        
        encrypted_input_data = VGroup()
        input_values = [2.718, 3.141, 1.414, 1.732, 2.236]
        for i, value in enumerate(input_values):
            numerical_display = DecimalNumber(value, num_decimal_places=3, color=RED)
            numerical_display.move_to(LEFT * 4 + UP * (1 - i * 0.5))
            encrypted_input_data.add(numerical_display)
        
        inverse_transform_operator = Arrow(LEFT * 2, RIGHT * 2, color=TEAL, buff=0.5)
        inverse_notation = MathTex(r"\mathcal{F}^{-1}[\cdot]", font_size=48)
        inverse_notation.next_to(inverse_transform_operator, UP)
        inverse_notation.set_color(TEAL)
        
        decrypted_output = Text("HELLO", font_size=72)
        decrypted_output.set_color(BLUE)
        decrypted_output.move_to(RIGHT * 4)
        
        self.play(*[Write(num) for num in encrypted_input_data])
        self.play(Create(inverse_transform_operator), Write(inverse_notation))
        
        inverse_operations = VGroup()
        inverse_operation_symbols = [r"-", r"\div", r"\frac{d}{dx}", r"\int"]
        for i, op_symbol in enumerate(inverse_operation_symbols):
            operation = MathTex(op_symbol)
            operation.set_color(TEAL)
            operation.move_to(UP * 2 + RIGHT * (i - 1.5))
            inverse_operations.add(operation)
        
        self.play(*[Write(op) for op in inverse_operations])
        self.wait(2)
        self.play(FadeOut(inverse_operations))
        
        for i, numerical_value in enumerate(encrypted_input_data):
            self.play(
                numerical_value.animate.set_color(TEAL).scale(1.2),
                run_time=0.3
            )
            self.play(
                numerical_value.animate.set_color(BLUE).scale(0.8),
                run_time=0.5
            )
        
        self.play(Write(decrypted_output))
        
        success_indicator = Text("✓ DECRYPTION SUCCESSFUL", font_size=36, color=GREEN)
        success_indicator.next_to(decrypted_output, DOWN, buff=1)
        self.play(Write(success_indicator))
        
        self.wait(2)
        
        self.play(
            FadeOut(decrypt_header),
            FadeOut(encrypted_input_data),
            FadeOut(inverse_transform_operator),
            FadeOut(inverse_notation),
            FadeOut(decrypted_output),
            FadeOut(success_indicator)
        )

    def display_algorithm_implementation(self):
        code_header = Text("Implementation", font_size=48)
        code_header.set_color(ORANGE)
        code_header.to_edge(UP)
        
        self.play(Write(code_header))
        
        encryption_algorithm = Text(
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
        encryption_algorithm.scale(0.8)
        encryption_algorithm.move_to(LEFT * 3)
        
        decryption_algorithm = Text(
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
        decryption_algorithm.scale(0.8)
        decryption_algorithm.move_to(RIGHT * 3)
        
        self.play(Write(encryption_algorithm), run_time=3)
        self.play(Write(decryption_algorithm), run_time=3)
        
        highlight_encryption = Rectangle(width=2, height=0.5, color=YELLOW)
        highlight_encryption.move_to(encryption_algorithm.get_center() + UP * 0.5)
        
        highlight_decryption = Rectangle(width=2, height=0.5, color=TEAL)
        highlight_decryption.move_to(decryption_algorithm.get_center() + UP * 0.5)
        
        self.play(Create(highlight_encryption), Create(highlight_decryption))
        self.wait(2)
        
        self.play(
            FadeOut(code_header),
            FadeOut(encryption_algorithm),
            FadeOut(decryption_algorithm),
            FadeOut(highlight_encryption),
            FadeOut(highlight_decryption)
        )

    def render_complete_system(self):
        final_header = Text("Complete Demonstration", font_size=48)
        final_header.set_color_by_gradient(RED, BLUE, GREEN)
        final_header.to_edge(UP)
        
        self.play(Write(final_header))
        
        input_container = Rectangle(width=2, height=1, color=BLUE)
        input_label = Text("INPUT", font_size=24, color=WHITE)
        input_label.move_to(input_container.get_center())
        input_module = VGroup(input_container, input_label)
        input_module.move_to(LEFT * 5)
        
        mathematical_processor = Rectangle(width=3, height=2, color=PURPLE)
        mathematical_formulas = VGroup(
            MathTex(r"\frac{d}{dx}", font_size=20),
            MathTex(r"\int", font_size=20),
            MathTex(r"\sum", font_size=20),
            MathTex(r"e^x", font_size=20)
        )
        mathematical_formulas.arrange(DOWN, buff=0.1)
        mathematical_formulas.move_to(mathematical_processor.get_center())
        processor_module = VGroup(mathematical_processor, mathematical_formulas)
        processor_module.move_to(ORIGIN)
        
        output_container = Rectangle(width=2, height=1, color=RED)
        output_label = Text("OUTPUT", font_size=24, color=WHITE)
        output_label.move_to(output_container.get_center())
        output_module = VGroup(output_container, output_label)
        output_module.move_to(RIGHT * 5)
        
        flow_arrow_1 = Arrow(input_module.get_right(), processor_module.get_left(), color=YELLOW)
        flow_arrow_2 = Arrow(processor_module.get_right(), output_module.get_left(), color=YELLOW)
        
        security_indicators = VGroup()
        for i in range(8):
            security_symbol = MathTex(r"\infty", font_size=20, color=YELLOW)
            angle_pos = i * PI / 4
            security_symbol.move_to(2 * np.array([np.cos(angle_pos), np.sin(angle_pos), 0]))
            security_indicators.add(security_symbol)
        
        self.play(
            Create(input_module),
            Create(processor_module),
            Create(output_module)
        )
        self.play(Create(flow_arrow_1), Create(flow_arrow_2))
        self.play(*[Create(symbol) for symbol in security_indicators])
        
        self.wait(2)
        
        final_security_equation = MathTex(
            r"\text{Security} = \lim_{n \to \infty} \sum_{k=1}^{n} \frac{1}{k!} \left(\frac{\partial^k f}{\partial x^k}\right)^2",
            font_size=40
        )
        final_security_equation.set_color_by_gradient(BLUE, PURPLE, RED)
        final_security_equation.next_to(processor_module, DOWN, buff=1)
        
        self.play(Write(final_security_equation), run_time=3)
        
        conclusion_statement = Text("Mathematics + Cryptography = Unbreakable Security", font_size=32)
        conclusion_statement.set_color_by_gradient(YELLOW, ORANGE, RED)
        conclusion_statement.to_edge(DOWN)
        
        self.play(Write(conclusion_statement))
        self.wait(3)
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )
