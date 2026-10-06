def fcfs_disk_scheduling(request_queue, initial_head):
    total_head_movement = 0
    current_head = initial_head
    
    print("FCFS Disk Scheduling")
    print(f"Initial Head Position: {initial_head}")
    print(f"Request Queue: {request_queue}\n")
    
    print("Step\tCurrent Track\tNext Track\tHead Movement")
    print("-" * 55)
    
    for i in range(len(request_queue)):
        next_track = request_queue[i]
        distance = abs(next_track - current_head)
        total_head_movement += distance
        
        print(f"{i+1}\t{current_head}\t\t{next_track}\t\t{distance}")
        current_head = next_track
        
    print("-" * 55)
    print(f"Total Head Movement: {total_head_movement} tracks")
    avg_seek = total_head_movement / len(request_queue)
    print(f"Average Seek Length: {round(avg_seek, 2)} tracks\n")


def scan_disk_scheduling(request_queue, initial_head, disk_size, direction='left'):
    total_head_movement = 0
    current_head = initial_head
    seek_sequence = []

    request_queue.sort()
    left = [r for r in request_queue if r < initial_head]
    right = [r for r in request_queue if r >= initial_head]

    if direction == 'left':
        seek_sequence.extend(reversed(left))
        if 0 not in seek_sequence:
            seek_sequence.append(0)  
        seek_sequence.extend(right)
    else:
        seek_sequence.extend(right)
        if disk_size not in seek_sequence:
            seek_sequence.append(disk_size)  
        seek_sequence.extend(reversed(left))

    print(" SCAN Disk Scheduling (Direction: left) ")
    print(f"Initial Head: {initial_head}, Disk Size: {disk_size}")
    print(f"Seek Sequence: {seek_sequence}\n")

    print("Step\tCurrent Track\tNext Track\tHead Movement")
    print("-" * 55)

    prev_track = initial_head
    for i, track in enumerate(seek_sequence):
        distance = abs(track - prev_track)
        total_head_movement += distance
        print(f"{i+1}\t{prev_track}\t\t{track}\t\t{distance}")
        prev_track = track

    print("-" * 55)
    print(f"Total Head Movement: {total_head_movement} tracks")
    print(f"Average Seek Length: {round(total_head_movement / len(request_queue), 2)} tracks")



request_queue = [98, 183, 37, 122, 14, 124, 65, 67]

fcfs_disk_scheduling(request_queue, initial_head=53)
scan_disk_scheduling(request_queue, initial_head=50, disk_size=200, direction='left')