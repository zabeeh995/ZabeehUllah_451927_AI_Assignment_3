from datetime import datetime

def time_delta(t1, t2):
    format_str = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, format_str)
    time2 = datetime.strptime(t2, format_str)
    delta = abs(int((time1 - time2).total_seconds()))
    return delta

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        t1 = input().strip()
        t2 = input().strip()
        result = time_delta(t1, t2)
        print(result)
