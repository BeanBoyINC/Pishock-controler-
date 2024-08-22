import dearpygui.dearpygui as dpg

def create_gui(pishock):
    def shock_command():
        intensity = dpg.get_value("shock_intensity")
        duration = dpg.get_value("shock_duration")
        pishock.shock(intensity, duration)

    def vibrate_command():
        intensity = dpg.get_value("vibrate_intensity")
        duration = dpg.get_value("vibrate_duration")
        pishock.vibrate(intensity, duration)

    def beep_command():
        duration = dpg.get_value("beep_duration")
        pishock.beep(duration)

    def pulse_command():
        min_intensity = dpg.get_value("pulse_min_intensity")
        max_intensity = dpg.get_value("pulse_max_intensity")
        duration = dpg.get_value("pulse_duration")
        interval = dpg.get_value("pulse_interval")
        count = dpg.get_value("pulse_count")
        pishock.pulse(min_intensity, max_intensity, duration, interval, count)

    def random_command():
        duration = dpg.get_value("random_duration")
        pishock.random_command(duration)

    # Create Dear PyGui context
    dpg.create_context()

    # Create the main window with specified size
    with dpg.window(label="PiShock Controller", width=1040, height=800, autosize=False):
        # Create two columns for layout
        with dpg.group(horizontal=True):
            # Left Column
            with dpg.child_window(width=500, height=780):  # Increased width
                dpg.add_text("Shock Settings", bullet=True)
                with dpg.group():
                    dpg.add_slider_int(label="Intensity (1-100)", tag="shock_intensity", min_value=1, max_value=100, default_value=50, width=350)
                    dpg.add_slider_int(label="Duration (1-15 sec)", tag="shock_duration", min_value=1, max_value=15, default_value=5, width=350)
                    dpg.add_button(label="Apply Shock", callback=shock_command, width=650, height=50)

                dpg.add_separator()

                dpg.add_text("Vibrate Settings", bullet=True)
                with dpg.group():
                    dpg.add_slider_int(label="Intensity (1-100)", tag="vibrate_intensity", min_value=1, max_value=100, default_value=50, width=350)
                    dpg.add_slider_int(label="Duration (1-15 sec)", tag="vibrate_duration", min_value=1, max_value=15, default_value=5, width=350)
                    dpg.add_button(label="Apply Vibration", callback=vibrate_command, width=650, height=50)

                dpg.add_separator()

                dpg.add_text("Beep Settings", bullet=True)
                with dpg.group():
                    dpg.add_slider_int(label="Duration (1-15 sec)", tag="beep_duration", min_value=1, max_value=15, default_value=5, width=350)
                    dpg.add_button(label="Apply Beep", callback=beep_command, width=650, height=50)

            # Right Column
            with dpg.child_window(width=500, height=780):  # Increased width
                dpg.add_text("Pulse Settings", bullet=True)
                with dpg.group():
                    dpg.add_slider_int(label="Min Intensity (1-100)", tag="pulse_min_intensity", min_value=1, max_value=100, default_value=10, width=320)
                    dpg.add_slider_int(label="Max Intensity (1-100)", tag="pulse_max_intensity", min_value=1, max_value=100, default_value=90, width=320)
                    dpg.add_slider_int(label="Duration per pulse (1-15 sec)", tag="pulse_duration", min_value=1, max_value=15, default_value=5, width=320)
                    dpg.add_slider_float(label="Interval between pulses (sec)", tag="pulse_interval", min_value=0.1, max_value=10.0, default_value=1.0, width=320)
                    dpg.add_slider_int(label="Number of pulses", tag="pulse_count", min_value=1, max_value=50, default_value=5, width=320)
                    dpg.add_button(label="Apply Pulse", callback=pulse_command, width=550, height=50)

                dpg.add_separator()

                dpg.add_text("Random Command", bullet=True)
                with dpg.group():
                    dpg.add_slider_int(label="Duration (1-15 sec)", tag="random_duration", min_value=1, max_value=15, default_value=5, width=350)
                    dpg.add_button(label="Apply Random", callback=random_command, width=550, height=50)

                # Plot Controls
                dpg.add_separator()
                dpg.add_text("Intensity Graph", bullet=True)
                with dpg.plot(label="Intensity vs Time", height=300, width=460):
                    dpg.add_plot_legend()
                    dpg.add_plot_axis(dpg.mvXAxis, label="Time (s)")
                    dpg.add_plot_axis(dpg.mvYAxis, label="Intensity")

    # Create the viewport with the specified size
    dpg.create_viewport(title='PiShock Controller', width=1040, height=800)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
