from django.shortcuts import render
import os
import json


def read_file(name):
    file = r"\organisations\{0}.json".format(name)
    path = os.getcwd() + file
    with open(path, "r", encoding='utf-8') as fh:
        data = json.load(fh)
    return data

def add_text_to_file(name, text):
    file = r"\organisations\{0}.json".format(name)
    path = os.getcwd() + file
    with open(path, "w", encoding='utf-8') as fh:
        fh.write(text)
    pass

def main(request):
    orgs = read_file("Organisations")
    return render(request, "organisations/orgs.html", {'orgs': orgs})

def get_employees(request):
    orgs = read_file("Organisations")
    for i in orgs:
        if i["name"] == request.POST.get("org"):
            return render(request, "organisations/employees.html", {'org': i})

    return render(request, "organisations/orgs.html", {'orgs': orgs})

def get_vacation(request):
    orgs = read_file("Organisations")
    for i in orgs:
        if i["name"] == request.POST.get("vacation"):
            for j in i["employees"]:
                if j["last_name"] == request.POST.get("name"):
                    return render(request, "organisations/vacation.html", {'org': j})

    return render(request, "organisations/orgs.html", {'orgs': orgs})

def admin(request):
    orgs = read_file("Organisations")
    info_adm = read_file("Admin")
    info_man = read_file("Manager")
    for i in info_adm:
        if request.POST.get('login') == i["login"] and request.POST.get('password') == i["password"]:
            return render(request, "organisations/admin.html", {'orgs': orgs})
    for i in info_man:
        if request.POST.get('login') == i["login"] and request.POST.get('password') == i["password"]:
            return render(request, "organisations/manager.html", {'orgs': orgs})

    return render(request, "organisations/orgs.html", {'orgs': orgs})

def add_manager(request):
    managers = read_file("Manager")
    orgs = read_file("Organisations")
    manager = {"login": request.POST.get("login"),
                  "password": request.POST.get("password")}
    managers.append(manager)
    add_text_to_file("Manager", str(managers).replace("\'", "\""))

    return render(request, "organisations/orgs.html", {'orgs': orgs})

def add_orgs(request):
    orgs = read_file("Organisations")
    p = True
    for i in orgs:
        if i["name"] == request.POST.get("name"):
            p = False
    if p:
        if request.POST.get("name") != None and request.POST.get("date") != None:
            new_org = {"name": request.POST.get("name"),
                 "date": request.POST.get("date"),
                 "place": request.POST.get("place"),
                 "description": request.POST.get("description"),
                 "employees": []
                }
            orgs.append(new_org)
            add_text_to_file("Organisations", str(orgs).replace("\'", "\""))
            return render(request, "organisations/orgs.html", {'orgs': orgs})
        else:
            return render(request, "organisations/admin.html", {'orgs': orgs})

    return render(request, "organisations/orgs.html", {'orgs': orgs})

def add_employee(request):
    orgs = read_file("Organisations")
    for i in orgs:
        if i["name"] == request.POST.get("1"):
            employee = {
                "number": request.POST.get("number"),
                "last_name": request.POST.get("last_name"),
                "first_name": request.POST.get("first_name"),
                "patronymic": request.POST.get("patronymic"),
                "bday": request.POST.get("bday"),
                "inn": request.POST.get("inn"),
                "degree": request.POST.get("degree"),
                "adress": request.POST.get("adress"),
                "phone": request.POST.get("phone"),
                "snils": request.POST.get("snils"),
                "passport_num": request.POST.get("passport_num"),
                "passport_date": request.POST.get("passport_date"),
                "vacation": []
            }
            i["employees"].append(employee)
            add_text_to_file("Organisations", str(orgs).replace("\'", "\""))
            return render(request, "organisations/admin.html", {'orgs': orgs})

    return render(request, "organisations/orgs.html", {'orgs': orgs})

def add_vacation(request):
    orgs = read_file("Organisations")
    for i in orgs:
        if i["name"] == request.POST.get("vacation"):
            for j in i["employees"]:
                if j["last_name"] == request.POST.get("name"):
                    vacation = {
                        "fday": request.POST.get("fday"),
                        "lday": request.POST.get("lday"),
                        "absence_type": request.POST.get("absence_type"),
                        "status": request.POST.get("status")
                    }
                    j["vacation"].append(vacation)
                    add_text_to_file("Organisations", str(orgs).replace("\'", "\""))
                    return render(request, "organisations/admin.html", {'orgs': orgs})

    return render(request, "organisations/orgs.html", {'orgs': orgs})

def delete_org(request):
    orgs = read_file("Organisations")
    for i in orgs:
        if i["name"] == request.POST.get("deleteorg"):
            orgs.remove(i)
            add_text_to_file("Organisations", str(orgs).replace("\'", "\""))
            return render(request, "organisations/admin.html", {'orgs': orgs})

    return render(request, "organisations/orgs.html", {'orgs': orgs})

def delete_empl(request):
    orgs = read_file("Organisations")
    for i in orgs:
        if i["name"] == request.POST.get("1"):
            for j in i["employees"]:
                if j["last_name"] == request.POST.get("lnameempl") and j["first_name"] == request.POST.get("fnameempl") and j["patronymic"] == request.POST.get("patrempl"):
                    i["employees"].remove(j)
                    add_text_to_file("Organisations", str(orgs).replace("\'", "\""))
                    return render(request, "organisations/admin.html", {'orgs': orgs})

    return render(request, "organisations/orgs.html", {'orgs': orgs})

def delete_vac(request):
    orgs = read_file("Organisations")
    for i in orgs:
        if i["name"] == request.POST.get("1"):
            for j in i["employees"]:
                if j["last_name"] == request.POST.get("name"):
                    for k in j["vacation"]:
                        if k["fday"] == request.POST.get("deletevac"):
                            j["vacation"].remove(k)
                            add_text_to_file("Organisations", str(orgs).replace("\'", "\""))
                            return render(request, "organisations/admin.html", {'orgs': orgs})

    return render(request, "organisations/orgs.html", {'orgs': orgs})

def delete_man(request):
    info = read_file("Manager")
    orgs = read_file("Organisations")
    for i in info:
        if i["login"] == request.POST.get("deletelogin") and i["password"] == request.POST.get("deletepassword"):
            info.remove(i)
            add_text_to_file("Manager", str(info).replace("\'", "\""))
            return render(request, "organisations/admin.html", {'orgs': orgs})

    return render(request, "organisations/orgs.html", {'orgs': orgs})
