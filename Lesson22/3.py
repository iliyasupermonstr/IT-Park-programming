def format_time(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"

seconds = 86465
formatted_time = format_time(seconds)
print(formatted_time)