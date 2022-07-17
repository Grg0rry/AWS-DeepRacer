def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle

    # Give a very low reward by default
    reward = 1e-3
    
    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.01 * track_width
    marker_2 = 0.08 * track_width
    marker_3 = 0.25 * track_width
    marker_4 = 0.35 * track_width
    marker_5 = 0.5 * track_width
    
    # Set the speed threshold based your action space
    SPEED_THRESHOLD = 1.0
    
    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if not all_wheels_on_track:
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
        reward = 0.5
    else:
        reward = 1
    # and (0.5*track_width - distance_from_center) >= 0.05:
    
    # Give higher reward if the car is closer to center line and vice versa
    if all_wheels_on_track and distance_from_center <= marker_1:
        reward = 1.0
    elif all_wheels_on_track and distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.2
    elif distance_from_center <= marker_4:
        reward = 0.1
    elif distance_from_center <= marker_5:
        reward = 0.001
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15 
    
    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    
    return float(reward)