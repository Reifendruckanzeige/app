# a mensagem para o prompt dá certo, agora é necessário integrar com o "content" na api
# precisamos pensar em como receberemos esse input do aplicativo.

def buildMessage(objectName):
    regions = {
        "Tecnotronia": (
            "Tecnotronia é uma metrópole avançada habitada por objetos que personificam a inovação tecnológica. A cidade é uma maravilha de engenharia,"
            "com arranha-céus futuristas, drones que zumbam pelo céu e objetos com implantes cibernéticos."
            "A sociedade aqui é altamente interconectada, composta por objetos como supercomputadores, andróides e dispositivos eletrônicos de alta tecnologia."
            "Os desafios que surgem em Tecnotronia frequentemente envolvem questões tecnológicas, como a segurança digital, a ética da inteligência artificial e a busca por aprimorar suas próprias capacidades tecnológicas."
        ),
        
        "Verdeselva": (
            "Verdeselva é uma região intocada pela civilização, onde objetos relacionados à natureza reinam de forma suprema."
            "A paisagem é composta por florestas exuberantes, montanhas majestosas e rios cristalinos, e os habitantes de Verdeselva são seres feitos de elementos naturais,"
            "como árvores, pedras, animais mágicos e até mesmo constelações encantadas. Eles utilizam a magia da natureza para se comunicar com outros seres e elementos naturais,"
            "protegendo a vida selvagem e explorando os segredos mágicos que permeiam esta terra. As aventuras em Verdeselva frequentemente envolvem a busca por equilíbrio na natureza"
            "e a preservação de seu mundo natural."
        ),
        
        "Utilitron": (
            "Utilitron é uma cidade industrial especializada na criação de utensílios mágicos. Os habitantes são objetos cotidianos que ganharam vida, "
            "como garfos, canetas e relógios. Eles têm habilidades mágicas relacionadas a suas funções. A cidade é um centro de comércio e criação de "
            "utensílios mágicos, e os aventureiros frequentemente buscam itens especiais e enfrentam desafios relacionados à funcionalidade."
        ),
        
        "Automorphia": (
            "Automorphia é uma terra em constante movimento, onde estradas sinuosas e cidades cintilantes são dominadas por carros, motocicletas e veículos autônomos de alta tecnologia."
            "Esta região é um paraíso para entusiastas de veículos, com corridas de rua emocionantes, garagens de alta tecnologia e uma rivalidade feroz entre marcas de veículos."
            "A inovação reina de forma suprema, com laboratórios subterrâneos desenvolvendo tecnologias de transporte de vanguarda,"
            "e os desafios envolvem desde missões de resgate em alta velocidade até a solução de quebra-cabeças relacionados a automóveis."
        ),
        
        "Artalúdico": (
            "Artalúdico é um reino mágico onde objetos relacionados à criatividade e imaginação ganharam vida. "
            "Aqui, pincéis, paletas de cores, blocos de construção e instrumentos musicais formaram uma sociedade baseada na expressão artística. "
            "A paisagem de Artalúdico é um cenário em constante transformação, onde a realidade é moldada pela imaginação. "
            "O solo é feito de tintas mágicas que criam padrões enquanto você pisa, e o ar é preenchido com notas musicais flutuantes."
        )
    }

    attributes = "Força, Destreza, Percepção, Pontos de vida, Classe(Guerreiro/Mago/Ladrão/Paladino/Arqueiro)"

    model = f"Ficha de RPG baseado num {objectName}"\
        "Força: (valor de força)"\
        "Destreza: (valor de destreza)"\
        "Percepção: (valor de percepção)"\
        "Pontos de vida: (valor de pontos de vida)"\
        "Classe: (Guerreiro/Mago/Ladrão/Paladino/Arqueiro)"\
        "Região: (Tecnotronia/Verdeselva/Utilitron/Automorphia/Artalúdico)"\

    message = f"Estou criando uma ficha de personagem de RPG baseado num  {objectName}."\
        f"Eu preciso que você crie um nome relacionado e valores de 0-10 dos atributos (os pontos de vida vão de 0-100): {attributes}."\
        f"Esse personagem precisa se encaixar em uma das regiões com a qual ele mais se relaciona: {regions}"\
        f"Além disso, coloque um, apenas um, breve parágrafo que invente uma história para esse personagem." \
        f"Ao final me retorne no seguinte modelo: {model}"
    
    return message