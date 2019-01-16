from django.shortcuts import render, HttpResponse
import json

def index(request):
    return render(request, 'index.html')

def adminpanel(request):
    data = open("logins.json").read()
    data = json.loads(data)
    if request.POST:
        for i in data:
            if i['login'] == request.POST.get('username') and i['password'] == request.POST.get('password'):
                base1 = open('arrivalsDB.json')
                baseread1 = base1.read()
                base1.close()
                arrivalsdb = json.loads(baseread1)

                base2 = open('departuresDB.json')
                baseread2 = base2.read()
                base2.close()
                departuresdb = json.loads(baseread2)
                return render(request, "adminpanel.html", {'a': arrivalsdb, 'b': departuresdb})
    return render(request, 'error.html')

def error(request):
    return(request, 'error.html')

def arrivals(request):
	base = open('arrivalsDB.json')
	baseread = base.read()
	base.close()
	arrivalsdb = json.loads(baseread)
	return render(request, 'arrivals.html', {'a': arrivalsdb})

def departures(request):
	base = open('departuresDB.json')
	baseread = base.read()
	base.close()
	departuresdb = json.loads(baseread)
	return render(request, 'departures.html', {'b': departuresdb})


def addarrival(request):
    if request.POST:
        dbase1  = json.load(open("arrivalsDB.json"))
        new_arrival = {
            "time": request.POST.get("time"),
            "flight_number": request.POST.get("flight_number"),
            "origin": request.POST.get("origin"),
            "aircraft": request.POST.get("aircraft"),
            "status": request.POST.get("status"),
        }
        dbase1.append(new_arrival)
        database1 = open('arrivalsDB.json', 'w').write(json.dumps(dbase1))
        return render(request, 'adminpanel.html', {'a': dbase1})

def deletearrival(request):
    dbase2  = json.load(open("arrivalsDB.json"))
    for i in range(len(dbase2)):
        if dbase2[i]["flight_number"] == request.POST.get("flight_number"):
            dbase2.pop(i)
            break

    database2 = open('arrivalsDB.json', 'w').write(json.dumps(dbase2))
    return render(request, 'adminpanel.html', {'a': dbase2})


def adddeparture(request):
    if request.POST:
        dbase3  = json.load(open("departuresDB.json"))
        new_departure = {
            "time": request.POST.get("time"),
            "flight_number": request.POST.get("flight_number"),
            "aircraft": request.POST.get("aircraft"),
            "status": request.POST.get("status"),
            "destination": request.POST.get("destination"),
        }
        dbase3.append(new_departure)
        database3 = open('departuresDB.json', 'w').write(json.dumps(dbase3))
        return render(request, 'adminpanel.html', {'b': dbase3})


def deletedeparture(request):
    dbase4  = json.load(open("departuresDB.json"))
    for i in range(len(dbase4)):
        if dbase4[i]["flight_number"] == request.POST.get("flight_number"):
            dbase4.pop(i)
            break

    database4 = open('departuresDB.json', 'w').write(json.dumps(dbase4))
    return render(request, 'adminpanel.html', {'b': dbase4})
