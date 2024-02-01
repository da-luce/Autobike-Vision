#!/usr/bin/env python

import rospy
from std_msgs.msg import String

"""
Declares a node named 'talker' publishes to the topic cloud_in

TO DO:
- Change published topic cloud_in if necessary
- Change 'String' to the message type of the cloud_in topic
- Change queue_size (limits the amount of queued messages if subscriber isn't receiving them fast enough)
"""
def talker():
    pub = rospy.Publisher('cloud_in', String, queue_size=10)
    rospy.init_node('talker', anoynmous=True)

    # Looping at 10 times per second
    rate = rospy.Rate(10)

    # Publishes string to topic, prints message to log, sleeps to maintain desired loop rate
    while not rospy.is_shutdown():
        data_str = "Talker: " % rospy.get_time()
        rospy.loginfo(data_str)
        pub.publish(data_str)
        rate.sleep()

if __name__ == '__main__':
    # Catches exception that can be thrown by sleep() when operation is cancelled or node is shutdown
    try:
        talker()
    except rospy.ROSInterruptException:
        pass