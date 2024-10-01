import turtle


def setup_turtle(
    *,
    turtle_speed: int = 0,
    turtle_color: str = "green",
    background_color: str = "black",
    should_hide_turtle: bool = False
) -> None:
    if should_hide_turtle:
        turtle.ht()
    turtle.speed(turtle_speed)
    turtle.bgcolor(background_color)
    turtle.color(turtle_color)


def compute_and_draw_dragon_curve(
    *,
    itercount: int = 10,
    step_length: int = 10,
    right: chr = "r",
    left: chr = "l",
    previous_state: str = "r",
    current_state: str = "r",
    angle: int | float = 90
) -> None:
    for _ in range(itercount):
        current_state = previous_state + right
        for index, char in enumerate(previous_state):
            previous_state = (
                previous_state[:index]
                + (left if char == right else right)
                + previous_state[index + 1 :]
            )
        current_state += previous_state[::-1]
        previous_state = current_state
    setup_turtle()

    for char in current_state:
        turtle.forward(step_length)
        turtle.right(angle) if char == right else turtle.left(angle)


def main(*args, **kwargs) -> None:
    """
    Compute and draw the Dragon curve.
    https://en.wikipedia.org/wiki/L-system
    """
    compute_and_draw_dragon_curve()
    turtle.done()


if __name__ == "__main__":
    main()
