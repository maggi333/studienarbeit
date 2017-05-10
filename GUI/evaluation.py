__author__ = "Maximilian Rasch"

import statistics
import csv
import os


def createCSV(msg_send, msg_ack, evaluation, options):
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
    wr.writerow(("Message ID", "Time message sended", "RSRQ", "RSRP", "RSSI", "SINR"))
    for item in msg_send:
        wr.writerow(item)

    newcsv = open(path + 'msg_ack', 'w')
    wr = csv.writer(newcsv, quoting=csv.QUOTE_ALL)
    wr.writerow(("Message ID", "Time message acknowleged"))
    for item in msg_ack:
        wr.writerow(item)

    newcsv = open(path + 'evaluation', 'w')
    wr = csv.writer(newcsv, quoting=csv.QUOTE_ALL)
    wr.writerow(("MQTT", "CoAP", "Packetgröße", "Sendeintervall", "Anzahl", "QoS(nur MQTT)", "Extra Client"))
    wr.writerow(options)
    wr.writerow("")
    wr.writerow("")
    wr.writerow(("Durschschnittliche Latenz [s]", "Minimum Latenz [s]", "Maximum Latenz [s]", "Standardabweichung",
                 "Nachrichten Verlust [%]", "Durschsnittliche Uebertragungsgeschwindigkeit[kb/s]"))
    wr.writerow(evaluation)


def create_latenz_list(msg_send, msg_ack):
    latenz = []
    msg_send_mid = [item[0] for item in msg_send]
    for mid, ack_time in msg_ack:
        ind = msg_send_mid.index(mid)
        mid_s, send_time, rsrq, rsrp, rssi, sinr = msg_send[ind]
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


def calculate_eval(msg_send, msg_ack, options):

    packet_size = options[2]

    # Berechne Liste der Latenzen für jede Nachricht
    latenz_list = create_latenz_list(msg_send, msg_ack)

    # Berechne Durchschnittslatenz
    latenz = sum_latenz(latenz_list)

    # Min/Max/Standartabweichung der Latenz
    min_lat = min(float(s) for s in latenz_list)
    max_lat = max(float(s) for s in latenz_list)
    try:
        stdev = statistics.stdev(latenz_list)
    except statistics.StatisticsError:  # Wenn nur eine Latenz
        stdev = latenz_list[0]

    # Berechne Nachrichten Verlust
    msg_lost = ((len(msg_send) - len(msg_ack)) / len(msg_send)) * 100

    # Berechne Uebertragungsgeschwindigkeit in kb/s
    speed = packet_size / (latenz * 1000)

    # Schreibe Auswertung in Liste
    evaluation = [latenz, min_lat, max_lat, stdev, msg_lost, speed]

    # Werte Runden für Ausgabe
    latenz = round(latenz, 3)
    min_lat = round(min_lat, 3)
    max_lat = round(max_lat, 3)
    stdev = round(stdev, 3)
    msg_lost = round(msg_lost, 3)
    speed = round(speed, 3)

    # Export to CSV
    createCSV(msg_send, msg_ack, evaluation, options)
    return latenz, min_lat, max_lat, stdev, msg_lost, speed
