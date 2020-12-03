# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from django.template.loader import render_to_string

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

def svm(request, kind):

    print(kind);
    
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
        
    # Load and return the breast cancer wisconsin dataset (classification).
    cancer = datasets.load_breast_cancer()
        
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,random_state=109) # 70% training and 30% test
     
    # Create a svm Classifier
    if kind == "1":
        clf = SVC(kernel='linear')

    elif kind == "2":
        clf = SVC(kernel='poly', degree=2, gamma='auto')

    elif kind == "3":
        clf = SVC(kernel='poly', degree=2, gamma='scale')
        
    elif kind == "4":
        clf = SVC(kernel='rbf', gamma='scale')
  
    # Train the model using the training sets
    clf.fit(X_train, y_train)
            
    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    efficacite = metrics.accuracy_score(y_test, y_pred)
    taux_fauxPositifs = 1-metrics.precision_score(y_test, y_pred)
    taux_fauxNegatifs = 1-metrics.recall_score(y_test, y_pred)  
    
    # Predict
    pred = clf.predict([[m_area, m_compactness, m_concavePtr, m_concavity, m_fractalDimension, m_perimeter, m_radius, m_smoothness, m_symmetry, m_texture, se_area, se_compactness, se_concavePtr, se_concavity, se_fractalDimension, se_perimeter, se_radius, se_smoothness, se_symmetry, se_texture, w_area, w_compactness, w_concavePtr, w_concavity, w_fractalDimension, w_perimeter, w_radius, w_smoothness, w_symmetry, w_texture]])
    print(pred)
    if pred[0] == 1:
        res = "Malignant"
    else : 
        res = "Benign"
    
    html = render_to_string("algos/svm.html", {'result': res, 'eff': efficacite, 'taux_fp': taux_fauxPositifs, 'taux_fn': taux_fauxNegatifs})
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