tanya_time = int(input())
tanya_band = int(input())
pod_band = int(input())

time_in_utc = tanya_time - tanya_band
pod_time = (time_in_utc + pod_band + 24) % 24
print(pod_time)