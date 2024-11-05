# Import necessary libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class RealTimePlot:
    def __init__(self, x_limit=100, y_limit=(0, 1)):
        """
        Initialize the real-time plot with axis limits and set up the figure and axis.

        Parameters:
        x_limit (int): Maximum x-axis limit.
        y_limit (tuple): y-axis limits as a tuple (min, max).
        """
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.x_data, self.y_data = [], []  # Initialize empty lists to hold x and y data
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)

        # Set axis limits
        self.ax.set_xlim(0, self.x_limit)
        self.ax.set_ylim(self.y_limit)

    def init_plot(self):
        """Initialization function for the animation."""
        self.line.set_data([], [])
        return self.line,

    def update_plot(self, frame, new_data):
        """
        Update function for the animation.

        Parameters:
        frame (int): Current frame number.
        new_data (float): New data point to append to y_data.
        """
        self.x_data.append(frame)
        self.y_data.append(new_data)

        # Update line with new data
        self.line.set_data(self.x_data, self.y_data)

        # Optionally, adjust x-axis to show the last x_limit frames
        if frame > self.x_limit:
            self.ax.set_xlim(frame - self.x_limit, frame)

        return self.line,

    def start_animation(self, data_generator, frames=1000):
        """
        Start the real-time animation.

        Parameters:
        data_generator (callable): A generator or function that yields the next data point.
        frames (int): Number of frames for the animation.
        """

        def update_wrapper(frame):
            # Get the next data point from the provided data generator
            new_data = next(data_generator)
            return self.update_plot(frame, new_data)

        # Create the animation
        self.ani = animation.FuncAnimation(
            self.fig, update_wrapper, frames=range(frames), init_func=self.init_plot, blit=True
        )
        plt.show()
