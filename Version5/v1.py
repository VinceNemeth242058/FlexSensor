import serial
from plotter import RealTimePlot

# Initialize serial communication
ser = serial.Serial("COM4", baudrate=9600, timeout=1)

# Set up the moving average sample size and the sample array
sample_size = 10
sample = [0 for _ in range(sample_size)]
current_index = 0

# Create an instance of the RealTimePlot class
plot = RealTimePlot(x_limit=100, y_limit=(0, 1023))  # Adjust y_limit based on the expected data range


def data_generator():
    global current_index  # Use global if modifying current_index inside the function

    while True:
        data = ser.readline()
        data = str(data)[2:-5]
        try:
            # Read and update the sample array with the new data point
            sample[current_index] = int(data)
        except ValueError:
            # If data is invalid, set the sample to 0 at the current index
            sample[current_index] = 0

        # Update the circular index
        current_index = (current_index + 1) % sample_size

        # Calculate the simple moving average
        sma = int(sum(sample) / sample_size)
        print(sma)

        # Yield the SMA value for real-time plotting
        yield sma


# Start the real-time plotting animation
plot.start_animation(data_generator())
