# web_scraping

A página da gupy utiliza rolagem contínua ao invés de paginação, então utilizei o webdriver para abrir todos os elementos da lista do "front" do site, em seguida selecionei um nome da class da div que englobava as informações do cargo, nome da empresa e cidade da vaga, coletei essas informações e salvei em uma lista. Como a página principal do site da gupy não começa com a listagem das vagas, para fazer uma busca maior, criei uma lista com nomes de vagas e coloquei uma variavel no url do site para passar por cada item da lista e aumentar o número de vagas pesquisadas.
