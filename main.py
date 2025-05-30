import tkinter


class BMIAdvisor:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("BMI Advisor")
        self.window.geometry("1270x670")
        self.window.resizable(False, False)

        self.weight_label = tkinter.Label(self.window, text="Weight (kg):")
        self.weight_label.pack(pady=(20, 0))

        self.weight_entry = tkinter.Entry(self.window)
        self.weight_entry.pack(pady=5)

        self.height_label = tkinter.Label(self.window, text="Height (cm):")
        self.height_label.pack(pady=(15, 0))

        self.height_entry = tkinter.Entry(self.window)
        self.height_entry.pack(pady=5)

        self.calculate_button = tkinter.Button(
            self.window,
            text="Calculate BMI",
            command=self.calculate_bmi
        )
        self.calculate_button.pack(pady=15)

        self.result_label = tkinter.Label(
            self.window,
            text="",
            wraplength=320,
            justify="center",
            font=("Arial", 10, "bold")
        )
        self.result_label.pack(pady=10)

        self.window.mainloop()

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height_cm = float(self.height_entry.get())

            if weight <= 0 or height_cm <= 0:
                self.result_label.config(text="Please enter positive values only.")
                return

            height_m = height_cm / 100
            bmi = weight / (height_m ** 2)

            if bmi < 18.5:
                category = "Underweight"
                advice = "Increase your calorie intake and consult a nutritionist."
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
                advice = "Maintain your current lifestyle and stay physically active."
            elif 25 <= bmi < 29.9:
                category = "Overweight"
                advice = "Consider regular exercise and a balanced diet."
            else:
                category = "Obesity"
                advice = "Seek guidance from a healthcare professional for weight management."

            self.result_label.config(
                text=f"Your BMI is {bmi:.2f} ({category})\n{advice}"
            )

        except ValueError:
            self.result_label.config(text="Please enter valid numeric values.")


if __name__ == "__main__":
    BMIAdvisor()