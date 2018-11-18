from matplotlib import pyplot


class GraphicsDrawer:
    @staticmethod
    def draw(x_vector, y_vector):
        pyplot.plot(x_vector, y_vector)
        pyplot.show()
