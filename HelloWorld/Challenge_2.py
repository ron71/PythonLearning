raw_ip_address = input("Enter the IP Address")
if len(raw_ip_address) != 0:
    if raw_ip_address[0] == ".":                      # removing full stop from front
        ip_address = ''
        for char in range(1, len(raw_ip_address)):
            ip_address += raw_ip_address[char]
        raw_ip_address = ip_address

    # now removing full stop from last
    if raw_ip_address[len(raw_ip_address)-1] == '.':
        ip_address = ""
        for char in range(0, len(raw_ip_address)-1):
            ip_address += raw_ip_address[char]
        raw_ip_address = ip_address

    # adding a full stop implicitly
    raw_ip_address += "."

    segmentList = []
    segment = ''

    for i in raw_ip_address:
        if i == ".":
            segmentList.append(segment)
            segment = ''
        else:
            segment += i

    print("NO OF SEGMENTS\t:\t{0}".format(len(segmentList)))

    for seg in segmentList:
        print(len(seg))

else:
    print("No IP ADDRESS FOUND")
