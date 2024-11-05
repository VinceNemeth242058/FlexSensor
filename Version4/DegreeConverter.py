def custom_scaling(x):
    if x < 0 or x > 1000:
        raise ValueError("Input must be between 0 and 1000.")

    if x <= 300:
        # Scale linearly from 0 to 0.3 for inputs 0 to 300
        return x / 1000
    elif x <= 800:
        # Scale linearly from 0.3 to 0.7 for inputs 300 to 800
        return 0.3 + (x - 300) * (0.7 - 0.3) / (800 - 300)
    else:
        # Scale linearly from 0.7 to 1 for inputs 800 to 1000
        return 0.7 + (x - 800) * (1 - 0.7) / (1000 - 800)