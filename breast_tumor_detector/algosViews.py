# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from django.template.loader import render_to_string

def svm(request, kind):

    m_area = request.POST.get('m-area')
    m_compactness = request.POST.get('m-compactness')
    m_concavePtr = request.POST.get('m-concavePtr')
    m_concavity = request.POST.get('m-concavity')
    m_fractalDimension = request.POST.get('m-fractalDimension')
    m_perimeter = request.POST.get('m-perimeter')
    m_radius = request.POST.get('m-radius')
    m_smoothness = request.POST.get('m-smoothness')
    m_symmetry = request.POST.get('m-symmetry')
    m_texture = request.POST.get('m-texture')

    se_area = request.POST.get('se-area')
    se_compactness = request.POST.get('se-compactness')
    se_concavePtr = request.POST.get('se-concavePtr')
    se_concavity = request.POST.get('se-concavity')
    se_fractalDimension = request.POST.get('se-fractalDimension')
    se_perimeter = request.POST.get('se-perimeter')
    se_radius = request.POST.get('se-radius')
    se_smoothness = request.POST.get('se-smoothness')
    se_symmetry = request.POST.get('se-symmetry')
    se_texture = request.POST.get('se-texture')

    w_area = request.POST.get('w-area')
    w_compactness = request.POST.get('w-compactness')
    w_concavePtr = request.POST.get('w-concavePtr')
    w_concavity = request.POST.get('w-concavity')
    w_fractalDimension = request.POST.get('w-fractalDimension')
    w_perimeter = request.POST.get('w-perimeter')
    w_radius = request.POST.get('w-radius')
    w_smoothness = request.POST.get('w-smoothness')
    w_symmetry = request.POST.get('w-symmetry')
    w_texture = request.POST.get('w-texture')

    efficacite = 0
    taux_fauxPositifs = 0
    taux_fauxNegatifs = 0

    if kind == 1:
        #algo 1
        #calculs taux
        0==0
    elif kind == 2:
        #algo 2
        #calculs taux
        0==0
    elif kind == 3:
        #algo 3
        #calculs taux
        0==0

    html = render_to_string("algos/svm.html", {'eff':efficacite, 'taux_fp': taux_fauxPositifs, 'taux_fn': taux_fauxNegatifs})
    return HttpResponse(html)
	

def rf(request):

    m_area = request.POST.get('m-area')
    m_compactness = request.POST.get('m-compactness')
    m_concavePtr = request.POST.get('m-concavePtr')
    m_concavity = request.POST.get('m-concavity')
    m_fractalDimension = request.POST.get('m-fractalDimension')
    m_perimeter = request.POST.get('m-perimeter')
    m_radius = request.POST.get('m-radius')
    m_smoothness = request.POST.get('m-smoothness')
    m_symmetry = request.POST.get('m-symmetry')
    m_texture = request.POST.get('m-texture')

    se_area = request.POST.get('se-area')
    se_compactness = request.POST.get('se-compactness')
    se_concavePtr = request.POST.get('se-concavePtr')
    se_concavity = request.POST.get('se-concavity')
    se_fractalDimension = request.POST.get('se-fractalDimension')
    se_perimeter = request.POST.get('se-perimeter')
    se_radius = request.POST.get('se-radius')
    se_smoothness = request.POST.get('se-smoothness')
    se_symmetry = request.POST.get('se-symmetry')
    se_texture = request.POST.get('se-texture')

    w_area = request.POST.get('w-area')
    w_compactness = request.POST.get('w-compactness')
    w_concavePtr = request.POST.get('w-concavePtr')
    w_concavity = request.POST.get('w-concavity')
    w_fractalDimension = request.POST.get('w-fractalDimension')
    w_perimeter = request.POST.get('w-perimeter')
    w_radius = request.POST.get('w-radius')
    w_smoothness = request.POST.get('w-smoothness')
    w_symmetry = request.POST.get('w-symmetry')
    w_texture = request.POST.get('w-texture')

	#algo + calculs taux
    efficacite = 0
    taux_fauxPositifs = 0
    taux_fauxNegatifs = 0

    html = render_to_string("algos/random_forest.html", {'eff':efficacite, 'taux_fp': taux_fauxPositifs, 'taux_fn': taux_fauxNegatifs})
    return HttpResponse(html)

def knn(request):

    m_area = request.POST.get('m-area')
    m_compactness = request.POST.get('m-compactness')
    m_concavePtr = request.POST.get('m-concavePtr')
    m_concavity = request.POST.get('m-concavity')
    m_fractalDimension = request.POST.get('m-fractalDimension')
    m_perimeter = request.POST.get('m-perimeter')
    m_radius = request.POST.get('m-radius')
    m_smoothness = request.POST.get('m-smoothness')
    m_symmetry = request.POST.get('m-symmetry')
    m_texture = request.POST.get('m-texture')

    se_area = request.POST.get('se-area')
    se_compactness = request.POST.get('se-compactness')
    se_concavePtr = request.POST.get('se-concavePtr')
    se_concavity = request.POST.get('se-concavity')
    se_fractalDimension = request.POST.get('se-fractalDimension')
    se_perimeter = request.POST.get('se-perimeter')
    se_radius = request.POST.get('se-radius')
    se_smoothness = request.POST.get('se-smoothness')
    se_symmetry = request.POST.get('se-symmetry')
    se_texture = request.POST.get('se-texture')

    w_area = request.POST.get('w-area')
    w_compactness = request.POST.get('w-compactness')
    w_concavePtr = request.POST.get('w-concavePtr')
    w_concavity = request.POST.get('w-concavity')
    w_fractalDimension = request.POST.get('w-fractalDimension')
    w_perimeter = request.POST.get('w-perimeter')
    w_radius = request.POST.get('w-radius')
    w_smoothness = request.POST.get('w-smoothness')
    w_symmetry = request.POST.get('w-symmetry')
    w_texture = request.POST.get('w-texture')

	#algos + calculs taux
    efficacite = 0
    taux_fauxPositifs = 0
    taux_fauxNegatifs = 0

    html = render_to_string("algos/knn.html", {'eff':efficacite, 'taux_fp': taux_fauxPositifs, 'taux_fn': taux_fauxNegatifs})
    return HttpResponse(html)