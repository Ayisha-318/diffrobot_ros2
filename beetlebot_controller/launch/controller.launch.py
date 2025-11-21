from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
def generate_launch_description():
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager"
        ]
    )
    
    joint_velocity_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_velocity_controller",  
            "--controller-manager",
            "/controller_manager"
        ]
    )
    wheel_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["beetlebot_diff_drive_controller", 
                   "--controller-manager", 
                   "/controller_manager"]         
                   )
    


    twist_relay_node = Node(
        package="beetlebot_controller",
        executable="twist_relay.py",
        name="twist_relay",
        parameters=[{"use_sim_time": True}]
    )


    robot_localization = Node(
        package="robot_localization",
        executable="ekf_node",
        name="ekf_filter_node",
        output="screen",
        parameters=[os.path.join(get_package_share_directory("beetlebot_controller"), "config", "local_ekf.yaml"),
                    {'use_sim_time': True}],
    )

   

    return LaunchDescription([
        joint_state_broadcaster_spawner,
        # joint_velocity_controller,
        wheel_controller_spawner,
        twist_relay_node,
        robot_localization
    ])