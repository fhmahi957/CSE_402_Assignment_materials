def sstf_disk_scheduling(request_queue, initial_head):
    total_head_movement = 0
    current_head = initial_head
    remaining = list(request_queue)
    step = 1

    print("SSTF Disk Scheduling")
    print(f"Initial Head Position: {initial_head}\n")

    print("Step\tCurrent Track\tNext Track\tHead Movement")
    print("-" * 55)

    while remaining:
        next_track = min(remaining, key=lambda x: abs(x - current_head))
        distance = abs(next_track - current_head)
        total_head_movement += distance

        print(f"{step}\t{current_head}\t\t{next_track}\t\t{distance}")
        current_head = next_track
        remaining.remove(next_track)
        step += 1

    print("-" * 55)
    print(f"Total Head Movement: {total_head_movement} tracks")

    avg_seek = total_head_movement / len(request_queue)
    print(f"Average Seek Length: {round(avg_seek, 2)} tracks")

request_queue = [60, 20, 100, 10, 15, 22, 42]
initial_head = 50

sstf_disk_scheduling(request_queue, initial_head)