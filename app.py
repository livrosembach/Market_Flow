from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Product:
    def __init__(self, name, aisle):
        self.__name = name
        self.__aisle = aisle
    
    def getName(self):
        return self.__name
    
    def getAisle(self):
        return self.__aisle

class Aisle:
    def __init__(self, index, type):
        self.__index = index
        self.__type = type
        self.__productsList = []

    def getIndex(self):
        return self.__index

    def getType(self):
        return self.__type

    def setProductsList(self, product):
        self.__productsList.append(product)
    
    def getProductsList(self):
        return self.__productsList

class Market:
    def __init__(self, name):
        self.__name = name
        self.__aisleList = [
            Aisle(0,"Outros"),
            Aisle(1, "Bebidas Alcolicas ou Refrigerantes"),
            Aisle(2, "Água, Sucos ou Isotônicos"),
            Aisle(3, "Utilidades para Casa ou Festa"),
            Aisle(4, "Pets, Manutenção e Lazer"),
            Aisle(5, "Enxoval e Papelaria"),
            Aisle(6, "Itens de Limpeza para Banheiro e Organização"),
            Aisle(7, "Papel Higiênico"),
            Aisle(8, "Itens de Papel e Cuidados Infantis"),
            Aisle(9, "Limpeza Doméstica e Detergentes"),
            Aisle(10, "Produtos de Lavanderia"),
            Aisle(11, "Itens de Banho e Higiene Pessoal"),
            Aisle(12, "Guloseimas e Ingredientes Doces"),
            Aisle(13, "Massas, Molhos e Temperos"),
            Aisle(14, "Condimentos e Conservas"),
            Aisle(15, "Biscoitos e Bolachas"),
            Aisle(16, "Chás, Cafés e Complementos"),
            Aisle(17, "Grãos e Misturas Alimentares"),
            Aisle(18, "Leite e Itens para Café da Manhã"),
            Aisle(19, "Salgadinhos"),
            Aisle(20, "Farinha, Arroz e Açúcar"),
            Aisle(21, "Carnes, Queijos, Congelados e Refrigerados"),
            Aisle(22, "Frutas, Verduras e Legumes")
        ]
    def addAisle(self, aisle):
        self.__aisleList.append(aisle)

    def getAisleList(self):
        return self.__aisleList

class MarketList:
    def __init__(self):
        self.__listProducts = []

    def addProduct(self, product):
        self.__listProducts.append(product)

    def getSortedListProducts(self):
        return sorted(self.__listProducts, key=lambda p: p.getAisle().getIndex())


market = Market("Gigante Atacadista")
market_list = MarketList()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    try:
        aisle_index = int(request.form['aisle'])
    except ValueError:
        return jsonify({'status': 'error', 'message': 'Invalid aisle index'})

    aisle = next((a for a in market.getAisleList() if a.getIndex() == aisle_index), None)
    if aisle:
        product = Product(name, aisle)
        market_list.addProduct(product)
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'Aisle not found'})

@app.route('/get_products')
def get_products():
    products = market_list.getSortedListProducts()
    return jsonify([{'name': p.getName(), 'aisle': p.getAisle().getType()} for p in products])

if __name__ == '__main__':
    app.run(debug=True)
