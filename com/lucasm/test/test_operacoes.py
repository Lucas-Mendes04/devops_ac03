def function(numero):
	return numero * 12

def test_um():
	assert function(1) == 12

def test_dois():
	assert function(2) == 24

def test_dez():
	assert function(10)  == 120