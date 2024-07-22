from collections import defaultdict
meetings = [
    ["10:00 AM", "01:00 PM"],
    ["08:00 PM", "01:00 AM"],
    ["08:00 AM", "11:00 PM"],
    ["06:00 AM", "05:50 AM"],
    ["06:00 AM", "00:00 AM"],
    ["00:00 AM", "01:00 AM"],
    ["03:00 AM", "04:00 AM"],
    ["04:00 AM", "11:59 PM"],
]
# detect change day
# day -- free slots
# no meeting is extended more than 24 hours and similarly free slots






# 1. detect when day changes
day_time = "AM"
night_time = "PM"


def split_meeting_day(cur_day,cur_start_time,cur_end_time,daywise_meeting_dict,cur_meeting):
    if cur_end_time[1] == day_time and cur_start_time[1] == night_time:
            
            last_meeting = ["0:00 AM",cur_meeting[1]]
            daywise_meeting_dict[cur_day].append([cur_meeting[0],"11:59 PM"])
            cur_day +=1
            daywise_meeting_dict[cur_day].append(last_meeting)
    elif cur_end_time[1] == cur_start_time[1] and cur_end_time[0] < cur_start_time[0]:
        
        last_meeting = ["0:00 AM",cur_meeting[1]]
        daywise_meeting_dict[cur_day].append([cur_meeting[0],"11:59 PM"])
        cur_day +=1
        daywise_meeting_dict[cur_day].append(last_meeting)

    else:
        daywise_meeting_dict[cur_day].append(cur_meeting)
        last_meeting = cur_meeting
    return last_meeting, cur_day

def get_day_wise_meeting(meetings):
    cur_day = 0
    last_meeting = None
    daywise_meeting_dict = defaultdict(list)
    ind = 0 
    while ind < len(meetings):
        cur_meeting = meetings[ind]

        cur_start_time = cur_meeting[0].split(" ") 
        cur_end_time = cur_meeting[1].split(" ") 

        if ind == 0:
            last_meeting, cur_day = split_meeting_day(cur_day,cur_start_time,cur_end_time,daywise_meeting_dict,cur_meeting)
            
        else:
            last_meeting_end_time = last_meeting[1].split(" ")
            if last_meeting_end_time[1] == night_time and cur_start_time[1] == day_time:
                cur_day +=1
                last_meeting, cur_day = split_meeting_day(cur_day,cur_start_time,cur_end_time,daywise_meeting_dict,cur_meeting)

            

            elif last_meeting_end_time[1] == cur_start_time[1]:
                if cur_start_time[0] < last_meeting_end_time[0]:
                    cur_day +=1
                    last_meeting, cur_day = split_meeting_day(cur_day,cur_start_time,cur_end_time,daywise_meeting_dict,cur_meeting)
                    
                else:
                    last_meeting, cur_day = split_meeting_day(cur_day,cur_start_time,cur_end_time,daywise_meeting_dict,cur_meeting)
                
            else:
                last_meeting, cur_day = split_meeting_day(cur_day,cur_start_time,cur_end_time,daywise_meeting_dict,cur_meeting)

        ind +=1
    return daywise_meeting_dict

print(get_day_wise_meeting(meetings))






    
    
    