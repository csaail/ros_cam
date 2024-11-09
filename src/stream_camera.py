#!/usr/bin/env python

import rospy
import subprocess

def start_stream():
    rospy.init_node('pluto_camera_stream_node', anonymous=True)
    rospy.loginfo("Starting Pluto Camera live stream...")

    # Run the streaming command
    command = "plutocam stream start --out-file - | ffplay -i -fflags nobuffer -flags low_delay -probesize 32 -sync ext -"
    try:
        process = subprocess.Popen(command, shell=True)
        rospy.loginfo("Streaming from Pluto camera.")
        process.wait()  # Waits for the process to complete
    except Exception as e:
        rospy.logerr(f"Error occurred: {e}")
    finally:
        process.terminate()

if __name__ == '__main__':
    start_stream()
