#!/usr/bin/env python

import rospy
from std_msgs.msg import String

"""
When new messages are received, callback is invoked with the message as the argument.
Here, the method prints the the following to the log.
"""
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " heard %s", data.data)
    
"""
Declares a node (named listener) subscribes to the topic "octomap_binary"

TO DO:
- Change the topic the node subscribes to, if necessary
- Change 'String' depending on the message type of the node it's subscribed to
"""
def listener():
    # anonymous=True makes sure each node name is unique
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("octomap_binary", String, callback)

    # keeps Python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()