rain_fall_month = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]


def rainfall_statistics(rain_fall):
    total_rain_fall = sum(rain_fall)
    month_with_lowest_rain_fall = rain_fall_month[rain_fall.index(min(rain_fall))]
    month_with_highest_rain_fall = rain_fall_month[rain_fall.index(max(rain_fall))]
    average_rain_fall = total_rain_fall / len(rain_fall)

    return total_rain_fall, average_rain_fall, month_with_highest_rain_fall, month_with_lowest_rain_fall


if __name__ == '__main__':
    rain_fall_data = []
    for i in rain_fall_month:
        rain_fall = int(input(f"Enter rainfall for {i}: "))
        rain_fall_data.append(rain_fall)

    total_rain_fall, average_rain_fall, month_with_highest_rain_fall, month_with_lowest_rain_fall, = rainfall_statistics(
        rain_fall_data)

    print(f"Total rainfall: {total_rain_fall}")
    print(f"Average rainfall: {average_rain_fall}")
    print(f"Month with highest rainfall: {month_with_highest_rain_fall}")
    print(f"Month with lowest rainfall: {month_with_lowest_rain_fall}")
