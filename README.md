# z_view
When activated, the code changes creates a new subfolder called zview and the impedance data is copied and changed there so it can be recognised by the zview program

# Lights_in_the_room

Telegram bot installed on raspberry pi sends the commands to arduino to send IR pulse to turn on the LED strip
Also sends some photos/pics if requested

# Send_gcode_to_raspberry

Sends the generated gcode file to the pi's directory, where grblcontroller can be used

# Plant

Collects information from arduino sensors (humidity and sunlight) and sends it to raspberry pi, where the graph is plotted and sent through telegram bot upon request
