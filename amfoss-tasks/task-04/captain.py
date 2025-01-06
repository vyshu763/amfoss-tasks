def captains_room(K, room_list):
    unique_rooms = set(room_list)
    
    total= sum(room_list)
    unique_sum = sum(unique_rooms) * K
    captains_room = (unique_sum - total) // (K - 1)
    
    return captains_room

K = int(input())
room_list = list(map(int, input().split()))

captains_room = captains_room(K, room_list)
print(captains_room)

