import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import paho.mqtt.client as mqtt
import json

# MQTT Settings
mqtt_broker = "broker.emqx.io"
mqtt_topic = "robot/velocity"
mqtt_username = "emqx"
mqtt_password = "public"

class MQTTPublisherNode(Node):
    def __init__(self):
        super().__init__('mqtt_publisher_node')
        
        # Set up MQTT client
        self.client = mqtt.Client()
        self.client.username_pw_set(mqtt_username, mqtt_password)
        self.client.connect(mqtt_broker, 1883, 60)
        
        # Create a publisher to listen to the twist topic
        self.twist_subscription = self.create_subscription(
            Twist,
            'cmd_vel',  # This is the ROS2 topic
            self.twist_callback,
            10
        )
        
        # Set QoS for MQTT publishing
        self.client.loop_start()

    def twist_callback(self, msg: Twist):
        # Convert the Twist message to JSON
        twist_data = {
            "linear": {
                "x": msg.linear.x,
                "y": msg.linear.y,
                "z": msg.linear.z
            },
            "angular": {
                "x": msg.angular.x,
                "y": msg.angular.y,
                "z": msg.angular.z
            }
        }
        
        # Publish the JSON message to the ESP32
        self.client.publish(mqtt_topic, json.dumps(twist_data))

def main(args=None):
    rclpy.init(args=args)
    mqtt_publisher = MQTTPublisherNode()
    rclpy.spin(mqtt_publisher)
    mqtt_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()