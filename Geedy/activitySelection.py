def activitySelection(activities):
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]

    for i in range(1, len(activities)):
        if(activities[i][0]>=selected[-1][1]):
            selected.append(activities[i])
    return selected

activities = [(1, 4), (2, 3), (3, 5), (0,6), (5, 7), (8, 9)]
print("selected works: ",activitySelection(activities))



"""def activitySelection(activities):
    # কাজগুলো শেষ হওয়ার সময় অনুযায়ী সর্ট করা হচ্ছে
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]  # প্রথম কাজটি নির্বাচন করা হলো

    for i in range(1, len(activities)):
        # যদি বর্তমান কাজের শুরু সময় পূর্ববর্তী নির্বাচিত কাজের শেষ সময়ের পরে হয়
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])  # কাজটি নির্বাচন করা হলো

    return selected  # সব নির্বাচিত কাজগুলো রিটার্ন করা হলো

# ইনপুট কাজের তালিকা
activities = [(1, 4), (2, 3), (3, 5), (0, 6), (5, 7), (8, 9)]
print("নির্বাচিত কাজগুলো:", activitySelection(activities))
"""