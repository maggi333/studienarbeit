
def create_latenz_list(msg_send, msg_ack):
    latenz = []
    msg_send_mid = [item[0] for item in msg_send]
    for mid, ack_time in msg_ack:
        ind = msg_send_mid.index(mid)
        mid_s, send_time = msg_send[ind]
        latenz.append((mid, mid_s, ack_time - send_time))
    return latenz


def sum_latenz(latenz_list):
    sum = 0
    i = 0
    for latenz in latenz_list:
        sum = sum + latenz[2]
        i += 1
    return round(sum / i, 6)


def calculate_eval(msg_send, msg_ack):

    # Berechne Liste der Latenzen für jede Nachricht
    latenz_list = create_latenz_list(msg_send, msg_ack)

    # Berechne Durchschnittslatenz
    latenz = sum_latenz(latenz_list)

    # Berechne Nachrichten Verlust
    msg_lost = ((len(msg_send) - len(msg_ack)) / len(msg_send)) * 100
    return latenz, msg_lost
