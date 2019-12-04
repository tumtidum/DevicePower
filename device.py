"""Device Power Consumption v0.0.1 - Python 3.7 - by tumtidum.

Calculate the energy cost of an electrical device based on the
power in Watt and the (average) amount of time it is active during
a 24 hour day.

As default this script uses the average electricity tariff from The
Netherlands as was in 2019, of course this value can be modified to
correspondent with your own region or energy supplier.

"""

from tkinter import ttk, Tk, Frame, StringVar, N, W, E, S


class App(Frame):
    """Main application (tkinter GUI)."""

    def __init__(self, root):
        """Summary here."""
        Frame.__init__(self, root)

        def only_numbers_i(char):
            """Restrict the input to numbers only."""
            return char.isdigit()

        def only_numbers_f(char):
            """Restrict the input to only numbers including floats."""
            try:
                float(char)
            except ValueError:
                return False
            return True

        def calculate(*args):
            """All calculations.

            Parameters
            ----------
            *args : integer, float
                Power in Watt.
                Time in hours and minutes.
                Electricity tariff.

            Returns
            -------
            integer
                Kilo Watt hours per year.
                Costs in Euros per day, week month and year.

            """
            try:
                watt = int(power.get())
                hour = int(hours.get())
                minute = int(minutes.get())
                total_hours = float(hour + ((1 / 60) * minute))
                tariff = float(average_tariff.get())
                # Calculation of kWh over a year.
                kwh = ((watt * total_hours * 365) / 1000)
                kwhperyear.set("%0.1f" % kwh)
                # Calculation of the costs.
                cost = (kwh * tariff)
                year_price.set(("%0.2f" % cost) + "   ")
                day_cost = (cost / 365)
                day_price.set("%0.5f" % day_cost)
                month_cost = (cost / 12)
                month_price.set(("%0.3f" % month_cost) + "  ")
                week_cost = (day_cost * 7)
                week_price.set(("%0.4f" % week_cost) + " ")
            except ValueError:
                root.bell()
                pass

        # Statements & variables.
        power = StringVar()
        hours = StringVar()
        minutes = StringVar()
        minutes.set(0)
        average_tariff = StringVar()
        # Default electricity tariff.
        average_tariff.set(0.2173)
        day_price = StringVar()
        week_price = StringVar()
        month_price = StringVar()
        year_price = StringVar()
        kwhperyear = StringVar()

        # Frames.
        # Root frame.
        root_frame = ttk.Frame(
            root,
            padding="6 12 6 8"
            )
        root_frame.grid(
            column=0,
            row=0,
            sticky=(N, W, E, S)
            )
        # Input frame.
        input_frame = ttk.Labelframe(
            root_frame,
            text="Device",
            padding="12 10 10 10"
            )
        input_frame.grid(
            column=0,
            row=0,
            sticky=(N, W, S)
            )
        for child in input_frame.winfo_children():
            child.grid_configure(
                padx=2,
                pady=2
                )
        # Power frame.
        power_frame = ttk.Frame(
            input_frame,
            padding="0 0 0 0"
            )
        power_frame.grid(
            column=0,
            row=0,
            sticky=W
            )
        # Time frame.
        time_frame = ttk.Frame(
            input_frame,
            padding="0 16 0 0"
            )
        time_frame.grid(
            column=0,
            row=1,
            sticky=W
            )
        # Tariff frame.
        tariff_frame = ttk.Frame(
            input_frame,
            padding="0 16 0 0"
            )
        tariff_frame.grid(
            column=0,
            row=2,
            sticky=W
            )
        # Output frame.
        output_frame = ttk.Labelframe(
            root_frame,
            text="Power consumption & cost",
            padding="12 31 10 10"
            )
        output_frame.grid(
            column=1,
            row=0,
            sticky=(N, W, E, S)
            )
        for child in output_frame.winfo_children():
            child.grid_configure(
                padx=1,
                pady=1
                )

        # Key binds and validation for input.
        root.bind('<KP_Enter>', calculate)
        root.bind('<Return>', calculate)
        validation_i = root_frame.register(only_numbers_i)
        validation_f = root_frame.register(only_numbers_f)

        # Content
        # Calculate button.
        ttk.Button(
            root_frame,
            text="Calculate",
            command=calculate
            ).grid(
                column=0,
                row=1,
                columnspan=2,
                padx=12,
                pady=4,
                sticky=(W, E)
                )

        # Power text label.
        ttk.Label(
            power_frame,
            text="Power",
            font="-weight bold"
            ).grid(
                column=0,
                row=0,
                columnspan=2,
                sticky=W
                )
        # Power entry.
        power_entry = ttk.Entry(
            power_frame,
            width=6,
            textvariable=power,
            validate='key',
            validatecommand=(validation_i, '%S')
            )
        power_entry.grid(
            column=0,
            row=1,
            sticky=W
            )
        power_entry.focus()
        # Watt text label.
        ttk.Label(
            power_frame,
            text="Watt"
            ).grid(
                column=1,
                row=1,
                sticky=W
                )

        # Active per day text label.
        ttk.Label(
            time_frame,
            text="Active per day",
            font="-weight bold"
            ).grid(
                column=0,
                row=0,
                columnspan=40,
                sticky=W
                )
        # Hours entry.
        hours_entry = ttk.Entry(
            time_frame,
            width=2,
            textvariable=hours,
            validate='key',
            validatecommand=(validation_i, '%S')
            )
        hours_entry.grid(
            column=0,
            row=1,
            sticky=W
            )
        # Hours text label.
        ttk.Label(
            time_frame,
            text="hours"
            ).grid(
                column=1,
                row=1,
                sticky=W
                )
        # Minutes entry.
        minutes_entry = ttk.Entry(
            time_frame,
            width=2,
            textvariable=minutes,
            validate='key',
            validatecommand=(validation_i, '%S')
            )
        minutes_entry.grid(
            column=0,
            row=2,
            sticky=W
            )
        # Minutes text label.
        ttk.Label(
            time_frame,
            text="minutes"
            ).grid(
                column=1,
                row=2,
                sticky=W
                )

        # Electricity tariff text label.
        ttk.Label(
            tariff_frame,
            text="Electricity tariff",
            font="-weight bold"
            ).grid(
                column=0,
                row=0,
                columnspan=2,
                sticky=W
                )
        # Average tariff entry.
        average_tariff_entry = ttk.Entry(
            tariff_frame,
            width=6,
            textvariable=average_tariff,
            validate='key',
            validatecommand=(validation_f, '%P')
            )
        average_tariff_entry.grid(
            column=0,
            row=1,
            sticky=W
            )
        # Euro per kWh text label.
        ttk.Label(
            tariff_frame,
            text="\u20AC per kWh"
            ).grid(
                column=1,
                row=1,
                sticky=W
                )

        # Output kWh per year.
        ttk.Label(
            output_frame,
            textvariable=kwhperyear,
            font=("courier", "0", "bold")
            ).grid(
                column=0,
                row=0,
                sticky=(E, S)
                )
        # kWh per year text label.
        ttk.Label(
            output_frame,
            text=" kWh per year"
            ).grid(
                column=1,
                row=0,
                sticky=W
                )
        # Empty row text label.
        ttk.Label(
            output_frame,
            text="\t\t\t"
            ).grid(
                column=0,
                row=1,
                columnspan=2
                )
        # Output day price.
        ttk.Label(
            output_frame,
            textvariable=day_price,
            font=("courier", "0", "bold")
            ).grid(
                column=0,
                row=2,
                sticky=(E, S)
                )
        # Euro per day text label.
        ttk.Label(
            output_frame,
            text=" \u20AC  per day"
            ).grid(
                column=1,
                row=2,
                sticky=W
                )
        # Output week price.
        ttk.Label(
            output_frame,
            textvariable=week_price,
            font=("courier", "0", "bold")
            ).grid(
                column=0,
                row=3,
                sticky=(E, S)
                )
        # Euro per week text label.
        ttk.Label(
            output_frame,
            text=" \u20AC  per week"
            ).grid(
                column=1,
                row=3,
                sticky=W
                )
        # Output month price.
        ttk.Label(
            output_frame,
            textvariable=month_price,
            font=("courier", "0", "bold")
            ).grid(
                column=0,
                row=4,
                sticky=(E, S)
                )
        # Euro per month text label.
        ttk.Label(
            output_frame,
            text=" \u20AC  per month"
            ).grid(
                column=1,
                row=4,
                sticky=W
                )
        # Output year price.
        ttk.Label(
            output_frame,
            textvariable=year_price,
            font=("courier", "0", "bold")
            ).grid(
                column=0,
                row=5,
                sticky=(E, S)
                )
        # Euro per year text label.
        ttk.Label(
            output_frame,
            text=" \u20AC  per year"
            ).grid(
                column=1,
                row=5,
                sticky=W
                )


# Now, power up!
if __name__ == '__main__':
    root = Tk()
    root.title('Device Power Consumption v0.0.1')
    # Place window somewhere near the centre on the desktop.
    screen_width = str(int(root.winfo_screenwidth() / 2 - 198))
    screen_height = str(int(root.winfo_screenheight() / 2 - 200))
    desktop = '-' + screen_width + '+' + screen_height
    root.geometry(desktop)
    app = App(root)
    root.mainloop()
