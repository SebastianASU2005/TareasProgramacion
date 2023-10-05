import pytest
from funciones import *
#ejercicio 1
@pytest.mark.parametrize("dni_number,res",[
    (94205043,False),
    (457878,False),
    (45966570,True),
    ])
def test_digits(dni_number,res):
    assert digits(dni_number)==res

#ejercicio 2
@pytest.mark.parametrize("phrase,res",[
    ("La vida es una","una"),
    ("Y la felicidad que","que"),
    ("All we need is love","amor"),
    ])
def test_lasr_word(phrase,res):
    assert last_word(phrase)==res
#ejercicio 3
import pytest
from funciones import *
@pytest.mark.parametrize('a,b,res',[
    ('paulo guidolin','44841460','paulo4484')
])
def test_id(a,b,res):
    resultado=id_unico(a,b)
    assert resultado==res
#ejercicio 4
@pytest.mark.parametrize("num1,num2,res",[
    (17,5,"El primer n° es multiplo del segundo"),
    (15,5,"El primer n° es multiplo del segundo"),
    (18,3,"El primer n° es multiplo del segundo"),
])
def test_multi(num1,num2,res):
    assert multi(num1,num2)==res
#ejercicio 5
@pytest.mark.parametrize("num,num1,res",[
    (2,2,2),
    (3,3,3),
    (2,2,3),
])
def test_temperature(num,num1,res):
    assert temperature(num,num1)==res
#ejercicio 6
@pytest.mark.parametrize("phrase,res",[
    ("hola","h o l a "),
    ("juan","j u a n "),
    ("hola","hola"),
])
def test_space(phrase,res):
    assert space(phrase)==res
#ejercicio 7
@pytest.mark.parametrize("number_ls, expected_result", [
    ([1, 2, 3, 4, 5, 6], "Número máximo ,6, y número mínimo ,1"),
    ([1, 2, 3, 4], "Número máximo ,4, y número mínimo ,1"),
    ([1, 2, 3], "Número máximo ,34, y número mínimo ,1"),
])
def test_max_and_min(number_ls, expected_result):
    assert max_and_min(number_ls) == expected_result
#ejercicio 8
@pytest.mark.parametrize("num,radio,res",[ 
    (3.14,2,"12.566370614359172, ' y el perímetro es ', 12.566370614359172")
])
def test_area(num,radio,res):
    assert area(num,radio)==res
#ejercicio 9
import pytest
from funciones import *

@pytest.mark.parametrize('a,b,res',[
    ('usuario1','asdasd',True)
])

def test_9(a,b,res):
    assert login(a,b)==res
    