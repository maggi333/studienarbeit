import statistics
import csv
import os


def createCSV(msg_send, msg_ack, evaluation):
    path = "result/0/"
    i = 0
    while True:

        if os.path.exists(path):
            i += 1
            path = "result/" + str(i) + "/"
        else:
            os.makedirs(path)
            break

    newcsv = open(path + 'msg_send', 'w')
    wr = csv.writer(newcsv, quoting=csv.QUOTE_ALL)
    wr.writerow(msg_send)

    newcsv = open(path + 'msg_ack', 'w')
    wr = csv.writer(newcsv, quoting=csv.QUOTE_ALL)
    wr.writerow(msg_ack)

    newcsv = open(path + 'evaluation', 'w')
    wr = csv.writer(newcsv, quoting=csv.QUOTE_ALL)
    wr.writerow(evaluation)


def create_latenz_list(msg_send, msg_ack):
    latenz = []
    msg_send_mid = [item[0] for item in msg_send]
    for mid, ack_time in msg_ack:
        ind = msg_send_mid.index(mid)
        mid_s, send_time = msg_send[ind]
        # latenz.append((mid, mid_s, ack_time - send_time))
        latenz.append(ack_time - send_time)
    return latenz


def sum_latenz(latenz_list):
    sum = 0
    i = 0
    for latenz in latenz_list:
        sum = sum + latenz
        i += 1
    return sum / i


def calculate_eval(msg_send, msg_ack):
    # Berechne Liste der Latenzen für jede Nachricht
    latenz_list = create_latenz_list(msg_send, msg_ack)

    # Berechne Durchschnittslatenz
    latenz = round(sum_latenz(latenz_list), 3)
    # Min/Max/Standartabweichung der Latenz
    min_lat = round(min(float(s) for s in latenz_list), 3)
    max_lat = round(max(float(s) for s in latenz_list), 3)
    try:
        stdev = round(statistics.stdev(latenz_list), 3)
    except statistics.StatisticsError:  # Wenn nur eine Latenz
        stdev = round(latenz_list[0], 3)

    # Berechne Nachrichten Verlust
    msg_lost = round(((len(msg_send) - len(msg_ack)) / len(msg_send)) * 100, 3)

    # Export to CSV
    createCSV(msg_send, msg_ack, latenz_list)
    return latenz, min_lat, max_lat, stdev, msg_lost
