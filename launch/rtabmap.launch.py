from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # 패키지 경로 가져오기
    package_path = get_package_share_directory('rtabmap_ros')

    # RViz 설정 파일 경로
    rviz_config_file = os.path.join(package_path, 'config', 'rtabmap.rviz')

    return LaunchDescription([
        Node(
            package='rtabmap_ros',
            executable='rtabmap',
            name='rtabmap',
            output='screen',
            parameters=[{'use_sim_time': False}],  # 시뮬레이션 시간 사용 설정
            remappings=[
                ('rgb', '/zed/zed_node/rgb_raw/image_raw_color'),
                ('depth', '/zed/zed_node/depth/depth_registered'),
                ('rgb/camera_info', '/zed/zed_node/rgb/camera_info')
            ],
            arguments=['--delete_db_on_start']
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file]  # RViz 설정 파일 사용
        )
    ])
