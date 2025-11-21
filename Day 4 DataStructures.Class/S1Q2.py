
def track_guests():
    guest_ID = list(map(int,input().split()))
    remove_ID = int(input())
    temp = []

    for item in guest_ID:
        if item not in temp:
            temp.append(item)

    if remove_ID in temp:
        temp.remove(remove_ID)

    s = set(temp)

    print(temp)

    

if __name__ == "__main__":
    track_guests()