def mru_page_replacement(reference_string, frame_size):
    frames = []
    last_used = {}
    page_faults = 0
    page_hits = 0

    print(f"MRU Page Replacement (Frame Size = {frame_size})")
    print(f"Reference String: {reference_string}\n")

    print("Step\tPage\tFrames\t\tStatus")
    print("-" * 45)

    for i, page in enumerate(reference_string):
        last_used[page] = i

        if page in frames:
            page_hits += 1
            status = "Hit"
        else:
            page_faults += 1
            status = "Fault"
            if len(frames) < frame_size:
                frames.append(page)
            else:
                victim = max(frames, key=lambda p: last_used[p])
                frames[frames.index(victim)] = page

        print(f"{i+1}\t{page}\t{frames}\t\t{status}")

    print("-" * 45)
    print(f"Total Page Faults: {page_faults}")
    print(f"Total Page Hits: {page_hits}")
    print(f"Page Hit Ratio: {round(page_hits / len(reference_string), 2)}")

reference_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frame_size = 4

mru_page_replacement(reference_string, frame_size)