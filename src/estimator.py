def estimator(data1):
    avgDailyIncomeInUSD = data["region"]["avgDailyIncomeInUSD"]
    avgDailyIncomePopulation = data["region"]['avgDailyIncomePopulation']
    periodType = data["periodType"]
    timeToElapse = data["timeToElapse"]
    reportedCases = data["reportedCases"]
    totalHospitalBeds = dataga["totalHospitalBeds"]
    #for impact we represent it by I
    #for sever inpact we represent it by SI

    currentlyInfectedI = reportedCases * 10
    currentlyInfectedSI = reportedCases * 50

    #add a for loop to check for time lapse format
    if periodType == "days":
        infectionsByRequestedTimeI = currentlyInfectedI*(2**(timeToElapse // 3))
        severeCasesByRequestedTimeI = 0.15 * infectionsByRequestedTimeI
        infectionsByRequestedTimeSI = currentlyInfectedSI*(2**(timeToElapse // 3))
        severeCasesByRequestedTimeSI = 0.15 * infectionsByRequestedTimeSI
        
        avBeds = .35 * totalHospitalBeds

        hospitalBedsByRequestedTimeI = avBeds - severeCasesByRequestedTimeI
        hospitalBedsByRequestedTimeSI = avBeds - severeCasesByRequestedTimeSI

        cFICURT_I = .05 * infectionsByRequestedTimeI 
        cFICURT_SI = .05 * infectionsByRequestedTimeSI 

        cFVBRT_I = .02 * infectionsByRequestedTimeI
        cFVBRT_SI = .02 * infectionsByRequestedTimeSI

        dollarsInFlightI = infectionsByRequestedTimeI * avgDailyIncomePopulation * avgDailyIncomeInUSD                 
        dollarsInFlightSI = infectionsByRequestedTimeSI * avgDailyIncomePopulation * avgDailyIncomeInUSD                 

        
    elif periodType == "weeks":
        timeToElapse = 7 * timeToElapse
        infectionsByRequestedTimeI = currentlyInfectedI * (2 ** (timeToElapse // 3))
        severeCasesByRequestedTimeI = 0.15 * infectionsByRequestedTimeI
        infectionsByRequestedTimeSI = currentlyInfectedSI * (2 ** (timeToElapse // 3))
        severeCasesByRequestedTimeSI = 0.15 * infectionsByRequestedTimeSI
        
        avBeds = .35 * totalHospitalBeds

        hospitalBedsByRequestedTimeI = avBeds - severeCasesByRequestedTimeI
        hospitalBedsByRequestedTimeSI = avBeds - severeCasesByRequestedTimeSI

        cFICURT_I = .05 * infectionsByRequestedTimeI 
        cFICURT_SI = .05 * infectionsByRequestedTimeSI 

        cFVBRT_I = .02 * infectionsByRequestedTimeI
        cFVBRT_SI = .02 * infectionsByRequestedTimeSI

        dollarsInFlightI = infectionsByRequestedTimeI * avgDailyIncomePopulation * avgDailyIncomeInUSD                 
        dollarsInFlightSI = infectionsByRequestedTimeSI * avgDailyIncomePopulation * avgDailyIncomeInUSD 

    elif periodType =="months":
        timeToElapse = 30 * timeToElapse
        infectionsByRequestedTimeI=currentlyInfectedI * (2 ** (timeToElapse // 3))
        severeCasesByRequestedTimeI = 0.15 * infectionsByRequestedTimeI
        infectionsByRequestedTimeSI = currentlyInfectedSI * (2 ** (timeToElapse // 3))
        severeCasesByRequestedTimeSI = 0.15 * infectionsByRequestedTimeSI
        
        avBeds = .35 * totalHospitalBeds

        hospitalBedsByRequestedTimeI = avBeds - severeCasesByRequestedTimeI
        hospitalBedsByRequestedTimeSI = avBeds - severeCasesByRequestedTimeSI

        cFICURT_I = .05 * infectionsByRequestedTimeI 
        cFICURT_SI = .05 * infectionsByRequestedTimeSI 

        cFVBRT_I = .02 * infectionsByRequestedTimeI
        cFVBRT_SI = .02 * infectionsByRequestedTimeSI

        dollarsInFlightI = infectionsByRequestedTimeI * avgDailyIncomePopulation * avgDailyIncomeInUSD                 
        dollarsInFlightSI = infectionsByRequestedTimeSI * avgDailyIncomePopulation * avgDailyIncomeInUSD 
    
    impact1 = {"impact" : {
                    "currentlyInfected": int(currentlyInfectedI),
                    "infectionsByRequestedTime": int(infectionsByRequestedTimeI),
                    "severeCasesByRequestedTime": int(severeCasesByRequestedTimeI),
                    "hospitalBedsByRequestedTime": int(hospitalBedsByRequestedTimeI),
                    "casesForIcuByRequestedTime": int(cFICURT_I),
                    "casesForVentilatorsByRequestedTime": int(cFVBRT_I),
                    "dollarsInFlight": int(dollarsInFlightI),
    }}
    severeImpact1 = {"impact" : {
                    "currentlyInfected": int(currentlyInfectedSI),
                    "infectionsByRequestedTime": int(infectionsByRequestedTimeSI),
                    "severeCasesByRequestedTime": int(severeCasesByRequestedTimeSI),
                    "hospitalBedsByRequestedTime": int(hospitalBedsByRequestedTimeSI),
                    "casesForIcuByRequestedTime": int(cFICURT_SI),
                    "casesForVentilatorsByRequestedTime": int(cFVBRT_SI),
                    "dollarsInFlight": int(dollarsInFlightSI),
    }}

    #for severe impact

    return data1,impact1,severeImpact1
