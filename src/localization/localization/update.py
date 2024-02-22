import rclpy
from rclpy.node import Node

class (Node):

    def __init__(self) :
        super().__init__('')

def main() :
    rclpy.init()
    node = DisplayMarkers()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()
