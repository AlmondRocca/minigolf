"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Minigolf :D"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON) 

        # If you have sprite lists, you should create them here,
        # and set them to None


    def draw_grass(self):
        arcade.start_render() # Must be done before draw

        # Draw the grass grid
        for i in range(0,8):                                                                
            for j in range(0,12):
                if (j % 2 == 0):
                    arcade.draw_rectangle_filled((25 + 100 * i + 50), (25 + 50 * j), 50, 50, arcade.color.LIME_GREEN)  # center x, center y, width, height, color
                else:
                    arcade.draw_rectangle_filled((25 + 100 * i), (25 + 50 * j), 50, 50, arcade.color.LIME_GREEN) # center x, center y, width, height, color

        # Draw the grass border
        arcade.draw_rectangle_filled(400, 5, 800, 10, arcade.color.GRAY)


        arcade.finish_render() # Must be done after draw


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        pass


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass


    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass


    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    game.draw_grass()
    arcade.run()


if __name__ == "__main__":
    main()