def number(bus_stops):
    #bus_stop is the number of bus stations, can be used as index
    total = 0
    for i in range(len(bus_stops)):
        sub = bus_stops[i][0] - bus_stops[i][1]
        total = total + sub

    return total

