def ge_time_calculation(times):
    agentSeconds = 0
    agentMinutes = 0
    agentHours = 0
    sAgentSeconds = 0
    sAgentMinutes = 0
    sAgentHours = 0
    dAgentSeconds = 0
    dAgentMinutes = 0
    dAgentHours = 0
    totalSeconds = 0
    totalMinutes = 0
    totalHours = 0

    for n in range(0,20):
        agentSeconds += times[3*n+1].second
        if agentSeconds >= 60:
            agentSeconds -= 60
            agentMinutes += 1
        agentMinutes += times[3*n+1].minute
        if agentMinutes >= 60:
            agentMinutes -= 60
            agentHours += 1
        agentHours += times[3*n+1].hour
    for n in range(0,20):
        sAgentSeconds += times[3*n+2].second
        if sAgentSeconds >= 60:
            sAgentSeconds -= 60
            sAgentMinutes += 1
        sAgentMinutes += times[3*n+2].minute
        if sAgentMinutes >= 60:
            sAgentMinutes -= 60
            sAgentHours += 1
        sAgentHours += times[3*n+2].hour
    for n in range(0,20):
        dAgentSeconds += times[3*n].second
        if dAgentSeconds >= 60:
            dAgentSeconds -= 60
            dAgentMinutes += 1
        dAgentMinutes += times[3*n].minute
        if dAgentMinutes >= 60:
            dAgentMinutes -= 60
            dAgentHours += 1
        dAgentHours += times[3*n].hour

    totalSeconds += (agentSeconds + sAgentSeconds + dAgentSeconds)
    if totalSeconds >= 120:
        totalSeconds -= 120
        totalMinutes += 2
    if totalSeconds >= 60:
        totalSeconds -= 60
        totalMinutes += 1
    totalMinutes += (agentMinutes + sAgentMinutes + dAgentMinutes)
    if totalMinutes >= 120:
        totalMinutes -= 120
        totalHours += 2
    if totalMinutes >= 60:
        totalMinutes -= 60
        totalHours += 1
    totalHours += (agentHours + sAgentHours + dAgentHours)
    return agentHours, agentMinutes, agentSeconds, sAgentHours, sAgentMinutes, sAgentSeconds, dAgentHours, dAgentMinutes, dAgentSeconds, totalHours, totalMinutes, totalSeconds

# The following is for Perfect Dark when I get around to implimenting that game
# to this program.
def pd_time_calculation(times):
    agentSeconds = 0
    agentMinutes = 0
    agentHours = 0
    sAgentSeconds = 0
    sAgentMinutes = 0
    sAgentHours = 0
    pAgentSeconds = 0
    pAgentMinutes = 0
    pAgentHours = 0
    totalSeconds = 0
    totalMinutes = 0
    totalHours = 0

    for n in range(0,21):
        agentSeconds += times[3*n+1].second
        if agentSeconds >= 60:
            agentSeconds -= 60
            agentMinutes += 1
        agentMinutes += times[3*n+1].minute
        if agentMinutes >= 60:
            agentMinutes -= 60
            agentHours += 1
        agentHours += times[3*n+1].hour
    for n in range(0,21):
        sAgentSeconds += times[3*n+2].second
        if sAgentSeconds >= 60:
            sAgentSeconds -= 60
            sAgentMinutes += 1
        sAgentMinutes += times[3*n+2].minute
        if sAgentMinutes >= 60:
            sAgentMinutes -= 60
            sAgentHours += 1
        sAgentHours += times[3*n+2].hour
    for n in range(0,21):
        pAgentSeconds += times[3*n].second
        if pAgentSeconds >= 60:
            pAgentSeconds -= 60
            pAgentMinutes += 1
        pAgentMinutes += times[3*n].minute
        if pAgentMinutes >= 60:
            pAgentMinutes -= 60
            pAgentHours += 1
        pAgentHours += times[3*n].hour

    totalSeconds += (agentSeconds + sAgentSeconds + pAgentSeconds)
    if totalSeconds >= 120:
        totalSeconds -= 120
        totalMinutes += 2
    if totalSeconds >= 60:
        totalSeconds -= 60
        totalMinutes += 1
    totalMinutes += (agentMinutes + sAgentMinutes + pAgentMinutes)
    if totalMinutes >= 120:
        totalMinutes -= 120
        totalHours += 2
    if totalMinutes >= 60:
        totalMinutes -= 60
        totalHours += 1
    totalHours += (agentHours + sAgentHours + pAgentHours)
    return agentHours, agentMinutes, agentSeconds, sAgentHours, sAgentMinutes, sAgentSeconds, pAgentHours, pAgentMinutes, pAgentSeconds, totalHours, totalMinutes, totalSeconds
