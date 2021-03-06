# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from django.template.loader import render_to_string

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics

from sklearn.svm import SVC

from sklearn import neighbors

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier

import math


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

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
    pred = clf.predict([[m_radius, m_texture, m_perimeter, m_area, m_smoothness, m_compactness, m_concavity, m_concavePtr, m_symmetry, m_fractalDimension,
           se_radius, se_texture, se_perimeter, se_area, se_smoothness, se_compactness, se_concavity, se_concavePtr, se_symmetry, se_fractalDimension,
           w_radius, w_texture, w_perimeter, w_area, w_smoothness, w_compactness, w_concavity, w_concavePtr, w_symmetry, w_fractalDimension]])
    
    if pred[0] == 1:
        res = "Benign"
    else : 
        res = "Malignant"
    
    html = render_to_string("results.html", {'result': res, 'eff': truncate(efficacite*100,4), 'taux_fp': truncate(taux_fauxPositifs*100,4), 'taux_fn': truncate(taux_fauxNegatifs*100,4)})
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

    cancer = datasets.load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,random_state=109) # 70% training and 30% test
    
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    
    efficacite = metrics.accuracy_score(y_test, y_pred)
    taux_fauxPositifs = 1-metrics.precision_score(y_test, y_pred)
    taux_fauxNegatifs = 1-metrics.recall_score(y_test, y_pred)
    
    pred = clf.predict([[m_radius, m_texture, m_perimeter, m_area, m_smoothness, m_compactness, m_concavity, m_concavePtr, m_symmetry, m_fractalDimension,
           se_radius, se_texture, se_perimeter, se_area, se_smoothness, se_compactness, se_concavity, se_concavePtr, se_symmetry, se_fractalDimension,
           w_radius, w_texture, w_perimeter, w_area, w_smoothness, w_compactness, w_concavity, w_concavePtr, w_symmetry, w_fractalDimension]])
    
    if pred[0] == 1:
        res = "Benign"
    else : 
        res = "Malignant"

    html = render_to_string("results.html", {'result': res, 'eff': truncate(efficacite*100,4), 'taux_fp': truncate(taux_fauxPositifs*100,4), 'taux_fn': truncate(taux_fauxNegatifs*100,4)})
    return HttpResponse(html)


def dt(request):

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

    cancer = datasets.load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,random_state=109) # 70% training and 30% test
    
    clf = DecisionTreeClassifier()
    t = clf.fit(X_train, y_train)
    fig, ax = plt.subplots(figsize=(25, 25))
    tree.plot_tree(t, feature_names=cancer.feature_names, class_names=cancer.target_names, max_depth=6, fontsize=10, filled=True)
    fig.savefig('static/static_local/result_tree/tree.png')
    y_pred = clf.predict(X_test)
    
    efficacite = metrics.accuracy_score(y_test, y_pred)
    taux_fauxPositifs = 1-metrics.precision_score(y_test, y_pred)
    taux_fauxNegatifs = 1-metrics.recall_score(y_test, y_pred)
    
    pred = clf.predict([[m_radius, m_texture, m_perimeter, m_area, m_smoothness, m_compactness, m_concavity, m_concavePtr, m_symmetry, m_fractalDimension,
           se_radius, se_texture, se_perimeter, se_area, se_smoothness, se_compactness, se_concavity, se_concavePtr, se_symmetry, se_fractalDimension,
           w_radius, w_texture, w_perimeter, w_area, w_smoothness, w_compactness, w_concavity, w_concavePtr, w_symmetry, w_fractalDimension]])
    
    if pred[0] == 1:
        res = "Benign"
    else : 
        res = "Malignant"

    html = render_to_string("results_dt.html", {'result': res, 'eff': truncate(efficacite*100,4), 'taux_fp': truncate(taux_fauxPositifs*100,4), 'taux_fn': truncate(taux_fauxNegatifs*100,4)})
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

    cancer = datasets.load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,random_state=109) # 70% training and 30% test
    knn = neighbors.KNeighborsClassifier(n_neighbors=15, weights='uniform')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    
    efficacite = metrics.accuracy_score(y_test, y_pred)
    taux_fauxPositifs = 1-metrics.precision_score(y_test, y_pred)
    taux_fauxNegatifs = 1-metrics.recall_score(y_test, y_pred)
    
    pred = knn.predict([[m_radius, m_texture, m_perimeter, m_area, m_smoothness, m_compactness, m_concavity, m_concavePtr, m_symmetry, m_fractalDimension,
           se_radius, se_texture, se_perimeter, se_area, se_smoothness, se_compactness, se_concavity, se_concavePtr, se_symmetry, se_fractalDimension,
           w_radius, w_texture, w_perimeter, w_area, w_smoothness, w_compactness, w_concavity, w_concavePtr, w_symmetry, w_fractalDimension]])
    
    if pred[0] == 1:
        res = "Benign"
    else : 
        res = "Malignant"
    
    html = render_to_string("results.html", {'result': res, 'eff': truncate(efficacite*100,4), 'taux_fp': truncate(taux_fauxPositifs*100,4), 'taux_fn': truncate(taux_fauxNegatifs*100,4)})
    return HttpResponse(html)