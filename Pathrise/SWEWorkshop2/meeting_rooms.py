def meeting_rooms(times):
   times = sort_by_start_times(times) # this solution only works with sorted times
   rooms = [[times[0]]]
   for idx in range(1, len(times)):
      meeting = times[idx]
      avail_room = find_avail_room(rooms, meeting)
      if avail_room:
         avail_room.append(meeting)
      else:
         rooms.append([meeting])
   return len(rooms)

def find_avail_room(rooms, meeting):
   for room in rooms:
      if room[-1]['end'] <= meeting["start"]:
         return room
   return None

# runtime complexity in n^2, where n is the number of times, because its a double for loop
# O of N space, because you're storing all the times - could store just the last meeting end time


# you could use a Heap to look up the room with the smallest end time