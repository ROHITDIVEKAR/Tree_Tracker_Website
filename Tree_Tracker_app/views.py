import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import Survey

def index(request):
    try:
        data={}
        for survey in Survey.objects.all():
            data.update({
                'latitude':survey.latitude,
                'longitude':survey.longitude,
                'species':survey.species,
                'spreading':survey.spreading,
                'crown_damage':survey.crown_damage,
                'trunk_damage':survey.trunk_damage,
            })
    except:
        pass
    return render(request,'index.html',{'data':data})

def add(request):
    if request.method == 'POST':
        try:
            survey=Survey()
            survey.latitude = request.POST['latitude']
            survey.longitude = request.POST['longitude']
            survey.species=request.POST['species']
            survey.tree_height=request.POST['tree_height']
            survey.steam_diameter=request.POST['steam_diameter']
            survey.crown_height=request.POST['crown_height']
            survey.crown_diameter=request.POST['crown_diameter']
            survey.spreading=request.POST['spreading']
            survey.crown_damage=request.POST['crown_dmg']
            survey.trunk_damage=request.POST['trunk_dmg']
            survey.reason_crown_damage=request.POST['reason_crown_dmg']
            survey.reason_trunk_damage=request.POST['reason_trunk_dmg']
            survey.save()
        except:
            pass   
    else:
        context = {}
    return render(request, 'map.html', context) 

def species(request):
    tree_species = [
    "Acacia",
    "Adenanthera pavonina",
    "Anogeissus",
    "Azadirachta indica",
    "Bauhinia",
    "Bombax ceiba",
    "Casuarina equisetifolia",
    "Cassia fistula",
    "Ficus",
    "Gmelina arborea",
    "Mangifera indica",
    "Neem",
    "Sal",
    "Ashoka tree (Saraca asoca)",
    "Banyan tree (Ficus benghalensis)",
    "Bodhi tree (Ficus religiosa)",
    "Chorisia speciosa (silk floss tree)",
    "Dhak tree (Butea monosperma)",
    "Jamun tree (Syzygium cumini)",
    "Kikar tree (Prosopis cineraria)",
    "Peepal tree (Ficus religiosa)",
    "Saman tree (Samanea saman)",
    "Aegle marmelos (Bael tree)",
    "Albizia lebbeck (Flamboyant tree)",
    "Alstonia scholaris (Scholar tree)",
    "Amaltas tree (Cassia fistula)",
    "Barringtonia acutangula (Sea almond tree)",
    "Boswellia serrata (Frankincense tree)",
    "Calophyllum inophyllum (Santalum album (Sandalwood tree))**",
    "Cassia siamea (Siamese cassia)",
    "Chloroxylon swietenia (Scented wood tree)",
    "Cissus quadrangularis (Gooseberry vine)",
    "Dalbergia sissoo (Sheesham tree)",
    "Dillenia indica (Indian cork tree)",
    "Eucalyptus globulus (Blue gum)",
    "Ficus benghalensis (Banyan tree)",
    "Grewia robusta (Tamarind tree)",
    "Holoptelea integrifolia (Indian Elm tree)",
    "Hyphaene thebaica (Date palm)",
    "Inga vera (Pithecellobium dulce (Monkeypod tree))**",
    "Jacaranda mimosifolia (Jacaranda tree)",
    "Lagerstroemia indica (Crape myrtle)",
    "Mimusops elengi (Plumeria tree)",
    "Nyctanthes arbor-tristis (Night jasmine tree)",
    "Peltophorum pterocarpum (Flame of the forest tree)",
    "Pinus roxburghii (Chilgoza pine tree)",
    "Pterocarpus santalinus (Red sandalwood tree)",
    "Terminalia arjuna (Arjun tree)",
    "Tamarindus indica (Tamarind tree)",
    "Vitex trifolia (Indian privet tree)",
    "Sterculia guttata (Kapok tree)",
    "Wrightia tinctoria (Indian privet)",
    "Grevillea robusta (Silk oak)",
    "Mimusops elengi (Plumeria tree)",
    "Nyctanthes arbor-tristis (Night jasmine tree)",
    "Peltophorum pterocarpum (Flame of the forest tree)",
    "Pinus roxburghii (Chilgoza pine tree)",
    "Prosopis cineraria (Kikar tree)",
    "Pterocarpus santalinus (Red sandalwood tree)"
    ]
    return JsonResponse(tree_species,safe=False)